"""ClutchDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "ClutchDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2575
    from mastapy.system_model.analyses_and_results.static_loads import _6831


__docformat__ = "restructuredtext en"
__all__ = ("ClutchDynamicAnalysis",)


Self = TypeVar("Self", bound="ClutchDynamicAnalysis")


class ClutchDynamicAnalysis(_6311.CouplingDynamicAnalysis):
    """ClutchDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchDynamicAnalysis")

    class _Cast_ClutchDynamicAnalysis:
        """Special nested class for casting ClutchDynamicAnalysis to subclasses."""

        def __init__(
            self: "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis",
            parent: "ClutchDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_dynamic_analysis(
            self: "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis",
        ):
            return self._parent._cast(_6311.CouplingDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(_6373.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6273

            return self._parent._cast(_6273.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.PartDynamicAnalysis)

        @property
        def part_fe_analysis(self: "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis",
        ) -> "ClutchDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2575.Clutch":
        """mastapy.system_model.part_model.couplings.Clutch

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6831.ClutchLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ClutchDynamicAnalysis._Cast_ClutchDynamicAnalysis":
        return self._Cast_ClutchDynamicAnalysis(self)
