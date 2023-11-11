"""ConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2646
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConnectionLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2269
    from mastapy.system_model.analyses_and_results.static_loads import _6801, _6802


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionLoadCase",)


Self = TypeVar("Self", bound="ConnectionLoadCase")


class ConnectionLoadCase(_2646.ConnectionAnalysis):
    """ConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _CONNECTION_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionLoadCase")

    class _Cast_ConnectionLoadCase:
        """Special nested class for casting ConnectionLoadCase to subclasses."""

        def __init__(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
            parent: "ConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def connection_analysis(self: "ConnectionLoadCase._Cast_ConnectionLoadCase"):
            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "ConnectionLoadCase._Cast_ConnectionLoadCase"):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6806

            return self._parent._cast(
                _6806.AbstractShaftToMountableComponentConnectionLoadCase
            )

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6811

            return self._parent._cast(_6811.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6817

            return self._parent._cast(_6817.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6820

            return self._parent._cast(_6820.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6825

            return self._parent._cast(_6825.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6829

            return self._parent._cast(_6829.ClutchConnectionLoadCase)

        @property
        def coaxial_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.CoaxialConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6839

            return self._parent._cast(_6839.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6843

            return self._parent._cast(_6843.ConicalGearMeshLoadCase)

        @property
        def coupling_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6848

            return self._parent._cast(_6848.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.CVTBeltConnectionLoadCase)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(
                _6855.CycloidalDiscCentralBearingConnectionLoadCase
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(
                _6857.CycloidalDiscPlanetaryBearingConnectionLoadCase
            )

        @property
        def cylindrical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6860

            return self._parent._cast(_6860.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6882

            return self._parent._cast(_6882.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(self: "ConnectionLoadCase._Cast_ConnectionLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6889

            return self._parent._cast(_6889.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6903

            return self._parent._cast(_6903.HypoidGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6908

            return self._parent._cast(_6908.InterMountableComponentConnectionLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6910

            return self._parent._cast(
                _6910.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6913

            return self._parent._cast(
                _6913.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6916

            return self._parent._cast(
                _6916.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6926

            return self._parent._cast(_6926.PartToPartShearCouplingConnectionLoadCase)

        @property
        def planetary_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PlanetaryConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(_6941.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6943

            return self._parent._cast(_6943.RollingRingConnectionLoadCase)

        @property
        def shaft_to_mountable_component_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.ShaftToMountableComponentConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6969

            return self._parent._cast(_6969.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6980

            return self._parent._cast(_6980.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.ZerolBevelGearMeshLoadCase)

        @property
        def connection_load_case(
            self: "ConnectionLoadCase._Cast_ConnectionLoadCase",
        ) -> "ConnectionLoadCase":
            return self._parent

        def __getattr__(self: "ConnectionLoadCase._Cast_ConnectionLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2269.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2269.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def static_load_case(self: Self) -> "_6801.StaticLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StaticLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StaticLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def time_series_load_case(self: Self) -> "_6802.TimeSeriesLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TimeSeriesLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConnectionLoadCase._Cast_ConnectionLoadCase":
        return self._Cast_ConnectionLoadCase(self)
