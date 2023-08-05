# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetUserResult',
    'AwaitableGetUserResult',
    'get_user',
    'get_user_output',
]

@pulumi.output_type
class GetUserResult:
    """
    A collection of values returned by getUser.
    """
    def __init__(__self__, alphanumeric=None, application_id=None, display_name=None, external_id=None, home=None, id=None, repos=None, user_id=None, user_name=None):
        if alphanumeric and not isinstance(alphanumeric, str):
            raise TypeError("Expected argument 'alphanumeric' to be a str")
        pulumi.set(__self__, "alphanumeric", alphanumeric)
        if application_id and not isinstance(application_id, str):
            raise TypeError("Expected argument 'application_id' to be a str")
        pulumi.set(__self__, "application_id", application_id)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if external_id and not isinstance(external_id, str):
            raise TypeError("Expected argument 'external_id' to be a str")
        pulumi.set(__self__, "external_id", external_id)
        if home and not isinstance(home, str):
            raise TypeError("Expected argument 'home' to be a str")
        pulumi.set(__self__, "home", home)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if repos and not isinstance(repos, str):
            raise TypeError("Expected argument 'repos' to be a str")
        pulumi.set(__self__, "repos", repos)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter
    def alphanumeric(self) -> str:
        """
        Alphanumeric representation of user local name. e.g. `mr_foo`.
        """
        return pulumi.get(self, "alphanumeric")

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> str:
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display name of the user, e.g. `Mr Foo`.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> str:
        """
        ID of the user in an external identity provider.
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter
    def home(self) -> str:
        """
        Home folder of the user, e.g. `/Users/mr.foo@example.com`.
        """
        return pulumi.get(self, "home")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def repos(self) -> str:
        """
        Personal Repos location of the user, e.g. `/Repos/mr.foo@example.com`.
        """
        return pulumi.get(self, "repos")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[str]:
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[str]:
        """
        Name of the user, e.g. `mr.foo@example.com`.
        """
        return pulumi.get(self, "user_name")


class AwaitableGetUserResult(GetUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserResult(
            alphanumeric=self.alphanumeric,
            application_id=self.application_id,
            display_name=self.display_name,
            external_id=self.external_id,
            home=self.home,
            id=self.id,
            repos=self.repos,
            user_id=self.user_id,
            user_name=self.user_name)


def get_user(user_id: Optional[str] = None,
             user_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserResult:
    """
    ## Related Resources

    The following resources are used in the same context:

    * End to end workspace management guide
    * get_current_user data to retrieve information about User or databricks_service_principal, that is calling Databricks REST API.
    * Group to manage [groups in Databricks Workspace](https://docs.databricks.com/administration-guide/users-groups/groups.html) or [Account Console](https://accounts.cloud.databricks.com/) (for AWS deployments).
    * Group data to retrieve information about Group members, entitlements and instance profiles.
    * GroupInstanceProfile to attach InstanceProfile (AWS) to databricks_group.
    * databricks_group_member to attach users and groups as group members.
    * Permissions to manage [access control](https://docs.databricks.com/security/access-control/index.html) in Databricks workspace.
    * User to [manage users](https://docs.databricks.com/administration-guide/users-groups/users.html), that could be added to Group within the workspace.
    * UserInstanceProfile to attach InstanceProfile (AWS) to databricks_user.


    :param str user_id: ID of the user.
    :param str user_name: User name of the user. The user must exist before this resource can be planned.
    """
    __args__ = dict()
    __args__['userId'] = user_id
    __args__['userName'] = user_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('databricks:index/getUser:getUser', __args__, opts=opts, typ=GetUserResult).value

    return AwaitableGetUserResult(
        alphanumeric=__ret__.alphanumeric,
        application_id=__ret__.application_id,
        display_name=__ret__.display_name,
        external_id=__ret__.external_id,
        home=__ret__.home,
        id=__ret__.id,
        repos=__ret__.repos,
        user_id=__ret__.user_id,
        user_name=__ret__.user_name)


@_utilities.lift_output_func(get_user)
def get_user_output(user_id: Optional[pulumi.Input[Optional[str]]] = None,
                    user_name: Optional[pulumi.Input[Optional[str]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserResult]:
    """
    ## Related Resources

    The following resources are used in the same context:

    * End to end workspace management guide
    * get_current_user data to retrieve information about User or databricks_service_principal, that is calling Databricks REST API.
    * Group to manage [groups in Databricks Workspace](https://docs.databricks.com/administration-guide/users-groups/groups.html) or [Account Console](https://accounts.cloud.databricks.com/) (for AWS deployments).
    * Group data to retrieve information about Group members, entitlements and instance profiles.
    * GroupInstanceProfile to attach InstanceProfile (AWS) to databricks_group.
    * databricks_group_member to attach users and groups as group members.
    * Permissions to manage [access control](https://docs.databricks.com/security/access-control/index.html) in Databricks workspace.
    * User to [manage users](https://docs.databricks.com/administration-guide/users-groups/users.html), that could be added to Group within the workspace.
    * UserInstanceProfile to attach InstanceProfile (AWS) to databricks_user.


    :param str user_id: ID of the user.
    :param str user_name: User name of the user. The user must exist before this resource can be planned.
    """
    ...
