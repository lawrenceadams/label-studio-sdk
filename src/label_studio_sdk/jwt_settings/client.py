# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.jwt_settings_response import JwtSettingsResponse
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class JwtSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> JwtSettingsResponse:
        """
        Retrieve JWT settings for the currently-active organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JwtSettingsResponse
            JWT settings retrieved successfully

        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.jwt_settings.get()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/jwt/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    JwtSettingsResponse,
                    parse_obj_as(
                        type_=JwtSettingsResponse,  # type: ignore
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
        api_tokens_enabled: bool,
        legacy_api_tokens_enabled: bool,
        api_token_ttl_days: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JwtSettingsResponse:
        """
        Update JWT settings for the currently active organization.

        Parameters
        ----------
        api_tokens_enabled : bool
            Whether JWT API tokens are enabled

        legacy_api_tokens_enabled : bool
            Whether legacy API tokens are enabled

        api_token_ttl_days : int
            Number of days before API tokens expire

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JwtSettingsResponse
            JWT settings updated successfully

        Examples
        --------
        from label_studio_sdk import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.jwt_settings.create(
            api_tokens_enabled=True,
            legacy_api_tokens_enabled=True,
            api_token_ttl_days=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/jwt/settings",
            method="POST",
            json={
                "api_tokens_enabled": api_tokens_enabled,
                "legacy_api_tokens_enabled": legacy_api_tokens_enabled,
                "api_token_ttl_days": api_token_ttl_days,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    JwtSettingsResponse,
                    parse_obj_as(
                        type_=JwtSettingsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncJwtSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> JwtSettingsResponse:
        """
        Retrieve JWT settings for the currently-active organization.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JwtSettingsResponse
            JWT settings retrieved successfully

        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.jwt_settings.get()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/jwt/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    JwtSettingsResponse,
                    parse_obj_as(
                        type_=JwtSettingsResponse,  # type: ignore
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
        api_tokens_enabled: bool,
        legacy_api_tokens_enabled: bool,
        api_token_ttl_days: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JwtSettingsResponse:
        """
        Update JWT settings for the currently active organization.

        Parameters
        ----------
        api_tokens_enabled : bool
            Whether JWT API tokens are enabled

        legacy_api_tokens_enabled : bool
            Whether legacy API tokens are enabled

        api_token_ttl_days : int
            Number of days before API tokens expire

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JwtSettingsResponse
            JWT settings updated successfully

        Examples
        --------
        import asyncio

        from label_studio_sdk import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.jwt_settings.create(
                api_tokens_enabled=True,
                legacy_api_tokens_enabled=True,
                api_token_ttl_days=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/jwt/settings",
            method="POST",
            json={
                "api_tokens_enabled": api_tokens_enabled,
                "legacy_api_tokens_enabled": legacy_api_tokens_enabled,
                "api_token_ttl_days": api_token_ttl_days,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    JwtSettingsResponse,
                    parse_obj_as(
                        type_=JwtSettingsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
