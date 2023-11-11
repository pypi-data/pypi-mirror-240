"""InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5019,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4919,
    )


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness"
)


class InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness(
    _5019.ConnectionCompoundModalAnalysisAtAStiffness
):
    """InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
    )

    class _Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
            parent: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            return self._parent._cast(_5019.ConnectionCompoundModalAnalysisAtAStiffness)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4989,
            )

            return self._parent._cast(
                _4989.AGMAGleasonConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4993,
            )

            return self._parent._cast(
                _4993.BeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(
                _4996.BevelDifferentialGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5001,
            )

            return self._parent._cast(
                _5001.BevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5006,
            )

            return self._parent._cast(
                _5006.ClutchConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5011,
            )

            return self._parent._cast(
                _5011.ConceptCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5014,
            )

            return self._parent._cast(
                _5014.ConceptGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5017,
            )

            return self._parent._cast(
                _5017.ConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(
                _5022.CouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_belt_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5024,
            )

            return self._parent._cast(
                _5024.CVTBeltConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5032,
            )

            return self._parent._cast(
                _5032.CylindricalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5038,
            )

            return self._parent._cast(
                _5038.FaceGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5043,
            )

            return self._parent._cast(_5043.GearMeshCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5047,
            )

            return self._parent._cast(
                _5047.HypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5051,
            )

            return self._parent._cast(
                _5051.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5054,
            )

            return self._parent._cast(
                _5054.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5057,
            )

            return self._parent._cast(
                _5057.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5065,
            )

            return self._parent._cast(
                _5065.PartToPartShearCouplingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5074,
            )

            return self._parent._cast(
                _5074.RingPinsToDiscConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5077,
            )

            return self._parent._cast(
                _5077.RollingRingConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5084,
            )

            return self._parent._cast(
                _5084.SpiralBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5087,
            )

            return self._parent._cast(
                _5087.SpringDamperConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(
                _5090.StraightBevelDiffGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5093,
            )

            return self._parent._cast(
                _5093.StraightBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5102,
            )

            return self._parent._cast(
                _5102.TorqueConverterConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5108,
            )

            return self._parent._cast(
                _5108.WormGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5111,
            )

            return self._parent._cast(
                _5111.ZerolBevelGearMeshCompoundModalAnalysisAtAStiffness
            )

        @property
        def inter_mountable_component_connection_compound_modal_analysis_at_a_stiffness(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
        ) -> "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4919.InterMountableComponentConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.InterMountableComponentConnectionModalAnalysisAtAStiffness]

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
    ) -> "List[_4919.InterMountableComponentConnectionModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.InterMountableComponentConnectionModalAnalysisAtAStiffness]

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
    ) -> "InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness":
        return self._Cast_InterMountableComponentConnectionCompoundModalAnalysisAtAStiffness(
            self
        )
