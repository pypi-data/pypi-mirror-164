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
    'GetTablesResult',
    'AwaitableGetTablesResult',
    'get_tables',
    'get_tables_output',
]

@pulumi.output_type
class GetTablesResult:
    """
    A collection of values returned by getTables.
    """
    def __init__(__self__, catalog_name=None, id=None, ids=None, schema_name=None):
        if catalog_name and not isinstance(catalog_name, str):
            raise TypeError("Expected argument 'catalog_name' to be a str")
        pulumi.set(__self__, "catalog_name", catalog_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if schema_name and not isinstance(schema_name, str):
            raise TypeError("Expected argument 'schema_name' to be a str")
        pulumi.set(__self__, "schema_name", schema_name)

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> str:
        return pulumi.get(self, "catalog_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        set of Table full names: *`catalog`.`schema`.`table`*
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> str:
        return pulumi.get(self, "schema_name")


class AwaitableGetTablesResult(GetTablesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTablesResult(
            catalog_name=self.catalog_name,
            id=self.id,
            ids=self.ids,
            schema_name=self.schema_name)


def get_tables(catalog_name: Optional[str] = None,
               ids: Optional[Sequence[str]] = None,
               schema_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTablesResult:
    """
    ## Related Resources

    The following resources are used in the same context:

    * Table to manage tables within Unity Catalog.
    * Schema to manage schemas within Unity Catalog.
    * Catalog to manage catalogs within Unity Catalog.


    :param str catalog_name: Name of databricks_catalog
    :param Sequence[str] ids: set of Table full names: *`catalog`.`schema`.`table`*
    :param str schema_name: Name of databricks_schema
    """
    __args__ = dict()
    __args__['catalogName'] = catalog_name
    __args__['ids'] = ids
    __args__['schemaName'] = schema_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('databricks:index/getTables:getTables', __args__, opts=opts, typ=GetTablesResult).value

    return AwaitableGetTablesResult(
        catalog_name=__ret__.catalog_name,
        id=__ret__.id,
        ids=__ret__.ids,
        schema_name=__ret__.schema_name)


@_utilities.lift_output_func(get_tables)
def get_tables_output(catalog_name: Optional[pulumi.Input[str]] = None,
                      ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                      schema_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTablesResult]:
    """
    ## Related Resources

    The following resources are used in the same context:

    * Table to manage tables within Unity Catalog.
    * Schema to manage schemas within Unity Catalog.
    * Catalog to manage catalogs within Unity Catalog.


    :param str catalog_name: Name of databricks_catalog
    :param Sequence[str] ids: set of Table full names: *`catalog`.`schema`.`table`*
    :param str schema_name: Name of databricks_schema
    """
    ...
