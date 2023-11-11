"""ConnectionCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7535
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ConnectionCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2724


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ConnectionCompoundSystemDeflection")


class ConnectionCompoundSystemDeflection(_7535.ConnectionCompoundAnalysis):
    """ConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionCompoundSystemDeflection")

    class _Cast_ConnectionCompoundSystemDeflection:
        """Special nested class for casting ConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
            parent: "ConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2851,
            )

            return self._parent._cast(
                _2851.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2853,
            )

            return self._parent._cast(
                _2853.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def belt_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2857,
            )

            return self._parent._cast(_2857.BeltConnectionCompoundSystemDeflection)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2860,
            )

            return self._parent._cast(
                _2860.BevelDifferentialGearMeshCompoundSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2865,
            )

            return self._parent._cast(_2865.BevelGearMeshCompoundSystemDeflection)

        @property
        def clutch_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2870,
            )

            return self._parent._cast(_2870.ClutchConnectionCompoundSystemDeflection)

        @property
        def coaxial_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2872,
            )

            return self._parent._cast(_2872.CoaxialConnectionCompoundSystemDeflection)

        @property
        def concept_coupling_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2875,
            )

            return self._parent._cast(
                _2875.ConceptCouplingConnectionCompoundSystemDeflection
            )

        @property
        def concept_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2878,
            )

            return self._parent._cast(_2878.ConceptGearMeshCompoundSystemDeflection)

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2881,
            )

            return self._parent._cast(_2881.ConicalGearMeshCompoundSystemDeflection)

        @property
        def coupling_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2886,
            )

            return self._parent._cast(_2886.CouplingConnectionCompoundSystemDeflection)

        @property
        def cvt_belt_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2888,
            )

            return self._parent._cast(_2888.CVTBeltConnectionCompoundSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2892,
            )

            return self._parent._cast(
                _2892.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2894,
            )

            return self._parent._cast(
                _2894.CycloidalDiscPlanetaryBearingConnectionCompoundSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2896,
            )

            return self._parent._cast(_2896.CylindricalGearMeshCompoundSystemDeflection)

        @property
        def face_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2903,
            )

            return self._parent._cast(_2903.FaceGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2908,
            )

            return self._parent._cast(_2908.GearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2912,
            )

            return self._parent._cast(_2912.HypoidGearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2914,
            )

            return self._parent._cast(
                _2914.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2916,
            )

            return self._parent._cast(
                _2916.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2919,
            )

            return self._parent._cast(
                _2919.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2922,
            )

            return self._parent._cast(
                _2922.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2930,
            )

            return self._parent._cast(
                _2930.PartToPartShearCouplingConnectionCompoundSystemDeflection
            )

        @property
        def planetary_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(_2932.PlanetaryConnectionCompoundSystemDeflection)

        @property
        def ring_pins_to_disc_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(
                _2939.RingPinsToDiscConnectionCompoundSystemDeflection
            )

        @property
        def rolling_ring_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2942,
            )

            return self._parent._cast(
                _2942.RollingRingConnectionCompoundSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2947,
            )

            return self._parent._cast(
                _2947.ShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def spring_damper_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2953,
            )

            return self._parent._cast(
                _2953.SpringDamperConnectionCompoundSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2956,
            )

            return self._parent._cast(
                _2956.StraightBevelDiffGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(
                _2959.StraightBevelGearMeshCompoundSystemDeflection
            )

        @property
        def torque_converter_connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2968,
            )

            return self._parent._cast(
                _2968.TorqueConverterConnectionCompoundSystemDeflection
            )

        @property
        def worm_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.WormGearMeshCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(_2977.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def connection_compound_system_deflection(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
        ) -> "ConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ConnectionCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2724.ConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection]

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
    ) -> "List[_2724.ConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection]

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
    ) -> "ConnectionCompoundSystemDeflection._Cast_ConnectionCompoundSystemDeflection":
        return self._Cast_ConnectionCompoundSystemDeflection(self)
