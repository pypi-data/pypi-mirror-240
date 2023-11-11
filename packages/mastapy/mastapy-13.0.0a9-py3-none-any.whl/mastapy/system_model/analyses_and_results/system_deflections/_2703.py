"""BevelGearMeshSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2686
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BevelGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2300
    from mastapy.system_model.analyses_and_results.power_flows import _4045


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearMeshSystemDeflection")


class BevelGearMeshSystemDeflection(_2686.AGMAGleasonConicalGearMeshSystemDeflection):
    """BevelGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshSystemDeflection")

    class _Cast_BevelGearMeshSystemDeflection:
        """Special nested class for casting BevelGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
            parent: "BevelGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            return self._parent._cast(_2686.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.ConicalGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2756,
            )

            return self._parent._cast(_2756.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(
                _2764.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2698,
            )

            return self._parent._cast(_2698.BevelDifferentialGearMeshSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2804,
            )

            return self._parent._cast(_2804.SpiralBevelGearMeshSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.StraightBevelGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.ZerolBevelGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
        ) -> "BevelGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2300.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4045.BevelGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.BevelGearMeshPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshSystemDeflection._Cast_BevelGearMeshSystemDeflection":
        return self._Cast_BevelGearMeshSystemDeflection(self)
