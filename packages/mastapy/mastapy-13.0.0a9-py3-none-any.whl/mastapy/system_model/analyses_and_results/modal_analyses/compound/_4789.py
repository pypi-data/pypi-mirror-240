"""InterMountableComponentConnectionCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4759
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "InterMountableComponentConnectionCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4638


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundModalAnalysis",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionCompoundModalAnalysis")


class InterMountableComponentConnectionCompoundModalAnalysis(
    _4759.ConnectionCompoundModalAnalysis
):
    """InterMountableComponentConnectionCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundModalAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundModalAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
            parent: "InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            return self._parent._cast(_4759.ConnectionCompoundModalAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4729,
            )

            return self._parent._cast(
                _4729.AGMAGleasonConicalGearMeshCompoundModalAnalysis
            )

        @property
        def belt_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4733,
            )

            return self._parent._cast(_4733.BeltConnectionCompoundModalAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4736,
            )

            return self._parent._cast(
                _4736.BevelDifferentialGearMeshCompoundModalAnalysis
            )

        @property
        def bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(_4741.BevelGearMeshCompoundModalAnalysis)

        @property
        def clutch_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4746,
            )

            return self._parent._cast(_4746.ClutchConnectionCompoundModalAnalysis)

        @property
        def concept_coupling_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(
                _4751.ConceptCouplingConnectionCompoundModalAnalysis
            )

        @property
        def concept_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4754,
            )

            return self._parent._cast(_4754.ConceptGearMeshCompoundModalAnalysis)

        @property
        def conical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4757,
            )

            return self._parent._cast(_4757.ConicalGearMeshCompoundModalAnalysis)

        @property
        def coupling_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.CouplingConnectionCompoundModalAnalysis)

        @property
        def cvt_belt_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4764,
            )

            return self._parent._cast(_4764.CVTBeltConnectionCompoundModalAnalysis)

        @property
        def cylindrical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4772,
            )

            return self._parent._cast(_4772.CylindricalGearMeshCompoundModalAnalysis)

        @property
        def face_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4778,
            )

            return self._parent._cast(_4778.FaceGearMeshCompoundModalAnalysis)

        @property
        def gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.GearMeshCompoundModalAnalysis)

        @property
        def hypoid_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4787,
            )

            return self._parent._cast(_4787.HypoidGearMeshCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4791,
            )

            return self._parent._cast(
                _4791.KlingelnbergCycloPalloidConicalGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4794,
            )

            return self._parent._cast(
                _4794.KlingelnbergCycloPalloidHypoidGearMeshCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4797,
            )

            return self._parent._cast(
                _4797.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(
                _4805.PartToPartShearCouplingConnectionCompoundModalAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4814,
            )

            return self._parent._cast(
                _4814.RingPinsToDiscConnectionCompoundModalAnalysis
            )

        @property
        def rolling_ring_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4817,
            )

            return self._parent._cast(_4817.RollingRingConnectionCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4824,
            )

            return self._parent._cast(_4824.SpiralBevelGearMeshCompoundModalAnalysis)

        @property
        def spring_damper_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4827,
            )

            return self._parent._cast(_4827.SpringDamperConnectionCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(
                _4830.StraightBevelDiffGearMeshCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4833,
            )

            return self._parent._cast(_4833.StraightBevelGearMeshCompoundModalAnalysis)

        @property
        def torque_converter_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(
                _4842.TorqueConverterConnectionCompoundModalAnalysis
            )

        @property
        def worm_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4848,
            )

            return self._parent._cast(_4848.WormGearMeshCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4851,
            )

            return self._parent._cast(_4851.ZerolBevelGearMeshCompoundModalAnalysis)

        @property
        def inter_mountable_component_connection_compound_modal_analysis(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
        ) -> "InterMountableComponentConnectionCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4638.InterMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis]

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
    ) -> "List[_4638.InterMountableComponentConnectionModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.InterMountableComponentConnectionModalAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundModalAnalysis._Cast_InterMountableComponentConnectionCompoundModalAnalysis":
        return self._Cast_InterMountableComponentConnectionCompoundModalAnalysis(self)
