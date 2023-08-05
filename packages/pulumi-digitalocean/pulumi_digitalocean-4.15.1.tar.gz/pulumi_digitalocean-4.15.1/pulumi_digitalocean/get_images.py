# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetImagesResult',
    'AwaitableGetImagesResult',
    'get_images',
    'get_images_output',
]

@pulumi.output_type
class GetImagesResult:
    """
    A collection of values returned by getImages.
    """
    def __init__(__self__, filters=None, id=None, images=None, sorts=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if images and not isinstance(images, list):
            raise TypeError("Expected argument 'images' to be a list")
        pulumi.set(__self__, "images", images)
        if sorts and not isinstance(sorts, list):
            raise TypeError("Expected argument 'sorts' to be a list")
        pulumi.set(__self__, "sorts", sorts)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetImagesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def images(self) -> Sequence['outputs.GetImagesImageResult']:
        """
        A set of images satisfying any `filter` and `sort` criteria. Each image has the following attributes:  
        - `slug`: Unique text identifier of the image.
        - `id`: The ID of the image.
        - `name`: The name of the image.
        - `type`: Type of the image.
        """
        return pulumi.get(self, "images")

    @property
    @pulumi.getter
    def sorts(self) -> Optional[Sequence['outputs.GetImagesSortResult']]:
        return pulumi.get(self, "sorts")


class AwaitableGetImagesResult(GetImagesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImagesResult(
            filters=self.filters,
            id=self.id,
            images=self.images,
            sorts=self.sorts)


def get_images(filters: Optional[Sequence[pulumi.InputType['GetImagesFilterArgs']]] = None,
               sorts: Optional[Sequence[pulumi.InputType['GetImagesSortArgs']]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImagesResult:
    """
    Get information on images for use in other resources (e.g. creating a Droplet
    based on a snapshot), with the ability to filter and sort the results. If no filters are specified,
    all images will be returned.

    This data source is useful if the image in question is not managed by the provider or you need to utilize any
    of the image's data.

    Note: You can use the `get_image` data source to obtain metadata
    about a single image if you already know the `slug`, unique `name`, or `id` to retrieve.

    ## Example Usage

    Use the `filter` block with a `key` string and `values` list to filter images.

    For example to find all Ubuntu images:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    ubuntu = digitalocean.get_images(filters=[digitalocean.GetImagesFilterArgs(
        key="distribution",
        values=["Ubuntu"],
    )])
    ```

    You can filter on multiple fields and sort the results as well:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    available = digitalocean.get_images(filters=[
            digitalocean.GetImagesFilterArgs(
                key="distribution",
                values=["Ubuntu"],
            ),
            digitalocean.GetImagesFilterArgs(
                key="regions",
                values=["nyc3"],
            ),
        ],
        sorts=[digitalocean.GetImagesSortArgs(
            direction="desc",
            key="created",
        )])
    ```


    :param Sequence[pulumi.InputType['GetImagesFilterArgs']] filters: Filter the results.
           The `filter` block is documented below.
    :param Sequence[pulumi.InputType['GetImagesSortArgs']] sorts: Sort the results.
           The `sort` block is documented below.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['sorts'] = sorts
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getImages:getImages', __args__, opts=opts, typ=GetImagesResult).value

    return AwaitableGetImagesResult(
        filters=__ret__.filters,
        id=__ret__.id,
        images=__ret__.images,
        sorts=__ret__.sorts)


@_utilities.lift_output_func(get_images)
def get_images_output(filters: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetImagesFilterArgs']]]]] = None,
                      sorts: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetImagesSortArgs']]]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetImagesResult]:
    """
    Get information on images for use in other resources (e.g. creating a Droplet
    based on a snapshot), with the ability to filter and sort the results. If no filters are specified,
    all images will be returned.

    This data source is useful if the image in question is not managed by the provider or you need to utilize any
    of the image's data.

    Note: You can use the `get_image` data source to obtain metadata
    about a single image if you already know the `slug`, unique `name`, or `id` to retrieve.

    ## Example Usage

    Use the `filter` block with a `key` string and `values` list to filter images.

    For example to find all Ubuntu images:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    ubuntu = digitalocean.get_images(filters=[digitalocean.GetImagesFilterArgs(
        key="distribution",
        values=["Ubuntu"],
    )])
    ```

    You can filter on multiple fields and sort the results as well:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    available = digitalocean.get_images(filters=[
            digitalocean.GetImagesFilterArgs(
                key="distribution",
                values=["Ubuntu"],
            ),
            digitalocean.GetImagesFilterArgs(
                key="regions",
                values=["nyc3"],
            ),
        ],
        sorts=[digitalocean.GetImagesSortArgs(
            direction="desc",
            key="created",
        )])
    ```


    :param Sequence[pulumi.InputType['GetImagesFilterArgs']] filters: Filter the results.
           The `filter` block is documented below.
    :param Sequence[pulumi.InputType['GetImagesSortArgs']] sorts: Sort the results.
           The `sort` block is documented below.
    """
    ...
