"""InterMountableComponentConnectionCompoundCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6706,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
        "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6607


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundCriticalSpeedAnalysis"
)


class InterMountableComponentConnectionCompoundCriticalSpeedAnalysis(
    _6706.ConnectionCompoundCriticalSpeedAnalysis
):
    """InterMountableComponentConnectionCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
            parent: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6706.ConnectionCompoundCriticalSpeedAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6676,
            )

            return self._parent._cast(
                _6676.AGMAGleasonConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def belt_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6680,
            )

            return self._parent._cast(_6680.BeltConnectionCompoundCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6683,
            )

            return self._parent._cast(
                _6683.BevelDifferentialGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6688,
            )

            return self._parent._cast(_6688.BevelGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def clutch_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6693,
            )

            return self._parent._cast(
                _6693.ClutchConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_coupling_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6698,
            )

            return self._parent._cast(
                _6698.ConceptCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def concept_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6701,
            )

            return self._parent._cast(
                _6701.ConceptGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6704,
            )

            return self._parent._cast(
                _6704.ConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def coupling_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(
                _6709.CouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cvt_belt_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6711,
            )

            return self._parent._cast(
                _6711.CVTBeltConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6719,
            )

            return self._parent._cast(
                _6719.CylindricalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6725,
            )

            return self._parent._cast(_6725.FaceGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6730,
            )

            return self._parent._cast(_6730.GearMeshCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6734,
            )

            return self._parent._cast(_6734.HypoidGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6738,
            )

            return self._parent._cast(
                _6738.KlingelnbergCycloPalloidConicalGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6741,
            )

            return self._parent._cast(
                _6741.KlingelnbergCycloPalloidHypoidGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6744,
            )

            return self._parent._cast(
                _6744.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6752,
            )

            return self._parent._cast(
                _6752.PartToPartShearCouplingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(
                _6761.RingPinsToDiscConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def rolling_ring_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6764,
            )

            return self._parent._cast(
                _6764.RollingRingConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6771,
            )

            return self._parent._cast(
                _6771.SpiralBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6774,
            )

            return self._parent._cast(
                _6774.SpringDamperConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6777,
            )

            return self._parent._cast(
                _6777.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(
                _6780.StraightBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def torque_converter_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6789,
            )

            return self._parent._cast(
                _6789.TorqueConverterConnectionCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6795,
            )

            return self._parent._cast(_6795.WormGearMeshCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6798,
            )

            return self._parent._cast(
                _6798.ZerolBevelGearMeshCompoundCriticalSpeedAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_critical_speed_analysis(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
        ) -> "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6607.InterMountableComponentConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.InterMountableComponentConnectionCriticalSpeedAnalysis]

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
    ) -> "List[_6607.InterMountableComponentConnectionCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.InterMountableComponentConnectionCriticalSpeedAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundCriticalSpeedAnalysis._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis":
        return (
            self._Cast_InterMountableComponentConnectionCompoundCriticalSpeedAnalysis(
                self
            )
        )
