"""CouplingConnectionCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6607
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CouplingConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2343


__docformat__ = "restructuredtext en"
__all__ = ("CouplingConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CouplingConnectionCriticalSpeedAnalysis")


class CouplingConnectionCriticalSpeedAnalysis(
    _6607.InterMountableComponentConnectionCriticalSpeedAnalysis
):
    """CouplingConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingConnectionCriticalSpeedAnalysis"
    )

    class _Cast_CouplingConnectionCriticalSpeedAnalysis:
        """Special nested class for casting CouplingConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
            parent: "CouplingConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
        ):
            return self._parent._cast(
                _6607.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6574,
            )

            return self._parent._cast(_6574.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_connection_critical_speed_analysis(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6560,
            )

            return self._parent._cast(_6560.ClutchConnectionCriticalSpeedAnalysis)

        @property
        def concept_coupling_connection_critical_speed_analysis(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6565,
            )

            return self._parent._cast(
                _6565.ConceptCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_critical_speed_analysis(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6622,
            )

            return self._parent._cast(
                _6622.PartToPartShearCouplingConnectionCriticalSpeedAnalysis
            )

        @property
        def spring_damper_connection_critical_speed_analysis(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.SpringDamperConnectionCriticalSpeedAnalysis)

        @property
        def torque_converter_connection_critical_speed_analysis(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6659,
            )

            return self._parent._cast(
                _6659.TorqueConverterConnectionCriticalSpeedAnalysis
            )

        @property
        def coupling_connection_critical_speed_analysis(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
        ) -> "CouplingConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CouplingConnectionCriticalSpeedAnalysis.TYPE"
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
    ) -> "CouplingConnectionCriticalSpeedAnalysis._Cast_CouplingConnectionCriticalSpeedAnalysis":
        return self._Cast_CouplingConnectionCriticalSpeedAnalysis(self)
