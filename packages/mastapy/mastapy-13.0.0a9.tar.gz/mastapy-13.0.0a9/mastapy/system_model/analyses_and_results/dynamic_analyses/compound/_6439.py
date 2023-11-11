"""ConnectionCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7535
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ConnectionCompoundDynamicAnalysis")


class ConnectionCompoundDynamicAnalysis(_7535.ConnectionCompoundAnalysis):
    """ConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionCompoundDynamicAnalysis")

    class _Cast_ConnectionCompoundDynamicAnalysis:
        """Special nested class for casting ConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
            parent: "ConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6407,
            )

            return self._parent._cast(
                _6407.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6409,
            )

            return self._parent._cast(
                _6409.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def belt_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6413,
            )

            return self._parent._cast(_6413.BeltConnectionCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6416,
            )

            return self._parent._cast(
                _6416.BevelDifferentialGearMeshCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6421,
            )

            return self._parent._cast(_6421.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def clutch_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6426,
            )

            return self._parent._cast(_6426.ClutchConnectionCompoundDynamicAnalysis)

        @property
        def coaxial_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6428,
            )

            return self._parent._cast(_6428.CoaxialConnectionCompoundDynamicAnalysis)

        @property
        def concept_coupling_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6431,
            )

            return self._parent._cast(
                _6431.ConceptCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def concept_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6434,
            )

            return self._parent._cast(_6434.ConceptGearMeshCompoundDynamicAnalysis)

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6437,
            )

            return self._parent._cast(_6437.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def coupling_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6442,
            )

            return self._parent._cast(_6442.CouplingConnectionCompoundDynamicAnalysis)

        @property
        def cvt_belt_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6444,
            )

            return self._parent._cast(_6444.CVTBeltConnectionCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6448,
            )

            return self._parent._cast(
                _6448.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6450,
            )

            return self._parent._cast(
                _6450.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6452,
            )

            return self._parent._cast(_6452.CylindricalGearMeshCompoundDynamicAnalysis)

        @property
        def face_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6458,
            )

            return self._parent._cast(_6458.FaceGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6463,
            )

            return self._parent._cast(_6463.GearMeshCompoundDynamicAnalysis)

        @property
        def hypoid_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.HypoidGearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6469,
            )

            return self._parent._cast(
                _6469.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6471,
            )

            return self._parent._cast(
                _6471.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(
                _6474.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6477,
            )

            return self._parent._cast(
                _6477.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6485,
            )

            return self._parent._cast(
                _6485.PartToPartShearCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def planetary_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.PlanetaryConnectionCompoundDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(
                _6494.RingPinsToDiscConnectionCompoundDynamicAnalysis
            )

        @property
        def rolling_ring_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6497,
            )

            return self._parent._cast(
                _6497.RollingRingConnectionCompoundDynamicAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6501,
            )

            return self._parent._cast(
                _6501.ShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6504,
            )

            return self._parent._cast(_6504.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def spring_damper_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6507,
            )

            return self._parent._cast(
                _6507.SpringDamperConnectionCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6510,
            )

            return self._parent._cast(
                _6510.StraightBevelDiffGearMeshCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(
                _6513.StraightBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def torque_converter_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6522,
            )

            return self._parent._cast(
                _6522.TorqueConverterConnectionCompoundDynamicAnalysis
            )

        @property
        def worm_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6528,
            )

            return self._parent._cast(_6528.WormGearMeshCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6531,
            )

            return self._parent._cast(_6531.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "ConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "ConnectionCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6308.ConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectionDynamicAnalysis]

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
    ) -> "List[_6308.ConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectionDynamicAnalysis]

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
    ) -> "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis":
        return self._Cast_ConnectionCompoundDynamicAnalysis(self)
