"""FaceGearDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "FaceGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525
    from mastapy.system_model.analyses_and_results.static_loads import _6881


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearDynamicAnalysis",)


Self = TypeVar("Self", bound="FaceGearDynamicAnalysis")


class FaceGearDynamicAnalysis(_6333.GearDynamicAnalysis):
    """FaceGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearDynamicAnalysis")

    class _Cast_FaceGearDynamicAnalysis:
        """Special nested class for casting FaceGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis",
            parent: "FaceGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_dynamic_analysis(
            self: "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis",
        ):
            return self._parent._cast(_6333.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(_6354.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def face_gear_dynamic_analysis(
            self: "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis",
        ) -> "FaceGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2525.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6881.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FaceGearDynamicAnalysis._Cast_FaceGearDynamicAnalysis":
        return self._Cast_FaceGearDynamicAnalysis(self)
