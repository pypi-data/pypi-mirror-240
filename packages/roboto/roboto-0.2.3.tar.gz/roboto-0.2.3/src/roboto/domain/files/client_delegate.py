import collections.abc
import pathlib
from typing import Any, Optional
import urllib.parse

import boto3
import boto3.s3.transfer as s3_transfer
import botocore.config
import botocore.credentials
import botocore.session

from ...exceptions import RobotoHttpExceptionParse
from ...http import (
    HttpClient,
    PaginatedList,
    roboto_headers,
)
from ...query import QuerySpecification
from ...serde import pydantic_jsonable_dict
from .delegate import (
    CredentialProvider,
    FileDelegate,
    FileTag,
)
from .progress import (
    NoopProgressMonitorFactory,
    ProgressMonitorFactory,
)
from .record import FileRecord

# Used to change between showing progress bars for every file and "uploading X files"
MANY_FILES = 100


class FileClientDelegate(FileDelegate):
    __http_client: HttpClient
    __roboto_service_base_url: str

    @staticmethod
    def generate_s3_client(
        credential_provider: CredentialProvider, tcp_keepalive: bool = True
    ):
        creds = credential_provider()
        refreshable_credentials = (
            botocore.credentials.RefreshableCredentials.create_from_metadata(
                metadata=creds,
                refresh_using=credential_provider,
                method="roboto-api",
            )
        )
        botocore_session = botocore.session.get_session()
        botocore_session._credentials = refreshable_credentials
        botocore_session.set_config_variable("region", creds["region"])
        session = boto3.Session(botocore_session=botocore_session)

        return session.client(
            "s3", config=botocore.config.Config(tcp_keepalive=tcp_keepalive)
        )

    def __init__(self, roboto_service_base_url: str, http_client: HttpClient) -> None:
        super().__init__()
        self.__http_client = http_client
        self.__roboto_service_base_url = roboto_service_base_url

    def delete_file(self, record: FileRecord) -> None:
        url = f"{self.__roboto_service_base_url}/v1/files/{record.file_id}"

        with RobotoHttpExceptionParse():
            self.__http_client.delete(
                url,
                headers=roboto_headers(
                    resource_owner_id=record.org_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )

    def download_file(
        self,
        record: FileRecord,
        local_path: pathlib.Path,
        credential_provider: CredentialProvider,
        progress_monitor_factory: ProgressMonitorFactory = NoopProgressMonitorFactory(),
    ) -> None:
        local_path.parent.mkdir(parents=True, exist_ok=True)
        s3_client = FileClientDelegate.generate_s3_client(credential_provider)

        res = s3_client.head_object(Bucket=record.bucket, Key=record.key)
        download_bytes = int(res.get("ContentLength", 0))

        progress_monitor = progress_monitor_factory.download_monitor(
            source=record.key, size=download_bytes
        )
        try:
            s3_client.download_file(
                Bucket=record.bucket,
                Key=record.key,
                Filename=str(local_path),
                Callback=progress_monitor.update,
            )
        finally:
            progress_monitor.close()

    def get_record_by_primary_key(
        self, file_id: str, org_id: Optional[str] = None
    ) -> FileRecord:
        url = f"{self.__roboto_service_base_url}/v1/files/record/{file_id}"

        with RobotoHttpExceptionParse():
            res = self.__http_client.get(
                url,
                headers=roboto_headers(
                    org_id=org_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )
        return FileRecord.parse_obj(res.from_json(json_path=["data"]))

    def get_signed_url(self, record: FileRecord) -> str:
        url = f"{self.__roboto_service_base_url}/v1/files/{record.file_id}/signed-url"

        with RobotoHttpExceptionParse():
            res = self.__http_client.get(
                url,
                headers=roboto_headers(
                    org_id=record.org_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )
        return res.from_json(json_path=["data", "url"])

    def query_files(
        self,
        query: QuerySpecification,
        org_id: Optional[str] = None,
    ) -> PaginatedList[FileRecord]:
        url = f"{self.__roboto_service_base_url}/v1/files/query"
        post_body = pydantic_jsonable_dict(query, exclude_none=True)
        with RobotoHttpExceptionParse():
            res = self.__http_client.post(
                url,
                data=post_body,
                headers=roboto_headers(
                    resource_owner_id=org_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )

        unmarshalled = res.from_json(json_path=["data"])
        return PaginatedList(
            items=[FileRecord.parse_obj(dataset) for dataset in unmarshalled["items"]],
            next_token=unmarshalled["next_token"],
        )

    def upload_file(
        self,
        local_path: pathlib.Path,
        bucket: str,
        key: str,
        credential_provider: CredentialProvider,
        tags: Optional[dict[FileTag, str]] = None,
        progress_monitor_factory: ProgressMonitorFactory = NoopProgressMonitorFactory(),
    ) -> None:
        upload_file_args: dict[str, Any] = {
            "Filename": str(local_path),
            "Key": key,
            "Bucket": bucket,
        }

        if tags is not None:
            serializable_tags = {tag.value: value for tag, value in tags.items()}
            encoded_tags = urllib.parse.urlencode(serializable_tags)
            upload_file_args["ExtraArgs"] = {"Tagging": encoded_tags}

        progress_monitor = progress_monitor_factory.upload_monitor(
            source=key, size=local_path.stat().st_size
        )
        upload_file_args["Callback"] = progress_monitor.update

        try:
            s3_client = FileClientDelegate.generate_s3_client(credential_provider)
            s3_client.upload_file(**upload_file_args)
        finally:
            if progress_monitor is not None:
                progress_monitor.close()

    def __upload_many_files(
        self,
        bucket: str,
        file_generator: collections.abc.Generator[tuple[pathlib.Path, str], None, None],
        credential_provider: CredentialProvider,
        progress_monitor_factory: ProgressMonitorFactory = NoopProgressMonitorFactory(),
        max_concurrency: int = 20,
        extra_args: Optional[dict[str, Any]] = None,
    ):
        s3_client = FileClientDelegate.generate_s3_client(credential_provider)
        transfer_config = s3_transfer.TransferConfig(
            use_threads=True, max_concurrency=max_concurrency
        )
        transfer_manager = s3_transfer.create_transfer_manager(
            s3_client, transfer_config
        )

        base_path = progress_monitor_factory.get_context().get("base_path", "?")
        expected_file_count = progress_monitor_factory.get_context().get(
            "expected_file_count", "?"
        )
        expected_file_size = progress_monitor_factory.get_context().get(
            "expected_file_size", -1
        )

        progress_monitor = progress_monitor_factory.upload_monitor(
            source=f"{expected_file_count} files from {base_path}",
            size=expected_file_size,
        )

        try:
            for src, key in file_generator:
                transfer_manager.upload(
                    str(src),
                    bucket,
                    key,
                    extra_args=extra_args,
                    subscribers=[
                        s3_transfer.ProgressCallbackInvoker(progress_monitor.update)
                    ],
                )

            transfer_manager.shutdown()
        finally:
            progress_monitor.close()

    def upload_files(
        self,
        bucket: str,
        file_generator: collections.abc.Generator[tuple[pathlib.Path, str], None, None],
        credential_provider: CredentialProvider,
        tags: Optional[dict[FileTag, str]] = None,
        progress_monitor_factory: ProgressMonitorFactory = NoopProgressMonitorFactory(),
        max_concurrency: int = 20,
    ) -> None:
        extra_args: Optional[dict[str, Any]] = None
        if tags is not None:
            serializable_tags = {tag.value: value for tag, value in tags.items()}
            encoded_tags = urllib.parse.urlencode(serializable_tags)
            extra_args = {"Tagging": encoded_tags}

        expected_file_count = progress_monitor_factory.get_context().get(
            "expected_file_count", "?"
        )

        if expected_file_count >= MANY_FILES:
            self.__upload_many_files(
                bucket=bucket,
                file_generator=file_generator,
                credential_provider=credential_provider,
                progress_monitor_factory=progress_monitor_factory,
                max_concurrency=max_concurrency,
                extra_args=extra_args,
            )
        else:
            for src, key in file_generator:
                self.upload_file(
                    local_path=src,
                    bucket=bucket,
                    key=key,
                    credential_provider=credential_provider,
                    tags=tags,
                    progress_monitor_factory=progress_monitor_factory,
                )
