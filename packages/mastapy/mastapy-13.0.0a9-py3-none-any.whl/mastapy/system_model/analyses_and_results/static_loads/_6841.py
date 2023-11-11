"""ConicalGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6887
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2520
    from mastapy.system_model.analyses_and_results.static_loads import _6842


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearLoadCase",)


Self = TypeVar("Self", bound="ConicalGearLoadCase")


class ConicalGearLoadCase(_6887.GearLoadCase):
    """ConicalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearLoadCase")

    class _Cast_ConicalGearLoadCase:
        """Special nested class for casting ConicalGearLoadCase to subclasses."""

        def __init__(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
            parent: "ConicalGearLoadCase",
        ):
            self._parent = parent

        @property
        def gear_load_case(self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase"):
            return self._parent._cast(_6887.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6921

            return self._parent._cast(_6921.MountableComponentLoadCase)

        @property
        def component_load_case(self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.ComponentLoadCase)

        @property
        def part_load_case(self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.PartLoadCase)

        @property
        def part_analysis(self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6810

            return self._parent._cast(_6810.AGMAGleasonConicalGearLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6819

            return self._parent._cast(_6819.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6822

            return self._parent._cast(_6822.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.BevelGearLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6902

            return self._parent._cast(_6902.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6909

            return self._parent._cast(_6909.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(
                _6915.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def spiral_bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.SpiralBevelGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6956

            return self._parent._cast(_6956.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6959

            return self._parent._cast(_6959.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.StraightBevelSunGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.ZerolBevelGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "ConicalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2520.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_manufacture_errors(self: Self) -> "_6842.ConicalGearManufactureError":
        """mastapy.system_model.analyses_and_results.static_loads.ConicalGearManufactureError

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearManufactureErrors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConicalGearLoadCase._Cast_ConicalGearLoadCase":
        return self._Cast_ConicalGearLoadCase(self)
