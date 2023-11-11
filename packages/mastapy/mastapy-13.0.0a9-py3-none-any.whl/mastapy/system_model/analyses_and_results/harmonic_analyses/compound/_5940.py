"""InterMountableComponentConnectionCompoundHarmonicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5910
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "InterMountableComponentConnectionCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5770


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundHarmonicAnalysis"
)


class InterMountableComponentConnectionCompoundHarmonicAnalysis(
    _5910.ConnectionCompoundHarmonicAnalysis
):
    """InterMountableComponentConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
            parent: "InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            return self._parent._cast(_5910.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5880,
            )

            return self._parent._cast(
                _5880.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def belt_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5884,
            )

            return self._parent._cast(_5884.BeltConnectionCompoundHarmonicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5887,
            )

            return self._parent._cast(
                _5887.BevelDifferentialGearMeshCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5892,
            )

            return self._parent._cast(_5892.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def clutch_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5897,
            )

            return self._parent._cast(_5897.ClutchConnectionCompoundHarmonicAnalysis)

        @property
        def concept_coupling_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5902,
            )

            return self._parent._cast(
                _5902.ConceptCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def concept_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5905,
            )

            return self._parent._cast(_5905.ConceptGearMeshCompoundHarmonicAnalysis)

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5908,
            )

            return self._parent._cast(_5908.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def coupling_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5913,
            )

            return self._parent._cast(_5913.CouplingConnectionCompoundHarmonicAnalysis)

        @property
        def cvt_belt_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5915,
            )

            return self._parent._cast(_5915.CVTBeltConnectionCompoundHarmonicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5923,
            )

            return self._parent._cast(_5923.CylindricalGearMeshCompoundHarmonicAnalysis)

        @property
        def face_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5929,
            )

            return self._parent._cast(_5929.FaceGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5934,
            )

            return self._parent._cast(_5934.GearMeshCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5938,
            )

            return self._parent._cast(_5938.HypoidGearMeshCompoundHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5942,
            )

            return self._parent._cast(
                _5942.KlingelnbergCycloPalloidConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5945,
            )

            return self._parent._cast(
                _5945.KlingelnbergCycloPalloidHypoidGearMeshCompoundHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5948,
            )

            return self._parent._cast(
                _5948.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5956,
            )

            return self._parent._cast(
                _5956.PartToPartShearCouplingConnectionCompoundHarmonicAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5965,
            )

            return self._parent._cast(
                _5965.RingPinsToDiscConnectionCompoundHarmonicAnalysis
            )

        @property
        def rolling_ring_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5968,
            )

            return self._parent._cast(
                _5968.RollingRingConnectionCompoundHarmonicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5975,
            )

            return self._parent._cast(_5975.SpiralBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def spring_damper_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5978,
            )

            return self._parent._cast(
                _5978.SpringDamperConnectionCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5981,
            )

            return self._parent._cast(
                _5981.StraightBevelDiffGearMeshCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(
                _5984.StraightBevelGearMeshCompoundHarmonicAnalysis
            )

        @property
        def torque_converter_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5993,
            )

            return self._parent._cast(
                _5993.TorqueConverterConnectionCompoundHarmonicAnalysis
            )

        @property
        def worm_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5999,
            )

            return self._parent._cast(_5999.WormGearMeshCompoundHarmonicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6002,
            )

            return self._parent._cast(_6002.ZerolBevelGearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
        ) -> "InterMountableComponentConnectionCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5770.InterMountableComponentConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.InterMountableComponentConnectionHarmonicAnalysis]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5770.InterMountableComponentConnectionHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.InterMountableComponentConnectionHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionCompoundHarmonicAnalysis._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis":
        return self._Cast_InterMountableComponentConnectionCompoundHarmonicAnalysis(
            self
        )
