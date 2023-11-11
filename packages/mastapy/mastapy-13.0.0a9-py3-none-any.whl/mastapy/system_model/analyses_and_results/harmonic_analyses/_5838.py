"""ZerolBevelGearMeshHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5692
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ZerolBevelGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2328
    from mastapy.system_model.analyses_and_results.static_loads import _6983
    from mastapy.system_model.analyses_and_results.system_deflections import _2836


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshHarmonicAnalysis")


class ZerolBevelGearMeshHarmonicAnalysis(_5692.BevelGearMeshHarmonicAnalysis):
    """ZerolBevelGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ZerolBevelGearMeshHarmonicAnalysis")

    class _Cast_ZerolBevelGearMeshHarmonicAnalysis:
        """Special nested class for casting ZerolBevelGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
            parent: "ZerolBevelGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
        ):
            return self._parent._cast(_5692.BevelGearMeshHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5680,
            )

            return self._parent._cast(_5680.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5709,
            )

            return self._parent._cast(_5709.ConicalGearMeshHarmonicAnalysis)

        @property
        def gear_mesh_harmonic_analysis(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5751,
            )

            return self._parent._cast(_5751.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5770,
            )

            return self._parent._cast(
                _5770.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
        ) -> "ZerolBevelGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMeshHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2328.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6983.ZerolBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase

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
    ) -> "_2836.ZerolBevelGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearMeshSystemDeflection

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
    ) -> "ZerolBevelGearMeshHarmonicAnalysis._Cast_ZerolBevelGearMeshHarmonicAnalysis":
        return self._Cast_ZerolBevelGearMeshHarmonicAnalysis(self)
