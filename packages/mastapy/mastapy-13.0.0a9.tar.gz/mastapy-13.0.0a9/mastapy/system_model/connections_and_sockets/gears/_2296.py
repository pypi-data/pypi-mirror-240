"""AGMAGleasonConicalGearMesh"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.connections_and_sockets.gears import _2304
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "AGMAGleasonConicalGearMesh"
)


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMesh",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMesh")


class AGMAGleasonConicalGearMesh(_2304.ConicalGearMesh):
    """AGMAGleasonConicalGearMesh

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearMesh")

    class _Cast_AGMAGleasonConicalGearMesh:
        """Special nested class for casting AGMAGleasonConicalGearMesh to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
            parent: "AGMAGleasonConicalGearMesh",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ):
            return self._parent._cast(_2304.ConicalGearMesh)

        @property
        def gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2278

            return self._parent._cast(_2278.InterMountableComponentConnection)

        @property
        def connection(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2269

            return self._parent._cast(_2269.Connection)

        @property
        def design_entity(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ):
            from mastapy.system_model import _2200

            return self._parent._cast(_2200.DesignEntity)

        @property
        def bevel_differential_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2298

            return self._parent._cast(_2298.BevelDifferentialGearMesh)

        @property
        def bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2300

            return self._parent._cast(_2300.BevelGearMesh)

        @property
        def hypoid_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2312

            return self._parent._cast(_2312.HypoidGearMesh)

        @property
        def spiral_bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2324

            return self._parent._cast(_2324.StraightBevelGearMesh)

        @property
        def zerol_bevel_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.ZerolBevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
        ) -> "AGMAGleasonConicalGearMesh":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMesh._Cast_AGMAGleasonConicalGearMesh":
        return self._Cast_AGMAGleasonConicalGearMesh(self)
