"""SpringDamperHalfModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4607
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SpringDamperHalfModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.static_loads import _6954
    from mastapy.system_model.analyses_and_results.system_deflections import _2808


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperHalfModalAnalysis",)


Self = TypeVar("Self", bound="SpringDamperHalfModalAnalysis")


class SpringDamperHalfModalAnalysis(_4607.CouplingHalfModalAnalysis):
    """SpringDamperHalfModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperHalfModalAnalysis")

    class _Cast_SpringDamperHalfModalAnalysis:
        """Special nested class for casting SpringDamperHalfModalAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
            parent: "SpringDamperHalfModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ):
            return self._parent._cast(_4607.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
        ) -> "SpringDamperHalfModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperHalfModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2598.SpringDamperHalf":
        """mastapy.system_model.part_model.couplings.SpringDamperHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6954.SpringDamperHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2808.SpringDamperHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpringDamperHalfSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperHalfModalAnalysis._Cast_SpringDamperHalfModalAnalysis":
        return self._Cast_SpringDamperHalfModalAnalysis(self)
