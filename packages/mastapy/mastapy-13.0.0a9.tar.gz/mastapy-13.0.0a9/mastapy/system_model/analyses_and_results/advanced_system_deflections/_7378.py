"""StraightBevelDiffGearMeshAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7286
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "StraightBevelDiffGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.straight_bevel_diff import _396
    from mastapy.system_model.connections_and_sockets.gears import _2322
    from mastapy.system_model.analyses_and_results.static_loads import _6957
    from mastapy.system_model.analyses_and_results.system_deflections import _2810


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshAdvancedSystemDeflection")


class StraightBevelDiffGearMeshAdvancedSystemDeflection(
    _7286.BevelGearMeshAdvancedSystemDeflection
):
    """StraightBevelDiffGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection"
    )

    class _Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelDiffGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
            parent: "StraightBevelDiffGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7286.BevelGearMeshAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7274,
            )

            return self._parent._cast(
                _7274.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7302,
            )

            return self._parent._cast(_7302.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7330,
            )

            return self._parent._cast(_7330.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7336,
            )

            return self._parent._cast(
                _7336.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7304,
            )

            return self._parent._cast(_7304.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
        ) -> "StraightBevelDiffGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection",
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
        instance_to_wrap: "StraightBevelDiffGearMeshAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_detailed_analysis(
        self: Self,
    ) -> "_396.StraightBevelDiffGearMeshRating":
        """mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2322.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6957.StraightBevelDiffGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2810.StraightBevelDiffGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.StraightBevelDiffGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearMeshAdvancedSystemDeflection._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection":
        return self._Cast_StraightBevelDiffGearMeshAdvancedSystemDeflection(self)
