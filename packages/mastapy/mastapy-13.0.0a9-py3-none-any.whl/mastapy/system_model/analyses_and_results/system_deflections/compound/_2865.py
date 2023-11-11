"""BevelGearMeshCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2853
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "BevelGearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2703


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundSystemDeflection")


class BevelGearMeshCompoundSystemDeflection(
    _2853.AGMAGleasonConicalGearMeshCompoundSystemDeflection
):
    """BevelGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshCompoundSystemDeflection"
    )

    class _Cast_BevelGearMeshCompoundSystemDeflection:
        """Special nested class for casting BevelGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
            parent: "BevelGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ):
            return self._parent._cast(
                _2853.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2881,
            )

            return self._parent._cast(_2881.ConicalGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2908,
            )

            return self._parent._cast(_2908.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2914,
            )

            return self._parent._cast(
                _2914.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2883,
            )

            return self._parent._cast(_2883.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2860,
            )

            return self._parent._cast(
                _2860.BevelDifferentialGearMeshCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2956,
            )

            return self._parent._cast(
                _2956.StraightBevelDiffGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(
                _2959.StraightBevelGearMeshCompoundSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(_2977.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "BevelGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelGearMeshCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2703.BevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection]

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
    ) -> "List[_2703.BevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection]

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
    ) -> "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection":
        return self._Cast_BevelGearMeshCompoundSystemDeflection(self)
