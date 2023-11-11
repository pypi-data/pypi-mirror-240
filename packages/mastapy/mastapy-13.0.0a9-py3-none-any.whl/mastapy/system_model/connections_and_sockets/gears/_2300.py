"""BevelGearMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2296
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "BevelGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1179


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMesh",)


Self = TypeVar("Self", bound="BevelGearMesh")


class BevelGearMesh(_2296.AGMAGleasonConicalGearMesh):
    """BevelGearMesh

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMesh")

    class _Cast_BevelGearMesh:
        """Special nested class for casting BevelGearMesh to subclasses."""

        def __init__(
            self: "BevelGearMesh._Cast_BevelGearMesh", parent: "BevelGearMesh"
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh(self: "BevelGearMesh._Cast_BevelGearMesh"):
            return self._parent._cast(_2296.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(self: "BevelGearMesh._Cast_BevelGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2304

            return self._parent._cast(_2304.ConicalGearMesh)

        @property
        def gear_mesh(self: "BevelGearMesh._Cast_BevelGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2278

            return self._parent._cast(_2278.InterMountableComponentConnection)

        @property
        def connection(self: "BevelGearMesh._Cast_BevelGearMesh"):
            from mastapy.system_model.connections_and_sockets import _2269

            return self._parent._cast(_2269.Connection)

        @property
        def design_entity(self: "BevelGearMesh._Cast_BevelGearMesh"):
            from mastapy.system_model import _2200

            return self._parent._cast(_2200.DesignEntity)

        @property
        def bevel_differential_gear_mesh(self: "BevelGearMesh._Cast_BevelGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2298

            return self._parent._cast(_2298.BevelDifferentialGearMesh)

        @property
        def spiral_bevel_gear_mesh(self: "BevelGearMesh._Cast_BevelGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2320

            return self._parent._cast(_2320.SpiralBevelGearMesh)

        @property
        def straight_bevel_diff_gear_mesh(self: "BevelGearMesh._Cast_BevelGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2322

            return self._parent._cast(_2322.StraightBevelDiffGearMesh)

        @property
        def straight_bevel_gear_mesh(self: "BevelGearMesh._Cast_BevelGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2324

            return self._parent._cast(_2324.StraightBevelGearMesh)

        @property
        def zerol_bevel_gear_mesh(self: "BevelGearMesh._Cast_BevelGearMesh"):
            from mastapy.system_model.connections_and_sockets.gears import _2328

            return self._parent._cast(_2328.ZerolBevelGearMesh)

        @property
        def bevel_gear_mesh(
            self: "BevelGearMesh._Cast_BevelGearMesh",
        ) -> "BevelGearMesh":
            return self._parent

        def __getattr__(self: "BevelGearMesh._Cast_BevelGearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_mesh_design(self: Self) -> "_1179.BevelGearMeshDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_mesh_design(self: Self) -> "_1179.BevelGearMeshDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearMesh._Cast_BevelGearMesh":
        return self._Cast_BevelGearMesh(self)
