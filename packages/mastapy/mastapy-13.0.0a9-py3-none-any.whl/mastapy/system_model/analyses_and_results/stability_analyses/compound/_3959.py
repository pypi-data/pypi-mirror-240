"""InterMountableComponentConnectionCompoundStabilityAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3929
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "InterMountableComponentConnectionCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3827


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundStabilityAnalysis"
)


class InterMountableComponentConnectionCompoundStabilityAnalysis(
    _3929.ConnectionCompoundStabilityAnalysis
):
    """InterMountableComponentConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundStabilityAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
            parent: "InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            return self._parent._cast(_3929.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3899,
            )

            return self._parent._cast(
                _3899.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def belt_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3903,
            )

            return self._parent._cast(_3903.BeltConnectionCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3906,
            )

            return self._parent._cast(
                _3906.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3911,
            )

            return self._parent._cast(_3911.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def clutch_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3916,
            )

            return self._parent._cast(_3916.ClutchConnectionCompoundStabilityAnalysis)

        @property
        def concept_coupling_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3921,
            )

            return self._parent._cast(
                _3921.ConceptCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def concept_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(_3924.ConceptGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3927,
            )

            return self._parent._cast(_3927.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def coupling_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3932,
            )

            return self._parent._cast(_3932.CouplingConnectionCompoundStabilityAnalysis)

        @property
        def cvt_belt_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3934,
            )

            return self._parent._cast(_3934.CVTBeltConnectionCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3942,
            )

            return self._parent._cast(
                _3942.CylindricalGearMeshCompoundStabilityAnalysis
            )

        @property
        def face_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(_3948.FaceGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.GearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3961,
            )

            return self._parent._cast(
                _3961.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(
                _3964.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(
                _3967.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3975,
            )

            return self._parent._cast(
                _3975.PartToPartShearCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(
                _3984.RingPinsToDiscConnectionCompoundStabilityAnalysis
            )

        @property
        def rolling_ring_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3987,
            )

            return self._parent._cast(
                _3987.RollingRingConnectionCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(
                _3994.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def spring_damper_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(
                _3997.SpringDamperConnectionCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4000,
            )

            return self._parent._cast(
                _4000.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(
                _4003.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def torque_converter_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4012,
            )

            return self._parent._cast(
                _4012.TorqueConverterConnectionCompoundStabilityAnalysis
            )

        @property
        def worm_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(_4018.WormGearMeshCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
        ) -> "InterMountableComponentConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3827.InterMountableComponentConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.InterMountableComponentConnectionStabilityAnalysis]

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
    ) -> "List[_3827.InterMountableComponentConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.InterMountableComponentConnectionStabilityAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundStabilityAnalysis._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis":
        return self._Cast_InterMountableComponentConnectionCompoundStabilityAnalysis(
            self
        )
