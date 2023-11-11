"""ClutchConnectionAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7045,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2339
    from mastapy.system_model.analyses_and_results.static_loads import _6829
    from mastapy.system_model.analyses_and_results.system_deflections import _2708


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="ClutchConnectionAdvancedTimeSteppingAnalysisForModulation"
)


class ClutchConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7045.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """ClutchConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ClutchConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7045.CouplingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7073,
            )

            return self._parent._cast(
                _7073.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7042,
            )

            return self._parent._cast(
                _7042.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2339.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6829.ClutchConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchConnectionLoadCase

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
    ) -> "_2708.ClutchConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ClutchConnectionSystemDeflection

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
    ) -> "ClutchConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ClutchConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
