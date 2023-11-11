"""StraightBevelGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2517
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel import _961
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.connections_and_sockets.gears import _2324


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSet",)


Self = TypeVar("Self", bound="StraightBevelGearSet")


class StraightBevelGearSet(_2517.BevelGearSet):
    """StraightBevelGearSet

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearSet")

    class _Cast_StraightBevelGearSet:
        """Special nested class for casting StraightBevelGearSet to subclasses."""

        def __init__(
            self: "StraightBevelGearSet._Cast_StraightBevelGearSet",
            parent: "StraightBevelGearSet",
        ):
            self._parent = parent

        @property
        def bevel_gear_set(self: "StraightBevelGearSet._Cast_StraightBevelGearSet"):
            return self._parent._cast(_2517.BevelGearSet)

        @property
        def agma_gleason_conical_gear_set(
            self: "StraightBevelGearSet._Cast_StraightBevelGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2511

            return self._parent._cast(_2511.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(self: "StraightBevelGearSet._Cast_StraightBevelGearSet"):
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.ConicalGearSet)

        @property
        def gear_set(self: "StraightBevelGearSet._Cast_StraightBevelGearSet"):
            from mastapy.system_model.part_model.gears import _2529

            return self._parent._cast(_2529.GearSet)

        @property
        def specialised_assembly(
            self: "StraightBevelGearSet._Cast_StraightBevelGearSet",
        ):
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.SpecialisedAssembly)

        @property
        def abstract_assembly(self: "StraightBevelGearSet._Cast_StraightBevelGearSet"):
            from mastapy.system_model.part_model import _2431

            return self._parent._cast(_2431.AbstractAssembly)

        @property
        def part(self: "StraightBevelGearSet._Cast_StraightBevelGearSet"):
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.Part)

        @property
        def design_entity(self: "StraightBevelGearSet._Cast_StraightBevelGearSet"):
            from mastapy.system_model import _2200

            return self._parent._cast(_2200.DesignEntity)

        @property
        def straight_bevel_gear_set(
            self: "StraightBevelGearSet._Cast_StraightBevelGearSet",
        ) -> "StraightBevelGearSet":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSet._Cast_StraightBevelGearSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self: Self) -> "_961.StraightBevelGearSetDesign":
        """mastapy.gears.gear_designs.straight_bevel.StraightBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_gear_set_design(self: Self) -> "_961.StraightBevelGearSetDesign":
        """mastapy.gears.gear_designs.straight_bevel.StraightBevelGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_gears(self: Self) -> "List[_2544.StraightBevelGear]":
        """List[mastapy.system_model.part_model.gears.StraightBevelGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes(self: Self) -> "List[_2324.StraightBevelGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "StraightBevelGearSet._Cast_StraightBevelGearSet":
        return self._Cast_StraightBevelGearSet(self)
