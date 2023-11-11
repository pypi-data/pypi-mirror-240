"""ConicalGearMeshHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5751
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ConicalGearMeshHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2304
    from mastapy.system_model.analyses_and_results.system_deflections import _2721


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshHarmonicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearMeshHarmonicAnalysis")


class ConicalGearMeshHarmonicAnalysis(_5751.GearMeshHarmonicAnalysis):
    """ConicalGearMeshHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshHarmonicAnalysis")

    class _Cast_ConicalGearMeshHarmonicAnalysis:
        """Special nested class for casting ConicalGearMeshHarmonicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
            parent: "ConicalGearMeshHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            return self._parent._cast(_5751.GearMeshHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5770,
            )

            return self._parent._cast(
                _5770.InterMountableComponentConnectionHarmonicAnalysis
            )

        @property
        def connection_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.ConnectionHarmonicAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5680,
            )

            return self._parent._cast(_5680.AGMAGleasonConicalGearMeshHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.BevelDifferentialGearMeshHarmonicAnalysis)

        @property
        def bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5692,
            )

            return self._parent._cast(_5692.BevelGearMeshHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5768,
            )

            return self._parent._cast(_5768.HypoidGearMeshHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5772,
            )

            return self._parent._cast(
                _5772.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5775,
            )

            return self._parent._cast(
                _5775.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5778,
            )

            return self._parent._cast(
                _5778.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.SpiralBevelGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5816,
            )

            return self._parent._cast(_5816.StraightBevelDiffGearMeshHarmonicAnalysis)

        @property
        def straight_bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5819,
            )

            return self._parent._cast(_5819.StraightBevelGearMeshHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5838,
            )

            return self._parent._cast(_5838.ZerolBevelGearMeshHarmonicAnalysis)

        @property
        def conical_gear_mesh_harmonic_analysis(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
        ) -> "ConicalGearMeshHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2304.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.ConicalGearMeshHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2721.ConicalGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection

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
    ) -> "ConicalGearMeshHarmonicAnalysis._Cast_ConicalGearMeshHarmonicAnalysis":
        return self._Cast_ConicalGearMeshHarmonicAnalysis(self)
