"""AbstractShaftToMountableComponentConnectionDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AbstractShaftToMountableComponentConnectionDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2262


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionDynamicAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionDynamicAnalysis"
)


class AbstractShaftToMountableComponentConnectionDynamicAnalysis(
    _6308.ConnectionDynamicAnalysis
):
    """AbstractShaftToMountableComponentConnectionDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            return self._parent._cast(_6308.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6297

            return self._parent._cast(_6297.CoaxialConnectionDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(
                _6317.CycloidalDiscCentralBearingConnectionDynamicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6319

            return self._parent._cast(
                _6319.CycloidalDiscPlanetaryBearingConnectionDynamicAnalysis
            )

        @property
        def planetary_connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.PlanetaryConnectionDynamicAnalysis)

        @property
        def shaft_to_mountable_component_connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372

            return self._parent._cast(
                _6372.ShaftToMountableComponentConnectionDynamicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_dynamic_analysis(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionDynamicAnalysis.TYPE",
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
    ) -> "AbstractShaftToMountableComponentConnectionDynamicAnalysis._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionDynamicAnalysis(
            self
        )
