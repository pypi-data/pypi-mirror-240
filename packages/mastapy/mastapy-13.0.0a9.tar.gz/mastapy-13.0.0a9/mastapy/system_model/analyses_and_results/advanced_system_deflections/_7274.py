"""AGMAGleasonConicalGearMeshAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7302
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2296


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshAdvancedSystemDeflection")


class AGMAGleasonConicalGearMeshAdvancedSystemDeflection(
    _7302.ConicalGearMeshAdvancedSystemDeflection
):
    """AGMAGleasonConicalGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
            parent: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7302.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7330,
            )

            return self._parent._cast(_7330.GearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7336,
            )

            return self._parent._cast(
                _7336.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7304,
            )

            return self._parent._cast(_7304.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7281,
            )

            return self._parent._cast(
                _7281.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7286,
            )

            return self._parent._cast(_7286.BevelGearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7334,
            )

            return self._parent._cast(_7334.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7372,
            )

            return self._parent._cast(_7372.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7378,
            )

            return self._parent._cast(
                _7378.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(
                _7381.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
        ) -> "AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2296.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

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
    ) -> "AGMAGleasonConicalGearMeshAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearMeshAdvancedSystemDeflection(self)
