"""SpiralBevelGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6826
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SpiralBevelGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import _6950, _6951


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearSetLoadCase",)


Self = TypeVar("Self", bound="SpiralBevelGearSetLoadCase")


class SpiralBevelGearSetLoadCase(_6826.BevelGearSetLoadCase):
    """SpiralBevelGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearSetLoadCase")

    class _Cast_SpiralBevelGearSetLoadCase:
        """Special nested class for casting SpiralBevelGearSetLoadCase to subclasses."""

        def __init__(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
            parent: "SpiralBevelGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ):
            return self._parent._cast(_6826.BevelGearSetLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6812

            return self._parent._cast(_6812.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6892

            return self._parent._cast(_6892.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6803

            return self._parent._cast(_6803.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.PartLoadCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
        ) -> "SpiralBevelGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2541.SpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.SpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_6950.SpiralBevelGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_gears_load_case(
        self: Self,
    ) -> "List[_6950.SpiralBevelGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spiral_bevel_meshes_load_case(
        self: Self,
    ) -> "List[_6951.SpiralBevelGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearSetLoadCase._Cast_SpiralBevelGearSetLoadCase":
        return self._Cast_SpiralBevelGearSetLoadCase(self)
