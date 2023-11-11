"""ConnectorCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5602
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ConnectorCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5411


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConnectorCompoundMultibodyDynamicsAnalysis")


class ConnectorCompoundMultibodyDynamicsAnalysis(
    _5602.MountableComponentCompoundMultibodyDynamicsAnalysis
):
    """ConnectorCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectorCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ConnectorCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ConnectorCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConnectorCompoundMultibodyDynamicsAnalysis._Cast_ConnectorCompoundMultibodyDynamicsAnalysis",
            parent: "ConnectorCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "ConnectorCompoundMultibodyDynamicsAnalysis._Cast_ConnectorCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5602.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "ConnectorCompoundMultibodyDynamicsAnalysis._Cast_ConnectorCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5550,
            )

            return self._parent._cast(_5550.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "ConnectorCompoundMultibodyDynamicsAnalysis._Cast_ConnectorCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5604,
            )

            return self._parent._cast(_5604.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundMultibodyDynamicsAnalysis._Cast_ConnectorCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundMultibodyDynamicsAnalysis._Cast_ConnectorCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundMultibodyDynamicsAnalysis._Cast_ConnectorCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bearing_compound_multibody_dynamics_analysis(
            self: "ConnectorCompoundMultibodyDynamicsAnalysis._Cast_ConnectorCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5533,
            )

            return self._parent._cast(_5533.BearingCompoundMultibodyDynamicsAnalysis)

        @property
        def oil_seal_compound_multibody_dynamics_analysis(
            self: "ConnectorCompoundMultibodyDynamicsAnalysis._Cast_ConnectorCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(_5603.OilSealCompoundMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_compound_multibody_dynamics_analysis(
            self: "ConnectorCompoundMultibodyDynamicsAnalysis._Cast_ConnectorCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5621,
            )

            return self._parent._cast(
                _5621.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connector_compound_multibody_dynamics_analysis(
            self: "ConnectorCompoundMultibodyDynamicsAnalysis._Cast_ConnectorCompoundMultibodyDynamicsAnalysis",
        ) -> "ConnectorCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundMultibodyDynamicsAnalysis._Cast_ConnectorCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ConnectorCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5411.ConnectorMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConnectorMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5411.ConnectorMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConnectorMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorCompoundMultibodyDynamicsAnalysis._Cast_ConnectorCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ConnectorCompoundMultibodyDynamicsAnalysis(self)
