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

__all__ = ['NodeArgs', 'Node']

@pulumi.input_type
class NodeArgs:
    def __init__(__self__, *,
                 gateway: Optional[pulumi.Input['NodeGatewayArgs']] = None,
                 relay: Optional[pulumi.Input['NodeRelayArgs']] = None):
        """
        The set of arguments for constructing a Node resource.
        :param pulumi.Input['NodeGatewayArgs'] gateway: Gateway represents a StrongDM CLI installation running in gateway mode.
        :param pulumi.Input['NodeRelayArgs'] relay: Relay represents a StrongDM CLI installation running in relay mode.
        """
        if gateway is not None:
            pulumi.set(__self__, "gateway", gateway)
        if relay is not None:
            pulumi.set(__self__, "relay", relay)

    @property
    @pulumi.getter
    def gateway(self) -> Optional[pulumi.Input['NodeGatewayArgs']]:
        """
        Gateway represents a StrongDM CLI installation running in gateway mode.
        """
        return pulumi.get(self, "gateway")

    @gateway.setter
    def gateway(self, value: Optional[pulumi.Input['NodeGatewayArgs']]):
        pulumi.set(self, "gateway", value)

    @property
    @pulumi.getter
    def relay(self) -> Optional[pulumi.Input['NodeRelayArgs']]:
        """
        Relay represents a StrongDM CLI installation running in relay mode.
        """
        return pulumi.get(self, "relay")

    @relay.setter
    def relay(self, value: Optional[pulumi.Input['NodeRelayArgs']]):
        pulumi.set(self, "relay", value)


@pulumi.input_type
class _NodeState:
    def __init__(__self__, *,
                 gateway: Optional[pulumi.Input['NodeGatewayArgs']] = None,
                 relay: Optional[pulumi.Input['NodeRelayArgs']] = None):
        """
        Input properties used for looking up and filtering Node resources.
        :param pulumi.Input['NodeGatewayArgs'] gateway: Gateway represents a StrongDM CLI installation running in gateway mode.
        :param pulumi.Input['NodeRelayArgs'] relay: Relay represents a StrongDM CLI installation running in relay mode.
        """
        if gateway is not None:
            pulumi.set(__self__, "gateway", gateway)
        if relay is not None:
            pulumi.set(__self__, "relay", relay)

    @property
    @pulumi.getter
    def gateway(self) -> Optional[pulumi.Input['NodeGatewayArgs']]:
        """
        Gateway represents a StrongDM CLI installation running in gateway mode.
        """
        return pulumi.get(self, "gateway")

    @gateway.setter
    def gateway(self, value: Optional[pulumi.Input['NodeGatewayArgs']]):
        pulumi.set(self, "gateway", value)

    @property
    @pulumi.getter
    def relay(self) -> Optional[pulumi.Input['NodeRelayArgs']]:
        """
        Relay represents a StrongDM CLI installation running in relay mode.
        """
        return pulumi.get(self, "relay")

    @relay.setter
    def relay(self, value: Optional[pulumi.Input['NodeRelayArgs']]):
        pulumi.set(self, "relay", value)


class Node(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 gateway: Optional[pulumi.Input[pulumi.InputType['NodeGatewayArgs']]] = None,
                 relay: Optional[pulumi.Input[pulumi.InputType['NodeRelayArgs']]] = None,
                 __props__=None):
        """
        ## Import

        Node can be imported using the id, e.g.,

        ```sh
         $ pulumi import sdm:index/node:Node example n-12345678
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['NodeGatewayArgs']] gateway: Gateway represents a StrongDM CLI installation running in gateway mode.
        :param pulumi.Input[pulumi.InputType['NodeRelayArgs']] relay: Relay represents a StrongDM CLI installation running in relay mode.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[NodeArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        Node can be imported using the id, e.g.,

        ```sh
         $ pulumi import sdm:index/node:Node example n-12345678
        ```

        :param str resource_name: The name of the resource.
        :param NodeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NodeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 gateway: Optional[pulumi.Input[pulumi.InputType['NodeGatewayArgs']]] = None,
                 relay: Optional[pulumi.Input[pulumi.InputType['NodeRelayArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NodeArgs.__new__(NodeArgs)

            __props__.__dict__["gateway"] = gateway
            __props__.__dict__["relay"] = relay
        super(Node, __self__).__init__(
            'sdm:index/node:Node',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            gateway: Optional[pulumi.Input[pulumi.InputType['NodeGatewayArgs']]] = None,
            relay: Optional[pulumi.Input[pulumi.InputType['NodeRelayArgs']]] = None) -> 'Node':
        """
        Get an existing Node resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['NodeGatewayArgs']] gateway: Gateway represents a StrongDM CLI installation running in gateway mode.
        :param pulumi.Input[pulumi.InputType['NodeRelayArgs']] relay: Relay represents a StrongDM CLI installation running in relay mode.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NodeState.__new__(_NodeState)

        __props__.__dict__["gateway"] = gateway
        __props__.__dict__["relay"] = relay
        return Node(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def gateway(self) -> pulumi.Output[Optional['outputs.NodeGateway']]:
        """
        Gateway represents a StrongDM CLI installation running in gateway mode.
        """
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter
    def relay(self) -> pulumi.Output[Optional['outputs.NodeRelay']]:
        """
        Relay represents a StrongDM CLI installation running in relay mode.
        """
        return pulumi.get(self, "relay")

