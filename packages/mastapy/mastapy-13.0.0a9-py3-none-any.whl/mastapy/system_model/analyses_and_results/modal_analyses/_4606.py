"""CouplingConnectionModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4638
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CouplingConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2343
    from mastapy.system_model.analyses_and_results.system_deflections import _2726


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionModalAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionModalAnalysis")


class CouplingConnectionModalAnalysis(
    _4638.InterMountableComponentConnectionModalAnalysis
):
    """CouplingConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionModalAnalysis")

    class _Cast_CouplingConnectionModalAnalysis:
        """Special nested class for casting CouplingConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
            parent: "CouplingConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ):
            return self._parent._cast(
                _4638.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4603

            return self._parent._cast(_4603.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4589

            return self._parent._cast(_4589.ClutchConnectionModalAnalysis)

        @property
        def concept_coupling_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.ConceptCouplingConnectionModalAnalysis)

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(
                _4659.PartToPartShearCouplingConnectionModalAnalysis
            )

        @property
        def spring_damper_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4682

            return self._parent._cast(_4682.SpringDamperConnectionModalAnalysis)

        @property
        def torque_converter_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.TorqueConverterConnectionModalAnalysis)

        @property
        def coupling_connection_modal_analysis(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
        ) -> "CouplingConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingConnectionModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2343.CouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.CouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2726.CouplingConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingConnectionSystemDeflection

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
    ) -> "CouplingConnectionModalAnalysis._Cast_CouplingConnectionModalAnalysis":
        return self._Cast_CouplingConnectionModalAnalysis(self)
