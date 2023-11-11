"""VirtualComponentModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4654
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "VirtualComponentModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476
    from mastapy.system_model.analyses_and_results.system_deflections import _2832


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentModalAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentModalAnalysis")


class VirtualComponentModalAnalysis(_4654.MountableComponentModalAnalysis):
    """VirtualComponentModalAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentModalAnalysis")

    class _Cast_VirtualComponentModalAnalysis:
        """Special nested class for casting VirtualComponentModalAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
            parent: "VirtualComponentModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ):
            return self._parent._cast(_4654.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def mass_disc_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4648

            return self._parent._cast(_4648.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649

            return self._parent._cast(_4649.MeasurementComponentModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665

            return self._parent._cast(_4665.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.PowerLoadModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
        ) -> "VirtualComponentModalAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2476.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2832.VirtualComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection

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
    ) -> "VirtualComponentModalAnalysis._Cast_VirtualComponentModalAnalysis":
        return self._Cast_VirtualComponentModalAnalysis(self)
