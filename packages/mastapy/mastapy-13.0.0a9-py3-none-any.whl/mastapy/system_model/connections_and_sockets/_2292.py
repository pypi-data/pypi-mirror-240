"""ShaftToMountableComponentConnection"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets import _2262
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets",
    "ShaftToMountableComponentConnection",
)


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnection",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnection")


class ShaftToMountableComponentConnection(
    _2262.AbstractShaftToMountableComponentConnection
):
    """ShaftToMountableComponentConnection

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftToMountableComponentConnection")

    class _Cast_ShaftToMountableComponentConnection:
        """Special nested class for casting ShaftToMountableComponentConnection to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
            parent: "ShaftToMountableComponentConnection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ):
            return self._parent._cast(_2262.AbstractShaftToMountableComponentConnection)

        @property
        def connection(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets import _2269

            return self._parent._cast(_2269.Connection)

        @property
        def design_entity(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ):
            from mastapy.system_model import _2200

            return self._parent._cast(_2200.DesignEntity)

        @property
        def coaxial_connection(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets import _2266

            return self._parent._cast(_2266.CoaxialConnection)

        @property
        def planetary_connection(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets import _2284

            return self._parent._cast(_2284.PlanetaryConnection)

        @property
        def cycloidal_disc_central_bearing_connection(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ):
            from mastapy.system_model.connections_and_sockets.cycloidal import _2332

            return self._parent._cast(_2332.CycloidalDiscCentralBearingConnection)

        @property
        def shaft_to_mountable_component_connection(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
        ) -> "ShaftToMountableComponentConnection":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "ShaftToMountableComponentConnection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ShaftToMountableComponentConnection._Cast_ShaftToMountableComponentConnection"
    ):
        return self._Cast_ShaftToMountableComponentConnection(self)
