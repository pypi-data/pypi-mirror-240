"""InterMountableComponentConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "InterMountableComponentConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2278


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionLoadCase",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionLoadCase")


class InterMountableComponentConnectionLoadCase(_6846.ConnectionLoadCase):
    """InterMountableComponentConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionLoadCase"
    )

    class _Cast_InterMountableComponentConnectionLoadCase:
        """Special nested class for casting InterMountableComponentConnectionLoadCase to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
            parent: "InterMountableComponentConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            return self._parent._cast(_6846.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6811

            return self._parent._cast(_6811.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6817

            return self._parent._cast(_6817.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6820

            return self._parent._cast(_6820.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6825

            return self._parent._cast(_6825.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6829

            return self._parent._cast(_6829.ClutchConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6839

            return self._parent._cast(_6839.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6843

            return self._parent._cast(_6843.ConicalGearMeshLoadCase)

        @property
        def coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.CVTBeltConnectionLoadCase)

        @property
        def cylindrical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6860

            return self._parent._cast(_6860.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6882

            return self._parent._cast(_6882.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6889

            return self._parent._cast(_6889.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6903

            return self._parent._cast(_6903.HypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6910

            return self._parent._cast(
                _6910.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6913

            return self._parent._cast(
                _6913.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6916

            return self._parent._cast(
                _6916.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.PartToPartShearCouplingConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(_6941.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6943

            return self._parent._cast(_6943.RollingRingConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6969

            return self._parent._cast(_6969.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6980

            return self._parent._cast(_6980.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.ZerolBevelGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "InterMountableComponentConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
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
        self: Self, instance_to_wrap: "InterMountableComponentConnectionLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AdditionalModalDampingRatio = value

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
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase":
        return self._Cast_InterMountableComponentConnectionLoadCase(self)
