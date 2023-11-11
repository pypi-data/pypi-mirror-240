"""SpringDamperConnectionModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4606
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SpringDamperConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2347
    from mastapy.system_model.analyses_and_results.static_loads import _6953
    from mastapy.system_model.analyses_and_results.system_deflections import _2807


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnectionModalAnalysis",)


Self = TypeVar("Self", bound="SpringDamperConnectionModalAnalysis")


class SpringDamperConnectionModalAnalysis(_4606.CouplingConnectionModalAnalysis):
    """SpringDamperConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperConnectionModalAnalysis")

    class _Cast_SpringDamperConnectionModalAnalysis:
        """Special nested class for casting SpringDamperConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperConnectionModalAnalysis._Cast_SpringDamperConnectionModalAnalysis",
            parent: "SpringDamperConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_modal_analysis(
            self: "SpringDamperConnectionModalAnalysis._Cast_SpringDamperConnectionModalAnalysis",
        ):
            return self._parent._cast(_4606.CouplingConnectionModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "SpringDamperConnectionModalAnalysis._Cast_SpringDamperConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(
                _4638.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "SpringDamperConnectionModalAnalysis._Cast_SpringDamperConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpringDamperConnectionModalAnalysis._Cast_SpringDamperConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpringDamperConnectionModalAnalysis._Cast_SpringDamperConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpringDamperConnectionModalAnalysis._Cast_SpringDamperConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperConnectionModalAnalysis._Cast_SpringDamperConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperConnectionModalAnalysis._Cast_SpringDamperConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def spring_damper_connection_modal_analysis(
            self: "SpringDamperConnectionModalAnalysis._Cast_SpringDamperConnectionModalAnalysis",
        ) -> "SpringDamperConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnectionModalAnalysis._Cast_SpringDamperConnectionModalAnalysis",
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
        self: Self, instance_to_wrap: "SpringDamperConnectionModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2347.SpringDamperConnection":
        """mastapy.system_model.connections_and_sockets.couplings.SpringDamperConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6953.SpringDamperConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2807.SpringDamperConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SpringDamperConnectionSystemDeflection

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
    ) -> (
        "SpringDamperConnectionModalAnalysis._Cast_SpringDamperConnectionModalAnalysis"
    ):
        return self._Cast_SpringDamperConnectionModalAnalysis(self)
