# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Workspace(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unique ID of the workspace
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Workspace title
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Workspace description
    """

    is_public: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the workspace is public or not
    """

    is_personal: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the workspace is personal or not
    """

    is_archived: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the workspace is archived or not
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Creation time of the workspace
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Last updated time of the workspace
    """

    created_by: typing.Optional[int] = pydantic.Field(default=None)
    """
    User ID of the workspace creator
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Workspace color
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
