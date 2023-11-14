#
# Copyright (c) 2021 Nitric Technologies Pty Ltd.
#
# This file is part of Nitric Python 3 SDK.
# See https://github.com/nitrictech/python-sdk for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from dataclasses import dataclass
from typing import Union
from grpclib.client import Channel
from grpclib import GRPCError
from nitric.exception import exception_from_grpc_error, InvalidArgumentException
from nitric.utils import new_default_channel
from nitric.proto.nitric.storage.v1 import (
    StorageServiceStub,
    StoragePreSignUrlRequestOperation,
    StorageWriteRequest,
    StorageReadRequest,
    StorageDeleteRequest,
    StoragePreSignUrlRequest,
    StorageListFilesRequest,
)
from enum import Enum
from warnings import warn


class Storage(object):
    """
    Nitric generic blob storage client.

    This client insulates application code from stack specific blob store operations or SDKs.
    """

    def __init__(self):
        """Construct a Nitric Storage Client."""
        self._channel: Union[Channel, None] = new_default_channel()
        # Had to make unprotected (publically accessible in order to use as part of bucket reference)
        self.storage_stub = StorageServiceStub(channel=self._channel)

    def __del__(self):
        # close the channel when this client is destroyed
        if self._channel is not None:
            self._channel.close()

    def bucket(self, name: str):
        """Return a reference to a bucket from the connected storage service."""
        return BucketRef(_storage=self, name=name)


@dataclass(order=True)
class BucketRef(object):
    """A reference to a bucket in a storage service, used to the perform operations on that bucket."""

    _storage: Storage
    name: str

    def file(self, key: str):
        """Return a reference to a file in this bucket."""
        return File(_storage=self._storage, _bucket=self.name, key=key)

    async def files(self):
        """Return a list of files in this bucket."""
        resp = await self._storage.storage_stub.list_files(
            storage_list_files_request=StorageListFilesRequest(bucket_name=self.name)
        )
        return [self.file(f.key) for f in resp.files]


class FileMode(Enum):
    """Definition of available operation modes for file signed URLs."""

    READ = 0
    WRITE = 1

    def to_request_operation(self) -> StoragePreSignUrlRequestOperation:
        """Convert FileMode to a StoragePreSignUrlRequestOperation."""
        if self == FileMode.READ:
            return StoragePreSignUrlRequestOperation.READ
        elif self == FileMode.WRITE:
            return StoragePreSignUrlRequestOperation.WRITE
        else:
            raise InvalidArgumentException("Invalid FileMode")


@dataclass(frozen=True, order=True)
class File(object):
    """A reference to a file in a bucket, used to perform operations on that file."""

    _storage: Storage
    _bucket: str
    key: str

    async def write(self, body: bytes):
        """
        Write the bytes as the content of this file.

        Will create the file if it doesn't already exist.
        """
        try:
            await self._storage.storage_stub.write(
                storage_write_request=StorageWriteRequest(bucket_name=self._bucket, key=self.key, body=body)
            )
        except GRPCError as grpc_err:
            raise exception_from_grpc_error(grpc_err)

    async def read(self) -> bytes:
        """Read this files contents from the bucket."""
        try:
            response = await self._storage.storage_stub.read(
                storage_read_request=StorageReadRequest(bucket_name=self._bucket, key=self.key)
            )
            return response.body
        except GRPCError as grpc_err:
            raise exception_from_grpc_error(grpc_err)

    async def delete(self):
        """Delete this file from the bucket."""
        try:
            await self._storage.storage_stub.delete(
                storage_delete_request=StorageDeleteRequest(bucket_name=self._bucket, key=self.key)
            )
        except GRPCError as grpc_err:
            raise exception_from_grpc_error(grpc_err)

    async def upload_url(self, expiry: int = 600):
        """Get a temporary writable URL to this file."""
        return await self.sign_url(mode=FileMode.WRITE, expiry=expiry)

    async def download_url(self, expiry: int = 600):
        """Get a temporary readable URL to this file."""
        return await self.sign_url(mode=FileMode.READ, expiry=expiry)

    async def sign_url(self, mode: FileMode = FileMode.READ, expiry: int = 3600):
        """Generate a signed URL for reading or writing to a file."""
        warn("File.sign_url() is deprecated, use upload_url() or download_url() instead", DeprecationWarning)
        try:
            response = await self._storage.storage_stub.pre_sign_url(
                storage_pre_sign_url_request=StoragePreSignUrlRequest(
                    bucket_name=self._bucket, key=self.key, operation=mode.to_request_operation(), expiry=expiry
                )
            )
            return response.url
        except GRPCError as grpc_err:
            raise exception_from_grpc_error(grpc_err)
