"""AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5410
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2262


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
)


class AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis(
    _5410.ConnectionMultibodyDynamicsAnalysis
):
    """AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5410.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7538

            return self._parent._cast(_7538.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399

            return self._parent._cast(_5399.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(
                _5419.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(
                _5421.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5467

            return self._parent._cast(
                _5467.PlanetaryConnectionMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5483

            return self._parent._cast(
                _5483.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2262.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

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
    ) -> "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis(
            self
        )
