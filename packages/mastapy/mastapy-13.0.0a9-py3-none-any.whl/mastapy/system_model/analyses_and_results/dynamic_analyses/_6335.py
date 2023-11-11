"""GearSetDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "GearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2529


__docformat__ = "restructuredtext en"
__all__ = ("GearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="GearSetDynamicAnalysis")


class GearSetDynamicAnalysis(_6373.SpecialisedAssemblyDynamicAnalysis):
    """GearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetDynamicAnalysis")

    class _Cast_GearSetDynamicAnalysis:
        """Special nested class for casting GearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
            parent: "GearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            return self._parent._cast(_6373.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6273

            return self._parent._cast(_6273.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279

            return self._parent._cast(_6279.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286

            return self._parent._cast(_6286.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.BevelGearSetDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ConicalGearSetDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322

            return self._parent._cast(_6322.CylindricalGearSetDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.FaceGearSetDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(
                _6343.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(
                _6346.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(
                _6349.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(_6359.PlanetaryGearSetDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.SpiralBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.StraightBevelGearSetDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.ZerolBevelGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "GearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2529.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis":
        return self._Cast_GearSetDynamicAnalysis(self)
