"""ConicalGearTeethSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2311
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "ConicalGearTeethSocket"
)


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearTeethSocket",)


Self = TypeVar("Self", bound="ConicalGearTeethSocket")


class ConicalGearTeethSocket(_2311.GearTeethSocket):
    """ConicalGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearTeethSocket")

    class _Cast_ConicalGearTeethSocket:
        """Special nested class for casting ConicalGearTeethSocket to subclasses."""

        def __init__(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
            parent: "ConicalGearTeethSocket",
        ):
            self._parent = parent

        @property
        def gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ):
            return self._parent._cast(_2311.GearTeethSocket)

        @property
        def socket(self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket"):
            from mastapy.system_model.connections_and_sockets import _2293

            return self._parent._cast(_2293.Socket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2297

            return self._parent._cast(_2297.AGMAGleasonConicalGearTeethSocket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2299

            return self._parent._cast(_2299.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2301

            return self._parent._cast(_2301.BevelGearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2313

            return self._parent._cast(_2313.HypoidGearTeethSocket)

        @property
        def klingelnberg_conical_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2314

            return self._parent._cast(_2314.KlingelnbergConicalGearTeethSocket)

        @property
        def klingelnberg_hypoid_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2318

            return self._parent._cast(_2318.KlingelnbergHypoidGearTeethSocket)

        @property
        def klingelnberg_spiral_bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2319

            return self._parent._cast(_2319.KlingelnbergSpiralBevelGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.StraightBevelGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.ZerolBevelGearTeethSocket)

        @property
        def conical_gear_teeth_socket(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket",
        ) -> "ConicalGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearTeethSocket.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "ConicalGearTeethSocket._Cast_ConicalGearTeethSocket":
        return self._Cast_ConicalGearTeethSocket(self)
