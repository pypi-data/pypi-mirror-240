"""CoaxialConnectionCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5622
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2266
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5399


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundMultibodyDynamicsAnalysis")


class CoaxialConnectionCompoundMultibodyDynamicsAnalysis(
    _5622.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
):
    """CoaxialConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CoaxialConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5622.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5528,
            )

            return self._parent._cast(
                _5528.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(_5560.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5569,
            )

            return self._parent._cast(
                _5569.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "CoaxialConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis",
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
        self: Self,
        instance_to_wrap: "CoaxialConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2266.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2266.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5399.CoaxialConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CoaxialConnectionMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5399.CoaxialConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CoaxialConnectionMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CoaxialConnectionCompoundMultibodyDynamicsAnalysis._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CoaxialConnectionCompoundMultibodyDynamicsAnalysis(self)
