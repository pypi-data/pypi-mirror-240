"""GearMeshCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2914
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "GearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2756


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshCompoundSystemDeflection",)


Self = TypeVar("Self", bound="GearMeshCompoundSystemDeflection")


class GearMeshCompoundSystemDeflection(
    _2914.InterMountableComponentConnectionCompoundSystemDeflection
):
    """GearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshCompoundSystemDeflection")

    class _Cast_GearMeshCompoundSystemDeflection:
        """Special nested class for casting GearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
            parent: "GearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            return self._parent._cast(
                _2914.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2883,
            )

            return self._parent._cast(_2883.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2853,
            )

            return self._parent._cast(
                _2853.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2860,
            )

            return self._parent._cast(
                _2860.BevelDifferentialGearMeshCompoundSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2865,
            )

            return self._parent._cast(_2865.BevelGearMeshCompoundSystemDeflection)

        @property
        def concept_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2878,
            )

            return self._parent._cast(_2878.ConceptGearMeshCompoundSystemDeflection)

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2881,
            )

            return self._parent._cast(_2881.ConicalGearMeshCompoundSystemDeflection)

        @property
        def cylindrical_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2896,
            )

            return self._parent._cast(_2896.CylindricalGearMeshCompoundSystemDeflection)

        @property
        def face_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2903,
            )

            return self._parent._cast(_2903.FaceGearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2912,
            )

            return self._parent._cast(_2912.HypoidGearMeshCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2916,
            )

            return self._parent._cast(
                _2916.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2919,
            )

            return self._parent._cast(
                _2919.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2922,
            )

            return self._parent._cast(
                _2922.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2956,
            )

            return self._parent._cast(
                _2956.StraightBevelDiffGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(
                _2959.StraightBevelGearMeshCompoundSystemDeflection
            )

        @property
        def worm_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.WormGearMeshCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(_2977.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
        ) -> "GearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self: Self) -> "List[_2756.GearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection]

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
    ) -> "List[_2756.GearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection]

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
    ) -> "GearMeshCompoundSystemDeflection._Cast_GearMeshCompoundSystemDeflection":
        return self._Cast_GearMeshCompoundSystemDeflection(self)
