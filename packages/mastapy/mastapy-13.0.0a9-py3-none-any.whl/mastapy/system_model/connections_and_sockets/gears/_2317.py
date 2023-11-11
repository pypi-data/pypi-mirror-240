"""KlingelnbergCycloPalloidSpiralBevelGearMesh"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2315
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGearMesh",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _972


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearMesh",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearMesh")


class KlingelnbergCycloPalloidSpiralBevelGearMesh(
    _2315.KlingelnbergCycloPalloidConicalGearMesh
):
    """KlingelnbergCycloPalloidSpiralBevelGearMesh

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_MESH
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearMesh"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearMesh:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearMesh to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMesh._Cast_KlingelnbergCycloPalloidSpiralBevelGearMesh",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearMesh",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMesh._Cast_KlingelnbergCycloPalloidSpiralBevelGearMesh",
        ):
            return self._parent._cast(_2315.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMesh._Cast_KlingelnbergCycloPalloidSpiralBevelGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2304

            return self._parent._cast(_2304.ConicalGearMesh)

        @property
        def gear_mesh(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMesh._Cast_KlingelnbergCycloPalloidSpiralBevelGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets.gears import _2310

            return self._parent._cast(_2310.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMesh._Cast_KlingelnbergCycloPalloidSpiralBevelGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2278

            return self._parent._cast(_2278.InterMountableComponentConnection)

        @property
        def connection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMesh._Cast_KlingelnbergCycloPalloidSpiralBevelGearMesh",
        ):
            from mastapy.system_model.connections_and_sockets import _2269

            return self._parent._cast(_2269.Connection)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMesh._Cast_KlingelnbergCycloPalloidSpiralBevelGearMesh",
        ):
            from mastapy.system_model import _2200

            return self._parent._cast(_2200.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMesh._Cast_KlingelnbergCycloPalloidSpiralBevelGearMesh",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearMesh":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearMesh._Cast_KlingelnbergCycloPalloidSpiralBevelGearMesh",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_mesh_design(
        self: Self,
    ) -> "_972.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(
        self: Self,
    ) -> "_972.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearMesh._Cast_KlingelnbergCycloPalloidSpiralBevelGearMesh":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearMesh(self)
