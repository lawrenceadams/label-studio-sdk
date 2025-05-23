# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.redis_export_storage import RedisExportStorage
from ...core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from .types.redis_create_response import RedisCreateResponse
from ...core.jsonable_encoder import jsonable_encoder
from .types.redis_update_response import RedisUpdateResponse
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RedisClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RedisExportStorage]:
        """

        You can connect your Redis database to Label Studio as a source storage or target storage. Use this API request to get a list of all Redis export (target) storage connections for a specific project.

        The project ID can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list).

        For more information about working with external storage, see [Sync data from external storage](https://labelstud.io/guide/storage).

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RedisExportStorage]


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.redis.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/export/redis",
            method="GET",
            params={
                "project": project,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[RedisExportStorage],
                    parse_obj_as(
                        type_=typing.List[RedisExportStorage],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        db: typing.Optional[int] = OMIT,
        can_delete_objects: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        path: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        port: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RedisCreateResponse:
        """

        Create a new target storage connection to Redis.

        For information about the required fields and prerequisites, see [Redis database](https://labelstud.io/guide/storage#Redis-database) in the Label Studio documentation.

        <Tip>After you add the storage, you should validate the connection before attempting to sync your data. Your data will not be exported until you [sync your connection](sync).</Tip>

        Parameters
        ----------
        db : typing.Optional[int]
            Database ID of database to use

        can_delete_objects : typing.Optional[bool]
            Deletion from storage enabled.

        title : typing.Optional[str]
            Storage title

        description : typing.Optional[str]
            Storage description

        project : typing.Optional[int]
            Project ID

        path : typing.Optional[str]
            Storage prefix (optional)

        host : typing.Optional[str]
            Server Host IP (optional)

        port : typing.Optional[str]
            Server Port (optional)

        password : typing.Optional[str]
            Server Password (optional)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisCreateResponse


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.redis.create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/export/redis",
            method="POST",
            json={
                "db": db,
                "can_delete_objects": can_delete_objects,
                "title": title,
                "description": description,
                "project": project,
                "path": path,
                "host": host,
                "port": port,
                "password": password,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RedisCreateResponse,
                    parse_obj_as(
                        type_=RedisCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def validate(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        db: typing.Optional[int] = OMIT,
        can_delete_objects: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        path: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        port: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """

        Validate a specific Redis export storage connection. This is useful to ensure that the storage configuration settings are correct and operational before attempting to export data.

        Parameters
        ----------
        id : typing.Optional[int]
            Storage ID. If set, storage with specified ID will be updated

        db : typing.Optional[int]
            Database ID of database to use

        can_delete_objects : typing.Optional[bool]
            Deletion from storage enabled.

        title : typing.Optional[str]
            Storage title

        description : typing.Optional[str]
            Storage description

        project : typing.Optional[int]
            Project ID

        path : typing.Optional[str]
            Storage prefix (optional)

        host : typing.Optional[str]
            Server Host IP (optional)

        port : typing.Optional[str]
            Server Port (optional)

        password : typing.Optional[str]
            Server Password (optional)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.redis.validate()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/export/redis/validate",
            method="POST",
            json={
                "id": id,
                "db": db,
                "can_delete_objects": can_delete_objects,
                "title": title,
                "description": description,
                "project": project,
                "path": path,
                "host": host,
                "port": port,
                "password": password,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> RedisExportStorage:
        """

        Get a specific Redis export storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        For more information about working with external storage, see [Sync data from external storage](https://labelstud.io/guide/storage).

        Parameters
        ----------
        id : int
            A unique integer value identifying this redis export storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisExportStorage


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.redis.get(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RedisExportStorage,
                    parse_obj_as(
                        type_=RedisExportStorage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """

        Delete a specific Redis export storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        Deleting an export/target storage connection does not affect tasks with synced data in Label Studio. If you want to remove the tasks that were synced from the external storage, you will need to delete them manually from within the Label Studio UI or use the [Delete tasks](../../tasks/delete-all-tasks) API.

        Parameters
        ----------
        id : int
            A unique integer value identifying this redis export storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.redis.delete(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: int,
        *,
        db: typing.Optional[int] = OMIT,
        can_delete_objects: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        path: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        port: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RedisUpdateResponse:
        """

        Update a specific Redis export storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        For more information about working with external storage, see [Sync data from external storage](https://labelstud.io/guide/storage).

        Parameters
        ----------
        id : int
            A unique integer value identifying this redis export storage.

        db : typing.Optional[int]
            Database ID of database to use

        can_delete_objects : typing.Optional[bool]
            Deletion from storage enabled.

        title : typing.Optional[str]
            Storage title

        description : typing.Optional[str]
            Storage description

        project : typing.Optional[int]
            Project ID

        path : typing.Optional[str]
            Storage prefix (optional)

        host : typing.Optional[str]
            Server Host IP (optional)

        port : typing.Optional[str]
            Server Port (optional)

        password : typing.Optional[str]
            Server Password (optional)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisUpdateResponse


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.redis.update(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "db": db,
                "can_delete_objects": can_delete_objects,
                "title": title,
                "description": description,
                "project": project,
                "path": path,
                "host": host,
                "port": port,
                "password": password,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RedisUpdateResponse,
                    parse_obj_as(
                        type_=RedisUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def sync(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> RedisExportStorage:
        """

        Sync tasks to an Redis export/target storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        Sync operations with external databases only go one way. They either create tasks from objects in the database (source/import storage) or push annotations to the output database (export/target storage). Changing something on the database side doesn’t guarantee consistency in results.

        <Note>Before proceeding, you should review [How sync operations work - Source storage](https://labelstud.io/guide/storage#Source-storage) to ensure that your data remains secure and private.</Note>

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisExportStorage


        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.redis.sync(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}/sync",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RedisExportStorage,
                    parse_obj_as(
                        type_=RedisExportStorage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRedisClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RedisExportStorage]:
        """

        You can connect your Redis database to Label Studio as a source storage or target storage. Use this API request to get a list of all Redis export (target) storage connections for a specific project.

        The project ID can be found in the URL when viewing the project in Label Studio, or you can retrieve all project IDs using [List all projects](../projects/list).

        For more information about working with external storage, see [Sync data from external storage](https://labelstud.io/guide/storage).

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RedisExportStorage]


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.export_storage.redis.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/export/redis",
            method="GET",
            params={
                "project": project,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[RedisExportStorage],
                    parse_obj_as(
                        type_=typing.List[RedisExportStorage],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        db: typing.Optional[int] = OMIT,
        can_delete_objects: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        path: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        port: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RedisCreateResponse:
        """

        Create a new target storage connection to Redis.

        For information about the required fields and prerequisites, see [Redis database](https://labelstud.io/guide/storage#Redis-database) in the Label Studio documentation.

        <Tip>After you add the storage, you should validate the connection before attempting to sync your data. Your data will not be exported until you [sync your connection](sync).</Tip>

        Parameters
        ----------
        db : typing.Optional[int]
            Database ID of database to use

        can_delete_objects : typing.Optional[bool]
            Deletion from storage enabled.

        title : typing.Optional[str]
            Storage title

        description : typing.Optional[str]
            Storage description

        project : typing.Optional[int]
            Project ID

        path : typing.Optional[str]
            Storage prefix (optional)

        host : typing.Optional[str]
            Server Host IP (optional)

        port : typing.Optional[str]
            Server Port (optional)

        password : typing.Optional[str]
            Server Password (optional)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisCreateResponse


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.export_storage.redis.create()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/export/redis",
            method="POST",
            json={
                "db": db,
                "can_delete_objects": can_delete_objects,
                "title": title,
                "description": description,
                "project": project,
                "path": path,
                "host": host,
                "port": port,
                "password": password,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RedisCreateResponse,
                    parse_obj_as(
                        type_=RedisCreateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def validate(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        db: typing.Optional[int] = OMIT,
        can_delete_objects: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        path: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        port: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """

        Validate a specific Redis export storage connection. This is useful to ensure that the storage configuration settings are correct and operational before attempting to export data.

        Parameters
        ----------
        id : typing.Optional[int]
            Storage ID. If set, storage with specified ID will be updated

        db : typing.Optional[int]
            Database ID of database to use

        can_delete_objects : typing.Optional[bool]
            Deletion from storage enabled.

        title : typing.Optional[str]
            Storage title

        description : typing.Optional[str]
            Storage description

        project : typing.Optional[int]
            Project ID

        path : typing.Optional[str]
            Storage prefix (optional)

        host : typing.Optional[str]
            Server Host IP (optional)

        port : typing.Optional[str]
            Server Port (optional)

        password : typing.Optional[str]
            Server Password (optional)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.export_storage.redis.validate()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/export/redis/validate",
            method="POST",
            json={
                "id": id,
                "db": db,
                "can_delete_objects": can_delete_objects,
                "title": title,
                "description": description,
                "project": project,
                "path": path,
                "host": host,
                "port": port,
                "password": password,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> RedisExportStorage:
        """

        Get a specific Redis export storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        For more information about working with external storage, see [Sync data from external storage](https://labelstud.io/guide/storage).

        Parameters
        ----------
        id : int
            A unique integer value identifying this redis export storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisExportStorage


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.export_storage.redis.get(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RedisExportStorage,
                    parse_obj_as(
                        type_=RedisExportStorage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """

        Delete a specific Redis export storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        Deleting an export/target storage connection does not affect tasks with synced data in Label Studio. If you want to remove the tasks that were synced from the external storage, you will need to delete them manually from within the Label Studio UI or use the [Delete tasks](../../tasks/delete-all-tasks) API.

        Parameters
        ----------
        id : int
            A unique integer value identifying this redis export storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.export_storage.redis.delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        id: int,
        *,
        db: typing.Optional[int] = OMIT,
        can_delete_objects: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        path: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        port: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RedisUpdateResponse:
        """

        Update a specific Redis export storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        For more information about working with external storage, see [Sync data from external storage](https://labelstud.io/guide/storage).

        Parameters
        ----------
        id : int
            A unique integer value identifying this redis export storage.

        db : typing.Optional[int]
            Database ID of database to use

        can_delete_objects : typing.Optional[bool]
            Deletion from storage enabled.

        title : typing.Optional[str]
            Storage title

        description : typing.Optional[str]
            Storage description

        project : typing.Optional[int]
            Project ID

        path : typing.Optional[str]
            Storage prefix (optional)

        host : typing.Optional[str]
            Server Host IP (optional)

        port : typing.Optional[str]
            Server Port (optional)

        password : typing.Optional[str]
            Server Password (optional)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisUpdateResponse


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.export_storage.redis.update(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "db": db,
                "can_delete_objects": can_delete_objects,
                "title": title,
                "description": description,
                "project": project,
                "path": path,
                "host": host,
                "port": port,
                "password": password,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RedisUpdateResponse,
                    parse_obj_as(
                        type_=RedisUpdateResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def sync(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> RedisExportStorage:
        """

        Sync tasks to an Redis export/target storage connection. You will need to provide the export storage ID. You can find this using [List export storages](list).

        Sync operations with external databases only go one way. They either create tasks from objects in the database (source/import storage) or push annotations to the output database (export/target storage). Changing something on the database side doesn’t guarantee consistency in results.

        <Note>Before proceeding, you should review [How sync operations work - Source storage](https://labelstud.io/guide/storage#Source-storage) to ensure that your data remains secure and private.</Note>

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisExportStorage


        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.export_storage.redis.sync(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}/sync",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    RedisExportStorage,
                    parse_obj_as(
                        type_=RedisExportStorage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
