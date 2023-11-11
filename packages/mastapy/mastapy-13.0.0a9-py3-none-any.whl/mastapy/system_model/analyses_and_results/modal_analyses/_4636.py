"""HypoidGearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4573
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "HypoidGearModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.static_loads import _6902
    from mastapy.system_model.analyses_and_results.system_deflections import _2762


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearModalAnalysis",)


Self = TypeVar("Self", bound="HypoidGearModalAnalysis")


class HypoidGearModalAnalysis(_4573.AGMAGleasonConicalGearModalAnalysis):
    """HypoidGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearModalAnalysis")

    class _Cast_HypoidGearModalAnalysis:
        """Special nested class for casting HypoidGearModalAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis",
            parent: "HypoidGearModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis",
        ):
            return self._parent._cast(_4573.AGMAGleasonConicalGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.ConicalGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.GearModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis",
        ) -> "HypoidGearModalAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2531.HypoidGear":
        """mastapy.system_model.part_model.gears.HypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6902.HypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2762.HypoidGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.HypoidGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HypoidGearModalAnalysis._Cast_HypoidGearModalAnalysis":
        return self._Cast_HypoidGearModalAnalysis(self)
