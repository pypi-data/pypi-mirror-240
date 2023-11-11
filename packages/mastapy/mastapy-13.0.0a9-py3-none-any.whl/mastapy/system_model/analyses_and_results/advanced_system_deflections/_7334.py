"""HypoidGearMeshAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7274
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "HypoidGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.rating.hypoid import _436
    from mastapy.system_model.connections_and_sockets.gears import _2312
    from mastapy.system_model.analyses_and_results.static_loads import _6903
    from mastapy.system_model.analyses_and_results.system_deflections import _2760


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="HypoidGearMeshAdvancedSystemDeflection")


class HypoidGearMeshAdvancedSystemDeflection(
    _7274.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
):
    """HypoidGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshAdvancedSystemDeflection"
    )

    class _Cast_HypoidGearMeshAdvancedSystemDeflection:
        """Special nested class for casting HypoidGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection",
            parent: "HypoidGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7274.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7302,
            )

            return self._parent._cast(_7302.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7330,
            )

            return self._parent._cast(_7330.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7336,
            )

            return self._parent._cast(
                _7336.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7304,
            )

            return self._parent._cast(_7304.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(
            self: "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection",
        ) -> "HypoidGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "HypoidGearMeshAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_detailed_analysis(self: Self) -> "_436.HypoidGearMeshRating":
        """mastapy.gears.rating.hypoid.HypoidGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2312.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6903.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

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
    ) -> "List[_2760.HypoidGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.HypoidGearMeshSystemDeflection]

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
    ) -> "HypoidGearMeshAdvancedSystemDeflection._Cast_HypoidGearMeshAdvancedSystemDeflection":
        return self._Cast_HypoidGearMeshAdvancedSystemDeflection(self)
