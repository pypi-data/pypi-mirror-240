"""ConnectorModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4654
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ConnectorModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2444
    from mastapy.system_model.analyses_and_results.system_deflections import _2725


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorModalAnalysis",)


Self = TypeVar("Self", bound="ConnectorModalAnalysis")


class ConnectorModalAnalysis(_4654.MountableComponentModalAnalysis):
    """ConnectorModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorModalAnalysis")

    class _Cast_ConnectorModalAnalysis:
        """Special nested class for casting ConnectorModalAnalysis to subclasses."""

        def __init__(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
            parent: "ConnectorModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ):
            return self._parent._cast(_4654.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bearing_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4576

            return self._parent._cast(_4576.BearingModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4656

            return self._parent._cast(_4656.OilSealModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(_4674.ShaftHubConnectionModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis",
        ) -> "ConnectorModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2444.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2725.ConnectorSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConnectorSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConnectorModalAnalysis._Cast_ConnectorModalAnalysis":
        return self._Cast_ConnectorModalAnalysis(self)
