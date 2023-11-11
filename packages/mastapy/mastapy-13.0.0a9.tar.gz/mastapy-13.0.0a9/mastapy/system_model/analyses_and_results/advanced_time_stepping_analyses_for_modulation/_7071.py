"""HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7011,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2312
    from mastapy.system_model.analyses_and_results.static_loads import _6903
    from mastapy.system_model.analyses_and_results.system_deflections import _2760


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation")


class HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation(
    _7011.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
):
    """HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
            parent: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            return self._parent._cast(
                _7011.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7040,
            )

            return self._parent._cast(
                _7040.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7066,
            )

            return self._parent._cast(
                _7066.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7073,
            )

            return self._parent._cast(
                _7073.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7042,
            )

            return self._parent._cast(
                _7042.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2312.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6903.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2760.HypoidGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.HypoidGearMeshSystemDeflection

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
    ) -> "HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_HypoidGearMeshAdvancedTimeSteppingAnalysisForModulation(self)
