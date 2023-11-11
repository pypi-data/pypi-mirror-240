"""MassDiscModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4702
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "MassDiscModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2459
    from mastapy.system_model.analyses_and_results.static_loads import _6918
    from mastapy.system_model.analyses_and_results.system_deflections import _2776


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscModalAnalysis",)


Self = TypeVar("Self", bound="MassDiscModalAnalysis")


class MassDiscModalAnalysis(_4702.VirtualComponentModalAnalysis):
    """MassDiscModalAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscModalAnalysis")

    class _Cast_MassDiscModalAnalysis:
        """Special nested class for casting MassDiscModalAnalysis to subclasses."""

        def __init__(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
            parent: "MassDiscModalAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_modal_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            return self._parent._cast(_4702.VirtualComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def mass_disc_modal_analysis(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis",
        ) -> "MassDiscModalAnalysis":
            return self._parent

        def __getattr__(
            self: "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MassDiscModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2459.MassDisc":
        """mastapy.system_model.part_model.MassDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6918.MassDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2776.MassDiscSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MassDiscSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[MassDiscModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.MassDiscModalAnalysis]

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
    def cast_to(self: Self) -> "MassDiscModalAnalysis._Cast_MassDiscModalAnalysis":
        return self._Cast_MassDiscModalAnalysis(self)
