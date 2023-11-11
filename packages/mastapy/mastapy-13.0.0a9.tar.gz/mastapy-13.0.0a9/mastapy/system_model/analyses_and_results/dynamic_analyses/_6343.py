"""KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis")


class KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis(
    _6307.ConicalGearSetDynamicAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            return self._parent._cast(_6307.ConicalGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(_6373.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6273

            return self._parent._cast(_6273.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346

            return self._parent._cast(
                _6346.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(
                _6349.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2534.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis(self)
