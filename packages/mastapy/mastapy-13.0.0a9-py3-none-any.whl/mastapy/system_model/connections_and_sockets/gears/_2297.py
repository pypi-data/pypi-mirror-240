"""AGMAGleasonConicalGearTeethSocket"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2305
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_TEETH_SOCKET = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "AGMAGleasonConicalGearTeethSocket",
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearTeethSocket",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearTeethSocket")


class AGMAGleasonConicalGearTeethSocket(_2305.ConicalGearTeethSocket):
    """AGMAGleasonConicalGearTeethSocket

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_TEETH_SOCKET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearTeethSocket")

    class _Cast_AGMAGleasonConicalGearTeethSocket:
        """Special nested class for casting AGMAGleasonConicalGearTeethSocket to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
            parent: "AGMAGleasonConicalGearTeethSocket",
        ):
            self._parent = parent

        @property
        def conical_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ):
            return self._parent._cast(_2305.ConicalGearTeethSocket)

        @property
        def gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2311

            return self._parent._cast(_2311.GearTeethSocket)

        @property
        def socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets import _2293

            return self._parent._cast(_2293.Socket)

        @property
        def bevel_differential_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2299

            return self._parent._cast(_2299.BevelDifferentialGearTeethSocket)

        @property
        def bevel_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2301

            return self._parent._cast(_2301.BevelGearTeethSocket)

        @property
        def hypoid_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2313

            return self._parent._cast(_2313.HypoidGearTeethSocket)

        @property
        def spiral_bevel_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2321

            return self._parent._cast(_2321.SpiralBevelGearTeethSocket)

        @property
        def straight_bevel_diff_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2323

            return self._parent._cast(_2323.StraightBevelDiffGearTeethSocket)

        @property
        def straight_bevel_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2325

            return self._parent._cast(_2325.StraightBevelGearTeethSocket)

        @property
        def zerol_bevel_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2329

            return self._parent._cast(_2329.ZerolBevelGearTeethSocket)

        @property
        def agma_gleason_conical_gear_teeth_socket(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
        ) -> "AGMAGleasonConicalGearTeethSocket":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearTeethSocket.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearTeethSocket._Cast_AGMAGleasonConicalGearTeethSocket":
        return self._Cast_AGMAGleasonConicalGearTeethSocket(self)
