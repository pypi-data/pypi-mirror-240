"""ConicalGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6892
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.system_model.analyses_and_results.static_loads import _6844


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetLoadCase",)


Self = TypeVar("Self", bound="ConicalGearSetLoadCase")


class ConicalGearSetLoadCase(_6892.GearSetLoadCase):
    """ConicalGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetLoadCase")

    class _Cast_ConicalGearSetLoadCase:
        """Special nested class for casting ConicalGearSetLoadCase to subclasses."""

        def __init__(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
            parent: "ConicalGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            return self._parent._cast(_6892.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6803

            return self._parent._cast(_6803.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.PartLoadCase)

        @property
        def part_analysis(self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6812

            return self._parent._cast(_6812.AGMAGleasonConicalGearSetLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6821

            return self._parent._cast(_6821.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.BevelGearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6904

            return self._parent._cast(_6904.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(
                _6911.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(
                _6914.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(
                _6917.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def spiral_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.StraightBevelGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.ZerolBevelGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "ConicalGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2521.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def get_harmonic_load_data_for_import(
        self: Self,
    ) -> "_6844.ConicalGearSetHarmonicLoadData":
        """mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetHarmonicLoadData"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase":
        return self._Cast_ConicalGearSetLoadCase(self)
