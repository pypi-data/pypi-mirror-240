"""GearSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2779
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "GearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.math_utility.measured_vectors import _1557
    from mastapy.system_model.analyses_and_results.system_deflections import _2757
    from mastapy.system_model.analyses_and_results.power_flows import _4090


__docformat__ = "restructuredtext en"
__all__ = ("GearSystemDeflection",)


Self = TypeVar("Self", bound="GearSystemDeflection")


class GearSystemDeflection(_2779.MountableComponentSystemDeflection):
    """GearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSystemDeflection")

    class _Cast_GearSystemDeflection:
        """Special nested class for casting GearSystemDeflection to subclasses."""

        def __init__(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
            parent: "GearSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            return self._parent._cast(_2779.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(self: "GearSystemDeflection._Cast_GearSystemDeflection"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "GearSystemDeflection._Cast_GearSystemDeflection"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "GearSystemDeflection._Cast_GearSystemDeflection"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(_2688.AGMAGleasonConicalGearSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2701,
            )

            return self._parent._cast(_2701.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelGearSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2719,
            )

            return self._parent._cast(_2719.ConceptGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ConicalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2742,
            )

            return self._parent._cast(_2742.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(
                _2744.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.CylindricalPlanetGearSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.FaceGearSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2770,
            )

            return self._parent._cast(
                _2770.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2773,
            )

            return self._parent._cast(
                _2773.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def spiral_bevel_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.SpiralBevelGearSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2812,
            )

            return self._parent._cast(_2812.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2815,
            )

            return self._parent._cast(_2815.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelSunGearSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2835,
            )

            return self._parent._cast(_2835.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.ZerolBevelGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "GearSystemDeflection._Cast_GearSystemDeflection",
        ) -> "GearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearSystemDeflection._Cast_GearSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_loaded(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsLoaded

        if temp is None:
            return False

        return temp

    @property
    def component_design(self: Self) -> "_2527.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_point_results_in_wcs(
        self: Self,
    ) -> "List[_1557.ForceAndDisplacementResults]":
        """List[mastapy.math_utility.measured_vectors.ForceAndDisplacementResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshPointResultsInWCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_set(self: Self) -> "_2757.GearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4090.GearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.GearPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearSystemDeflection._Cast_GearSystemDeflection":
        return self._Cast_GearSystemDeflection(self)
