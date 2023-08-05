# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('databricks')


class _ExportableConfig(types.ModuleType):
    @property
    def account_id(self) -> Optional[str]:
        return __config__.get('accountId')

    @property
    def auth_type(self) -> Optional[str]:
        return __config__.get('authType')

    @property
    def azure_client_id(self) -> Optional[str]:
        return __config__.get('azureClientId')

    @property
    def azure_client_secret(self) -> Optional[str]:
        return __config__.get('azureClientSecret')

    @property
    def azure_environment(self) -> Optional[str]:
        return __config__.get('azureEnvironment')

    @property
    def azure_tenant_id(self) -> Optional[str]:
        return __config__.get('azureTenantId')

    @property
    def azure_use_msi(self) -> Optional[bool]:
        return __config__.get_bool('azureUseMsi')

    @property
    def azure_workspace_resource_id(self) -> Optional[str]:
        return __config__.get('azureWorkspaceResourceId')

    @property
    def config_file(self) -> Optional[str]:
        return __config__.get('configFile')

    @property
    def debug_headers(self) -> Optional[bool]:
        return __config__.get_bool('debugHeaders')

    @property
    def debug_truncate_bytes(self) -> Optional[int]:
        return __config__.get_int('debugTruncateBytes')

    @property
    def google_credentials(self) -> Optional[str]:
        return __config__.get('googleCredentials')

    @property
    def google_service_account(self) -> Optional[str]:
        return __config__.get('googleServiceAccount')

    @property
    def host(self) -> Optional[str]:
        return __config__.get('host')

    @property
    def http_timeout_seconds(self) -> Optional[int]:
        return __config__.get_int('httpTimeoutSeconds')

    @property
    def password(self) -> Optional[str]:
        return __config__.get('password')

    @property
    def profile(self) -> Optional[str]:
        return __config__.get('profile')

    @property
    def rate_limit(self) -> Optional[int]:
        return __config__.get_int('rateLimit')

    @property
    def skip_verify(self) -> Optional[bool]:
        return __config__.get_bool('skipVerify')

    @property
    def token(self) -> Optional[str]:
        return __config__.get('token')

    @property
    def username(self) -> Optional[str]:
        return __config__.get('username')

