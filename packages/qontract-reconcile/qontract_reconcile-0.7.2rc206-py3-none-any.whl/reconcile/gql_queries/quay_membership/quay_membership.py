"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from pathlib import Path  # noqa: F401 # pylint: disable=W0611
from typing import Optional, Union  # noqa: F401 # pylint: disable=W0611

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)


def query_string() -> str:
    with open(f"{Path(__file__).parent}/quay_membership.gql", "r") as f:
        return f.read()


class PermissionV1(BaseModel):
    service: str = Field(..., alias="service")

    class Config:
        smart_union = True
        extra = Extra.forbid


class QuayInstanceV1(BaseModel):
    name: str = Field(..., alias="name")

    class Config:
        smart_union = True
        extra = Extra.forbid


class QuayOrgV1(BaseModel):
    name: str = Field(..., alias="name")
    instance: QuayInstanceV1 = Field(..., alias="instance")

    class Config:
        smart_union = True
        extra = Extra.forbid


class UserV1(BaseModel):
    quay_username: Optional[str] = Field(..., alias="quay_username")

    class Config:
        smart_union = True
        extra = Extra.forbid


class BotV1(BaseModel):
    quay_username: Optional[str] = Field(..., alias="quay_username")

    class Config:
        smart_union = True
        extra = Extra.forbid


class RoleV1(BaseModel):
    users: Optional[list[Optional[UserV1]]] = Field(..., alias="users")
    bots: Optional[list[Optional[BotV1]]] = Field(..., alias="bots")
    expiration_date: Optional[str] = Field(..., alias="expirationDate")

    class Config:
        smart_union = True
        extra = Extra.forbid


class PermissionQuayOrgTeamV1(PermissionV1):
    quay_org: QuayOrgV1 = Field(..., alias="quayOrg")
    team: str = Field(..., alias="team")
    roles: Optional[list[Optional[RoleV1]]] = Field(..., alias="roles")

    class Config:
        smart_union = True
        extra = Extra.forbid


class QuayMembershipQueryData(BaseModel):
    permissions: Optional[
        list[Optional[Union[PermissionQuayOrgTeamV1, PermissionV1]]]
    ] = Field(..., alias="permissions")

    class Config:
        smart_union = True
        extra = Extra.forbid
