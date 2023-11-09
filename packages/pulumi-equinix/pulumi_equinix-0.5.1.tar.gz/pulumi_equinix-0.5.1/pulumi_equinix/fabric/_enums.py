# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AccessPointLinkProtocolType',
    'AccessPointPeeringType',
    'AccessPointType',
    'ConnectionType',
    'NotificationsType',
    'ProfileAccessPointType',
    'ProfileState',
    'ProfileType',
    'ProfileVisibility',
    'ServiceTokenType',
]


class AccessPointLinkProtocolType(str, Enum):
    UNTAGGED = "UNTAGGED"
    DOT1Q = "DOT1Q"
    QIN_Q = "QINQ"
    EVP_N_VXLAN = "EVPN_VXLAN"


class AccessPointPeeringType(str, Enum):
    PRIVATE = "PRIVATE"
    MICROSOFT = "MICROSOFT"
    PUBLIC = "PUBLIC"


class AccessPointType(str, Enum):
    COLO = "COLO"
    """
    Colocation
    """
    VD = "VD"
    """
    Virtual Device
    """
    SP = "SP"
    """
    Service Profile
    """
    IGW = "IGW"
    """
    Internet Gateway
    """
    SUBNET = "SUBNET"
    """
    Subnet
    """
    GW = "GW"
    """
    Gateway
    """
    NETWORK = "NETWORK"
    """
    Network
    """


class ConnectionType(str, Enum):
    VG = "VG_VC"
    """
    Virtual Gateway
    """
    EVPL = "EVPL_VC"
    """
    Ethernet Virtual Private Line
    """
    EPL = "EPL_VC"
    """
    Ethernet Private Line
    """
    GW = "GW_VC"
    """
    Fabric Gateway virtual connection
    """
    ACCESS_EPL = "ACCESS_EPL_VC"
    """
    E-access, layer 2 connection between a QINQ port and an EPL port.
    """


class NotificationsType(str, Enum):
    ALL = "ALL"
    CONNECTION_APPROVAL = "CONNECTION_APPROVAL"
    SALES_NOTIFICATIONS = "SALES_REP_NOTIFICATIONS"
    NOTIFICATIONS = "NOTIFICATIONS"


class ProfileAccessPointType(str, Enum):
    COLO = "COLO"
    """
    Colocation
    """
    VD = "VD"
    """
    Virtual Device
    """


class ProfileState(str, Enum):
    ACTIVE = "ACTIVE"
    PENDING_APPROVAL = "PENDING_APPROVAL"
    DELETED = "DELETED"
    REJECTED = "REJECTED"


class ProfileType(str, Enum):
    L2_PROFILE = "L2_PROFILE"
    L3_PROFILE = "L3_PROFILE"


class ProfileVisibility(str, Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


class ServiceTokenType(str, Enum):
    VC_TOKEN = "VC_TOKEN"
