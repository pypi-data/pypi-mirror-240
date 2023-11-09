# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetGatewayResult',
    'AwaitableGetGatewayResult',
    'get_gateway',
    'get_gateway_output',
]

@pulumi.output_type
class GetGatewayResult:
    """
    A collection of values returned by getGateway.
    """
    def __init__(__self__, gateway_id=None, id=None, ip_reservation_id=None, private_ipv4_subnet_size=None, project_id=None, state=None, vlan_id=None, vrf_id=None):
        if gateway_id and not isinstance(gateway_id, str):
            raise TypeError("Expected argument 'gateway_id' to be a str")
        pulumi.set(__self__, "gateway_id", gateway_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_reservation_id and not isinstance(ip_reservation_id, str):
            raise TypeError("Expected argument 'ip_reservation_id' to be a str")
        pulumi.set(__self__, "ip_reservation_id", ip_reservation_id)
        if private_ipv4_subnet_size and not isinstance(private_ipv4_subnet_size, int):
            raise TypeError("Expected argument 'private_ipv4_subnet_size' to be a int")
        pulumi.set(__self__, "private_ipv4_subnet_size", private_ipv4_subnet_size)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if vlan_id and not isinstance(vlan_id, str):
            raise TypeError("Expected argument 'vlan_id' to be a str")
        pulumi.set(__self__, "vlan_id", vlan_id)
        if vrf_id and not isinstance(vrf_id, str):
            raise TypeError("Expected argument 'vrf_id' to be a str")
        pulumi.set(__self__, "vrf_id", vrf_id)

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> str:
        return pulumi.get(self, "gateway_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipReservationId")
    def ip_reservation_id(self) -> str:
        """
        UUID of IP reservation block bound to the gateway.
        """
        return pulumi.get(self, "ip_reservation_id")

    @property
    @pulumi.getter(name="privateIpv4SubnetSize")
    def private_ipv4_subnet_size(self) -> int:
        """
        Size of the private IPv4 subnet bound to this metal gateway. One of
        `8`, `16`, `32`, `64`, `128`.
        """
        return pulumi.get(self, "private_ipv4_subnet_size")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        UUID of the project where the gateway is scoped to.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Status of the gateway resource.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> str:
        """
        UUID of the VLAN where the gateway is scoped to.
        """
        return pulumi.get(self, "vlan_id")

    @property
    @pulumi.getter(name="vrfId")
    def vrf_id(self) -> str:
        """
        UUID of the VRF associated with the IP Reservation.
        """
        return pulumi.get(self, "vrf_id")


class AwaitableGetGatewayResult(GetGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGatewayResult(
            gateway_id=self.gateway_id,
            id=self.id,
            ip_reservation_id=self.ip_reservation_id,
            private_ipv4_subnet_size=self.private_ipv4_subnet_size,
            project_id=self.project_id,
            state=self.state,
            vlan_id=self.vlan_id,
            vrf_id=self.vrf_id)


def get_gateway(gateway_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGatewayResult:
    """
    Use this datasource to retrieve Metal Gateway resources in Equinix Metal.

    > VRF features are not generally available. The interfaces related to VRF resources may change ahead of general availability.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_equinix as equinix

    # Create Metal Gateway for a VLAN with a private IPv4 block with 8 IP addresses
    test_vlan = equinix.metal.Vlan("testVlan",
        description="test VLAN in SV",
        metro="sv",
        project_id=local["project_id"])
    test_gateway = equinix.metal.get_gateway(gateway_id=local["gateway_id"])
    ```


    :param str gateway_id: UUID of the metal gateway resource to retrieve.
    """
    __args__ = dict()
    __args__['gatewayId'] = gateway_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('equinix:metal/getGateway:getGateway', __args__, opts=opts, typ=GetGatewayResult).value

    return AwaitableGetGatewayResult(
        gateway_id=pulumi.get(__ret__, 'gateway_id'),
        id=pulumi.get(__ret__, 'id'),
        ip_reservation_id=pulumi.get(__ret__, 'ip_reservation_id'),
        private_ipv4_subnet_size=pulumi.get(__ret__, 'private_ipv4_subnet_size'),
        project_id=pulumi.get(__ret__, 'project_id'),
        state=pulumi.get(__ret__, 'state'),
        vlan_id=pulumi.get(__ret__, 'vlan_id'),
        vrf_id=pulumi.get(__ret__, 'vrf_id'))


@_utilities.lift_output_func(get_gateway)
def get_gateway_output(gateway_id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGatewayResult]:
    """
    Use this datasource to retrieve Metal Gateway resources in Equinix Metal.

    > VRF features are not generally available. The interfaces related to VRF resources may change ahead of general availability.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_equinix as equinix

    # Create Metal Gateway for a VLAN with a private IPv4 block with 8 IP addresses
    test_vlan = equinix.metal.Vlan("testVlan",
        description="test VLAN in SV",
        metro="sv",
        project_id=local["project_id"])
    test_gateway = equinix.metal.get_gateway(gateway_id=local["gateway_id"])
    ```


    :param str gateway_id: UUID of the metal gateway resource to retrieve.
    """
    ...
