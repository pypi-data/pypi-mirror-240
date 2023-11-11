"""StraightBevelDiffGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2517
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel_diff import _965
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.connections_and_sockets.gears import _2322


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSet",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSet")


class StraightBevelDiffGearSet(_2517.BevelGearSet):
    """StraightBevelDiffGearSet

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearSet")

    class _Cast_StraightBevelDiffGearSet:
        """Special nested class for casting StraightBevelDiffGearSet to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
            parent: "StraightBevelDiffGearSet",
        ):
            self._parent = parent

        @property
        def bevel_gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ):
            return self._parent._cast(_2517.BevelGearSet)

        @property
        def agma_gleason_conical_gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2511

            return self._parent._cast(_2511.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.ConicalGearSet)

        @property
        def gear_set(self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet"):
            from mastapy.system_model.part_model.gears import _2529

            return self._parent._cast(_2529.GearSet)

        @property
        def specialised_assembly(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ):
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ):
            from mastapy.system_model.part_model import _2431

            return self._parent._cast(_2431.AbstractAssembly)

        @property
        def part(self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet"):
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.Part)

        @property
        def design_entity(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ):
            from mastapy.system_model import _2200

            return self._parent._cast(_2200.DesignEntity)

        @property
        def straight_bevel_diff_gear_set(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet",
        ) -> "StraightBevelDiffGearSet":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self: Self) -> "_965.StraightBevelDiffGearSetDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gear_set_design(
        self: Self,
    ) -> "_965.StraightBevelDiffGearSetDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gears(self: Self) -> "List[_2542.StraightBevelDiffGear]":
        """List[mastapy.system_model.part_model.gears.StraightBevelDiffGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes(
        self: Self,
    ) -> "List[_2322.StraightBevelDiffGearMesh]":
        """List[mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSet._Cast_StraightBevelDiffGearSet":
        return self._Cast_StraightBevelDiffGearSet(self)
