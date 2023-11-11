"""CouplingConnectionDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CouplingConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2343


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionDynamicAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionDynamicAnalysis")


class CouplingConnectionDynamicAnalysis(
    _6340.InterMountableComponentConnectionDynamicAnalysis
):
    """CouplingConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingConnectionDynamicAnalysis")

    class _Cast_CouplingConnectionDynamicAnalysis:
        """Special nested class for casting CouplingConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
            parent: "CouplingConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ):
            return self._parent._cast(
                _6340.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_connection_dynamic_analysis(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294

            return self._parent._cast(_6294.ClutchConnectionDynamicAnalysis)

        @property
        def concept_coupling_connection_dynamic_analysis(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.ConceptCouplingConnectionDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_connection_dynamic_analysis(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(
                _6355.PartToPartShearCouplingConnectionDynamicAnalysis
            )

        @property
        def spring_damper_connection_dynamic_analysis(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.SpringDamperConnectionDynamicAnalysis)

        @property
        def torque_converter_connection_dynamic_analysis(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.TorqueConverterConnectionDynamicAnalysis)

        @property
        def coupling_connection_dynamic_analysis(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
        ) -> "CouplingConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis",
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
        self: Self, instance_to_wrap: "CouplingConnectionDynamicAnalysis.TYPE"
    ):
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
    def cast_to(
        self: Self,
    ) -> "CouplingConnectionDynamicAnalysis._Cast_CouplingConnectionDynamicAnalysis":
        return self._Cast_CouplingConnectionDynamicAnalysis(self)
