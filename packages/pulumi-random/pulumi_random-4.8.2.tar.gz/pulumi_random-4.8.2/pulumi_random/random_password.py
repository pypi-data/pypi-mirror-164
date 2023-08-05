# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['RandomPasswordArgs', 'RandomPassword']

@pulumi.input_type
class RandomPasswordArgs:
    def __init__(__self__, *,
                 length: pulumi.Input[int],
                 keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 lower: Optional[pulumi.Input[bool]] = None,
                 min_lower: Optional[pulumi.Input[int]] = None,
                 min_numeric: Optional[pulumi.Input[int]] = None,
                 min_special: Optional[pulumi.Input[int]] = None,
                 min_upper: Optional[pulumi.Input[int]] = None,
                 number: Optional[pulumi.Input[bool]] = None,
                 override_special: Optional[pulumi.Input[str]] = None,
                 special: Optional[pulumi.Input[bool]] = None,
                 upper: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a RandomPassword resource.
        :param pulumi.Input[int] length: The length of the string desired.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
               documentation](../index.html) for more information.
        :param pulumi.Input[bool] lower: Include lowercase alphabet characters in the result.
        :param pulumi.Input[int] min_lower: Minimum number of lowercase alphabet characters in the result.
        :param pulumi.Input[int] min_numeric: Minimum number of numeric characters in the result.
        :param pulumi.Input[int] min_special: Minimum number of special characters in the result.
        :param pulumi.Input[int] min_upper: Minimum number of uppercase alphabet characters in the result.
        :param pulumi.Input[bool] number: Include numeric characters in the result.
        :param pulumi.Input[str] override_special: Supply your own list of special characters to use for string generation. This overrides the default character list in
               the special argument. The `special` argument must still be set to true for any overwritten characters to be used in
               generation.
        :param pulumi.Input[bool] special: Include special characters in the result. These are `!@#$%&*()-_=+[]{}<>:?`
        :param pulumi.Input[bool] upper: Include uppercase alphabet characters in the result.
        """
        pulumi.set(__self__, "length", length)
        if keepers is not None:
            pulumi.set(__self__, "keepers", keepers)
        if lower is not None:
            pulumi.set(__self__, "lower", lower)
        if min_lower is not None:
            pulumi.set(__self__, "min_lower", min_lower)
        if min_numeric is not None:
            pulumi.set(__self__, "min_numeric", min_numeric)
        if min_special is not None:
            pulumi.set(__self__, "min_special", min_special)
        if min_upper is not None:
            pulumi.set(__self__, "min_upper", min_upper)
        if number is not None:
            pulumi.set(__self__, "number", number)
        if override_special is not None:
            pulumi.set(__self__, "override_special", override_special)
        if special is not None:
            pulumi.set(__self__, "special", special)
        if upper is not None:
            pulumi.set(__self__, "upper", upper)

    @property
    @pulumi.getter
    def length(self) -> pulumi.Input[int]:
        """
        The length of the string desired.
        """
        return pulumi.get(self, "length")

    @length.setter
    def length(self, value: pulumi.Input[int]):
        pulumi.set(self, "length", value)

    @property
    @pulumi.getter
    def keepers(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
        documentation](../index.html) for more information.
        """
        return pulumi.get(self, "keepers")

    @keepers.setter
    def keepers(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "keepers", value)

    @property
    @pulumi.getter
    def lower(self) -> Optional[pulumi.Input[bool]]:
        """
        Include lowercase alphabet characters in the result.
        """
        return pulumi.get(self, "lower")

    @lower.setter
    def lower(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "lower", value)

    @property
    @pulumi.getter(name="minLower")
    def min_lower(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum number of lowercase alphabet characters in the result.
        """
        return pulumi.get(self, "min_lower")

    @min_lower.setter
    def min_lower(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_lower", value)

    @property
    @pulumi.getter(name="minNumeric")
    def min_numeric(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum number of numeric characters in the result.
        """
        return pulumi.get(self, "min_numeric")

    @min_numeric.setter
    def min_numeric(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_numeric", value)

    @property
    @pulumi.getter(name="minSpecial")
    def min_special(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum number of special characters in the result.
        """
        return pulumi.get(self, "min_special")

    @min_special.setter
    def min_special(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_special", value)

    @property
    @pulumi.getter(name="minUpper")
    def min_upper(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum number of uppercase alphabet characters in the result.
        """
        return pulumi.get(self, "min_upper")

    @min_upper.setter
    def min_upper(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_upper", value)

    @property
    @pulumi.getter
    def number(self) -> Optional[pulumi.Input[bool]]:
        """
        Include numeric characters in the result.
        """
        return pulumi.get(self, "number")

    @number.setter
    def number(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "number", value)

    @property
    @pulumi.getter(name="overrideSpecial")
    def override_special(self) -> Optional[pulumi.Input[str]]:
        """
        Supply your own list of special characters to use for string generation. This overrides the default character list in
        the special argument. The `special` argument must still be set to true for any overwritten characters to be used in
        generation.
        """
        return pulumi.get(self, "override_special")

    @override_special.setter
    def override_special(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "override_special", value)

    @property
    @pulumi.getter
    def special(self) -> Optional[pulumi.Input[bool]]:
        """
        Include special characters in the result. These are `!@#$%&*()-_=+[]{}<>:?`
        """
        return pulumi.get(self, "special")

    @special.setter
    def special(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "special", value)

    @property
    @pulumi.getter
    def upper(self) -> Optional[pulumi.Input[bool]]:
        """
        Include uppercase alphabet characters in the result.
        """
        return pulumi.get(self, "upper")

    @upper.setter
    def upper(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "upper", value)


@pulumi.input_type
class _RandomPasswordState:
    def __init__(__self__, *,
                 keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 length: Optional[pulumi.Input[int]] = None,
                 lower: Optional[pulumi.Input[bool]] = None,
                 min_lower: Optional[pulumi.Input[int]] = None,
                 min_numeric: Optional[pulumi.Input[int]] = None,
                 min_special: Optional[pulumi.Input[int]] = None,
                 min_upper: Optional[pulumi.Input[int]] = None,
                 number: Optional[pulumi.Input[bool]] = None,
                 override_special: Optional[pulumi.Input[str]] = None,
                 result: Optional[pulumi.Input[str]] = None,
                 special: Optional[pulumi.Input[bool]] = None,
                 upper: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering RandomPassword resources.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
               documentation](../index.html) for more information.
        :param pulumi.Input[int] length: The length of the string desired.
        :param pulumi.Input[bool] lower: Include lowercase alphabet characters in the result.
        :param pulumi.Input[int] min_lower: Minimum number of lowercase alphabet characters in the result.
        :param pulumi.Input[int] min_numeric: Minimum number of numeric characters in the result.
        :param pulumi.Input[int] min_special: Minimum number of special characters in the result.
        :param pulumi.Input[int] min_upper: Minimum number of uppercase alphabet characters in the result.
        :param pulumi.Input[bool] number: Include numeric characters in the result.
        :param pulumi.Input[str] override_special: Supply your own list of special characters to use for string generation. This overrides the default character list in
               the special argument. The `special` argument must still be set to true for any overwritten characters to be used in
               generation.
        :param pulumi.Input[str] result: The generated random string.
        :param pulumi.Input[bool] special: Include special characters in the result. These are `!@#$%&*()-_=+[]{}<>:?`
        :param pulumi.Input[bool] upper: Include uppercase alphabet characters in the result.
        """
        if keepers is not None:
            pulumi.set(__self__, "keepers", keepers)
        if length is not None:
            pulumi.set(__self__, "length", length)
        if lower is not None:
            pulumi.set(__self__, "lower", lower)
        if min_lower is not None:
            pulumi.set(__self__, "min_lower", min_lower)
        if min_numeric is not None:
            pulumi.set(__self__, "min_numeric", min_numeric)
        if min_special is not None:
            pulumi.set(__self__, "min_special", min_special)
        if min_upper is not None:
            pulumi.set(__self__, "min_upper", min_upper)
        if number is not None:
            pulumi.set(__self__, "number", number)
        if override_special is not None:
            pulumi.set(__self__, "override_special", override_special)
        if result is not None:
            pulumi.set(__self__, "result", result)
        if special is not None:
            pulumi.set(__self__, "special", special)
        if upper is not None:
            pulumi.set(__self__, "upper", upper)

    @property
    @pulumi.getter
    def keepers(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
        documentation](../index.html) for more information.
        """
        return pulumi.get(self, "keepers")

    @keepers.setter
    def keepers(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "keepers", value)

    @property
    @pulumi.getter
    def length(self) -> Optional[pulumi.Input[int]]:
        """
        The length of the string desired.
        """
        return pulumi.get(self, "length")

    @length.setter
    def length(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "length", value)

    @property
    @pulumi.getter
    def lower(self) -> Optional[pulumi.Input[bool]]:
        """
        Include lowercase alphabet characters in the result.
        """
        return pulumi.get(self, "lower")

    @lower.setter
    def lower(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "lower", value)

    @property
    @pulumi.getter(name="minLower")
    def min_lower(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum number of lowercase alphabet characters in the result.
        """
        return pulumi.get(self, "min_lower")

    @min_lower.setter
    def min_lower(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_lower", value)

    @property
    @pulumi.getter(name="minNumeric")
    def min_numeric(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum number of numeric characters in the result.
        """
        return pulumi.get(self, "min_numeric")

    @min_numeric.setter
    def min_numeric(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_numeric", value)

    @property
    @pulumi.getter(name="minSpecial")
    def min_special(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum number of special characters in the result.
        """
        return pulumi.get(self, "min_special")

    @min_special.setter
    def min_special(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_special", value)

    @property
    @pulumi.getter(name="minUpper")
    def min_upper(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum number of uppercase alphabet characters in the result.
        """
        return pulumi.get(self, "min_upper")

    @min_upper.setter
    def min_upper(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_upper", value)

    @property
    @pulumi.getter
    def number(self) -> Optional[pulumi.Input[bool]]:
        """
        Include numeric characters in the result.
        """
        return pulumi.get(self, "number")

    @number.setter
    def number(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "number", value)

    @property
    @pulumi.getter(name="overrideSpecial")
    def override_special(self) -> Optional[pulumi.Input[str]]:
        """
        Supply your own list of special characters to use for string generation. This overrides the default character list in
        the special argument. The `special` argument must still be set to true for any overwritten characters to be used in
        generation.
        """
        return pulumi.get(self, "override_special")

    @override_special.setter
    def override_special(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "override_special", value)

    @property
    @pulumi.getter
    def result(self) -> Optional[pulumi.Input[str]]:
        """
        The generated random string.
        """
        return pulumi.get(self, "result")

    @result.setter
    def result(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "result", value)

    @property
    @pulumi.getter
    def special(self) -> Optional[pulumi.Input[bool]]:
        """
        Include special characters in the result. These are `!@#$%&*()-_=+[]{}<>:?`
        """
        return pulumi.get(self, "special")

    @special.setter
    def special(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "special", value)

    @property
    @pulumi.getter
    def upper(self) -> Optional[pulumi.Input[bool]]:
        """
        Include uppercase alphabet characters in the result.
        """
        return pulumi.get(self, "upper")

    @upper.setter
    def upper(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "upper", value)


class RandomPassword(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 length: Optional[pulumi.Input[int]] = None,
                 lower: Optional[pulumi.Input[bool]] = None,
                 min_lower: Optional[pulumi.Input[int]] = None,
                 min_numeric: Optional[pulumi.Input[int]] = None,
                 min_special: Optional[pulumi.Input[int]] = None,
                 min_upper: Optional[pulumi.Input[int]] = None,
                 number: Optional[pulumi.Input[bool]] = None,
                 override_special: Optional[pulumi.Input[str]] = None,
                 special: Optional[pulumi.Input[bool]] = None,
                 upper: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        > **Note:** Requires random provider version >= 2.2.0

        Identical to RandomString with the exception that the
        result is treated as sensitive and, thus, _not_ displayed in console output.

        > **Note:** All attributes including the generated password will be stored in
        the raw state as plain-text. [Read more about sensitive data in
        state](https://www.terraform.io/docs/state/sensitive-data.html).

        This resource *does* use a cryptographic random number generator.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_random as random

        password = random.RandomPassword("password",
            length=16,
            special=True,
            override_special="_%@")
        example = aws.rds.Instance("example",
            instance_class="db.t3.micro",
            allocated_storage=64,
            engine="mysql",
            username="someone",
            password=password.result)
        ```

        ## Import

        Random Password can be imported by specifying the value of the string

        ```sh
         $ pulumi import random:index/randomPassword:RandomPassword password securepassword
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
               documentation](../index.html) for more information.
        :param pulumi.Input[int] length: The length of the string desired.
        :param pulumi.Input[bool] lower: Include lowercase alphabet characters in the result.
        :param pulumi.Input[int] min_lower: Minimum number of lowercase alphabet characters in the result.
        :param pulumi.Input[int] min_numeric: Minimum number of numeric characters in the result.
        :param pulumi.Input[int] min_special: Minimum number of special characters in the result.
        :param pulumi.Input[int] min_upper: Minimum number of uppercase alphabet characters in the result.
        :param pulumi.Input[bool] number: Include numeric characters in the result.
        :param pulumi.Input[str] override_special: Supply your own list of special characters to use for string generation. This overrides the default character list in
               the special argument. The `special` argument must still be set to true for any overwritten characters to be used in
               generation.
        :param pulumi.Input[bool] special: Include special characters in the result. These are `!@#$%&*()-_=+[]{}<>:?`
        :param pulumi.Input[bool] upper: Include uppercase alphabet characters in the result.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RandomPasswordArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        > **Note:** Requires random provider version >= 2.2.0

        Identical to RandomString with the exception that the
        result is treated as sensitive and, thus, _not_ displayed in console output.

        > **Note:** All attributes including the generated password will be stored in
        the raw state as plain-text. [Read more about sensitive data in
        state](https://www.terraform.io/docs/state/sensitive-data.html).

        This resource *does* use a cryptographic random number generator.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_random as random

        password = random.RandomPassword("password",
            length=16,
            special=True,
            override_special="_%@")
        example = aws.rds.Instance("example",
            instance_class="db.t3.micro",
            allocated_storage=64,
            engine="mysql",
            username="someone",
            password=password.result)
        ```

        ## Import

        Random Password can be imported by specifying the value of the string

        ```sh
         $ pulumi import random:index/randomPassword:RandomPassword password securepassword
        ```

        :param str resource_name: The name of the resource.
        :param RandomPasswordArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RandomPasswordArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 length: Optional[pulumi.Input[int]] = None,
                 lower: Optional[pulumi.Input[bool]] = None,
                 min_lower: Optional[pulumi.Input[int]] = None,
                 min_numeric: Optional[pulumi.Input[int]] = None,
                 min_special: Optional[pulumi.Input[int]] = None,
                 min_upper: Optional[pulumi.Input[int]] = None,
                 number: Optional[pulumi.Input[bool]] = None,
                 override_special: Optional[pulumi.Input[str]] = None,
                 special: Optional[pulumi.Input[bool]] = None,
                 upper: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RandomPasswordArgs.__new__(RandomPasswordArgs)

            __props__.__dict__["keepers"] = keepers
            if length is None and not opts.urn:
                raise TypeError("Missing required property 'length'")
            __props__.__dict__["length"] = length
            __props__.__dict__["lower"] = lower
            __props__.__dict__["min_lower"] = min_lower
            __props__.__dict__["min_numeric"] = min_numeric
            __props__.__dict__["min_special"] = min_special
            __props__.__dict__["min_upper"] = min_upper
            __props__.__dict__["number"] = number
            __props__.__dict__["override_special"] = override_special
            __props__.__dict__["special"] = special
            __props__.__dict__["upper"] = upper
            __props__.__dict__["result"] = None
        super(RandomPassword, __self__).__init__(
            'random:index/randomPassword:RandomPassword',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            length: Optional[pulumi.Input[int]] = None,
            lower: Optional[pulumi.Input[bool]] = None,
            min_lower: Optional[pulumi.Input[int]] = None,
            min_numeric: Optional[pulumi.Input[int]] = None,
            min_special: Optional[pulumi.Input[int]] = None,
            min_upper: Optional[pulumi.Input[int]] = None,
            number: Optional[pulumi.Input[bool]] = None,
            override_special: Optional[pulumi.Input[str]] = None,
            result: Optional[pulumi.Input[str]] = None,
            special: Optional[pulumi.Input[bool]] = None,
            upper: Optional[pulumi.Input[bool]] = None) -> 'RandomPassword':
        """
        Get an existing RandomPassword resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
               documentation](../index.html) for more information.
        :param pulumi.Input[int] length: The length of the string desired.
        :param pulumi.Input[bool] lower: Include lowercase alphabet characters in the result.
        :param pulumi.Input[int] min_lower: Minimum number of lowercase alphabet characters in the result.
        :param pulumi.Input[int] min_numeric: Minimum number of numeric characters in the result.
        :param pulumi.Input[int] min_special: Minimum number of special characters in the result.
        :param pulumi.Input[int] min_upper: Minimum number of uppercase alphabet characters in the result.
        :param pulumi.Input[bool] number: Include numeric characters in the result.
        :param pulumi.Input[str] override_special: Supply your own list of special characters to use for string generation. This overrides the default character list in
               the special argument. The `special` argument must still be set to true for any overwritten characters to be used in
               generation.
        :param pulumi.Input[str] result: The generated random string.
        :param pulumi.Input[bool] special: Include special characters in the result. These are `!@#$%&*()-_=+[]{}<>:?`
        :param pulumi.Input[bool] upper: Include uppercase alphabet characters in the result.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RandomPasswordState.__new__(_RandomPasswordState)

        __props__.__dict__["keepers"] = keepers
        __props__.__dict__["length"] = length
        __props__.__dict__["lower"] = lower
        __props__.__dict__["min_lower"] = min_lower
        __props__.__dict__["min_numeric"] = min_numeric
        __props__.__dict__["min_special"] = min_special
        __props__.__dict__["min_upper"] = min_upper
        __props__.__dict__["number"] = number
        __props__.__dict__["override_special"] = override_special
        __props__.__dict__["result"] = result
        __props__.__dict__["special"] = special
        __props__.__dict__["upper"] = upper
        return RandomPassword(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def keepers(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Arbitrary map of values that, when changed, will trigger recreation of resource. See [the main provider
        documentation](../index.html) for more information.
        """
        return pulumi.get(self, "keepers")

    @property
    @pulumi.getter
    def length(self) -> pulumi.Output[int]:
        """
        The length of the string desired.
        """
        return pulumi.get(self, "length")

    @property
    @pulumi.getter
    def lower(self) -> pulumi.Output[Optional[bool]]:
        """
        Include lowercase alphabet characters in the result.
        """
        return pulumi.get(self, "lower")

    @property
    @pulumi.getter(name="minLower")
    def min_lower(self) -> pulumi.Output[Optional[int]]:
        """
        Minimum number of lowercase alphabet characters in the result.
        """
        return pulumi.get(self, "min_lower")

    @property
    @pulumi.getter(name="minNumeric")
    def min_numeric(self) -> pulumi.Output[Optional[int]]:
        """
        Minimum number of numeric characters in the result.
        """
        return pulumi.get(self, "min_numeric")

    @property
    @pulumi.getter(name="minSpecial")
    def min_special(self) -> pulumi.Output[Optional[int]]:
        """
        Minimum number of special characters in the result.
        """
        return pulumi.get(self, "min_special")

    @property
    @pulumi.getter(name="minUpper")
    def min_upper(self) -> pulumi.Output[Optional[int]]:
        """
        Minimum number of uppercase alphabet characters in the result.
        """
        return pulumi.get(self, "min_upper")

    @property
    @pulumi.getter
    def number(self) -> pulumi.Output[Optional[bool]]:
        """
        Include numeric characters in the result.
        """
        return pulumi.get(self, "number")

    @property
    @pulumi.getter(name="overrideSpecial")
    def override_special(self) -> pulumi.Output[Optional[str]]:
        """
        Supply your own list of special characters to use for string generation. This overrides the default character list in
        the special argument. The `special` argument must still be set to true for any overwritten characters to be used in
        generation.
        """
        return pulumi.get(self, "override_special")

    @property
    @pulumi.getter
    def result(self) -> pulumi.Output[str]:
        """
        The generated random string.
        """
        return pulumi.get(self, "result")

    @property
    @pulumi.getter
    def special(self) -> pulumi.Output[Optional[bool]]:
        """
        Include special characters in the result. These are `!@#$%&*()-_=+[]{}<>:?`
        """
        return pulumi.get(self, "special")

    @property
    @pulumi.getter
    def upper(self) -> pulumi.Output[Optional[bool]]:
        """
        Include uppercase alphabet characters in the result.
        """
        return pulumi.get(self, "upper")

