"""ConnectionCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7535
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7304,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConnectionCompoundAdvancedSystemDeflection")


class ConnectionCompoundAdvancedSystemDeflection(_7535.ConnectionCompoundAnalysis):
    """ConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConnectionCompoundAdvancedSystemDeflection"
    )

    class _Cast_ConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
            parent: "ConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7405,
            )

            return self._parent._cast(
                _7405.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7407,
            )

            return self._parent._cast(
                _7407.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def belt_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7411,
            )

            return self._parent._cast(
                _7411.BeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7414,
            )

            return self._parent._cast(
                _7414.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7419,
            )

            return self._parent._cast(
                _7419.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def clutch_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7424,
            )

            return self._parent._cast(
                _7424.ClutchConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def coaxial_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7426,
            )

            return self._parent._cast(
                _7426.CoaxialConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def concept_coupling_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7429,
            )

            return self._parent._cast(
                _7429.ConceptCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7432,
            )

            return self._parent._cast(
                _7432.ConceptGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7435,
            )

            return self._parent._cast(
                _7435.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7440,
            )

            return self._parent._cast(
                _7440.CouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_belt_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(
                _7442.CVTBeltConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7446,
            )

            return self._parent._cast(
                _7446.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7448,
            )

            return self._parent._cast(
                _7448.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7450,
            )

            return self._parent._cast(
                _7450.CylindricalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7456,
            )

            return self._parent._cast(
                _7456.FaceGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7461,
            )

            return self._parent._cast(_7461.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(
                _7465.HypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7467,
            )

            return self._parent._cast(
                _7467.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7469,
            )

            return self._parent._cast(
                _7469.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7472,
            )

            return self._parent._cast(
                _7472.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7475,
            )

            return self._parent._cast(
                _7475.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(
                _7483.PartToPartShearCouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(
                _7485.PlanetaryConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def ring_pins_to_disc_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(
                _7492.RingPinsToDiscConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7495,
            )

            return self._parent._cast(
                _7495.RollingRingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7499,
            )

            return self._parent._cast(
                _7499.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7502,
            )

            return self._parent._cast(
                _7502.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7505,
            )

            return self._parent._cast(
                _7505.SpringDamperConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7508,
            )

            return self._parent._cast(
                _7508.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(
                _7511.StraightBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7520,
            )

            return self._parent._cast(
                _7520.TorqueConverterConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7526,
            )

            return self._parent._cast(
                _7526.WormGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7529,
            )

            return self._parent._cast(
                _7529.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
        ) -> "ConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "ConnectionCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7304.ConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConnectionAdvancedSystemDeflection]

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
    ) -> "List[_7304.ConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConnectionAdvancedSystemDeflection]

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
    ) -> "ConnectionCompoundAdvancedSystemDeflection._Cast_ConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_ConnectionCompoundAdvancedSystemDeflection(self)
