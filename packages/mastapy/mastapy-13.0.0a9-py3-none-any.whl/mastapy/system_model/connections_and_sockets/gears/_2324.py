"""StraightBevelGearMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2300
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "StraightBevelGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel import _960


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMesh",)


Self = TypeVar("Self", bound="StraightBevelGearMesh")


class StraightBevelGearMesh(_2300.BevelGearMesh):
    """StraightBevelGearMesh

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearMesh")

    class _Cast_StraightBevelGearMesh:
        """Special nested class for casting StraightBevelGearMesh to subclasses."""

        def __init__(
            self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh",
            parent: "StraightBevelGearMesh",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh(self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh"):
            return self._parent._cast(_2300.BevelGearMesh)

        @property
        def agma_gleason_conical_gear_mesh(
            self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2296

            return self._parent._cast(_2296.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2304

            return self._parent._cast(_2304.ConicalGearMesh)

        @property
        def gear_mesh(self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2278

            return self._parent._cast(_2278.InterMountableComponentConnection)

        @property
        def connection(self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh"):
            from mastapy.system_model.connections_and_sockets import _2269

            return self._parent._cast(_2269.Connection)

        @property
        def design_entity(self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh"):
            from mastapy.system_model import _2200

            return self._parent._cast(_2200.DesignEntity)

        @property
        def straight_bevel_gear_mesh(
            self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh",
        ) -> "StraightBevelGearMesh":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMesh._Cast_StraightBevelGearMesh", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_mesh_design(self: Self) -> "_960.StraightBevelGearMeshDesign":
        """mastapy.gears.gear_designs.straight_bevel.StraightBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_gear_mesh_design(
        self: Self,
    ) -> "_960.StraightBevelGearMeshDesign":
        """mastapy.gears.gear_designs.straight_bevel.StraightBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "StraightBevelGearMesh._Cast_StraightBevelGearMesh":
        return self._Cast_StraightBevelGearMesh(self)
