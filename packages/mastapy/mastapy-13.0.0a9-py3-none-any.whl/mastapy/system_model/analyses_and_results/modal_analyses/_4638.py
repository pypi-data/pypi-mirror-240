"""InterMountableComponentConnectionModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4603
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "InterMountableComponentConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2278
    from mastapy.system_model.analyses_and_results.system_deflections import _2764


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionModalAnalysis",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionModalAnalysis")


class InterMountableComponentConnectionModalAnalysis(_4603.ConnectionModalAnalysis):
    """InterMountableComponentConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionModalAnalysis"
    )

    class _Cast_InterMountableComponentConnectionModalAnalysis:
        """Special nested class for casting InterMountableComponentConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
            parent: "InterMountableComponentConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            return self._parent._cast(_4603.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4572

            return self._parent._cast(_4572.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def belt_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4577

            return self._parent._cast(_4577.BeltConnectionModalAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4579

            return self._parent._cast(_4579.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4584

            return self._parent._cast(_4584.BevelGearMeshModalAnalysis)

        @property
        def clutch_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4589

            return self._parent._cast(_4589.ClutchConnectionModalAnalysis)

        @property
        def concept_coupling_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.ConceptCouplingConnectionModalAnalysis)

        @property
        def concept_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ConceptGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4600

            return self._parent._cast(_4600.ConicalGearMeshModalAnalysis)

        @property
        def coupling_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606

            return self._parent._cast(_4606.CouplingConnectionModalAnalysis)

        @property
        def cvt_belt_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.CVTBeltConnectionModalAnalysis)

        @property
        def cylindrical_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616

            return self._parent._cast(_4616.CylindricalGearMeshModalAnalysis)

        @property
        def face_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625

            return self._parent._cast(_4625.FaceGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4631

            return self._parent._cast(_4631.GearMeshModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.HypoidGearMeshModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(
                _4639.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642

            return self._parent._cast(
                _4642.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4645

            return self._parent._cast(
                _4645.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4659

            return self._parent._cast(
                _4659.PartToPartShearCouplingConnectionModalAnalysis
            )

        @property
        def ring_pins_to_disc_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4669

            return self._parent._cast(_4669.RingPinsToDiscConnectionModalAnalysis)

        @property
        def rolling_ring_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(_4671.RollingRingConnectionModalAnalysis)

        @property
        def spiral_bevel_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.SpiralBevelGearMeshModalAnalysis)

        @property
        def spring_damper_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4682

            return self._parent._cast(_4682.SpringDamperConnectionModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688

            return self._parent._cast(_4688.StraightBevelGearMeshModalAnalysis)

        @property
        def torque_converter_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.TorqueConverterConnectionModalAnalysis)

        @property
        def worm_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4706

            return self._parent._cast(_4706.WormGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4709

            return self._parent._cast(_4709.ZerolBevelGearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
        ) -> "InterMountableComponentConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2278.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2764.InterMountableComponentConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.InterMountableComponentConnectionSystemDeflection

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
    ) -> "InterMountableComponentConnectionModalAnalysis._Cast_InterMountableComponentConnectionModalAnalysis":
        return self._Cast_InterMountableComponentConnectionModalAnalysis(self)
