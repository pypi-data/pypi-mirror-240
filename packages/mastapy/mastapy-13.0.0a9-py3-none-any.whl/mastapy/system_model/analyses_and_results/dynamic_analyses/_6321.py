"""CylindricalGearMeshDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CylindricalGearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2306
    from mastapy.system_model.analyses_and_results.static_loads import _6860


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearMeshDynamicAnalysis")


class CylindricalGearMeshDynamicAnalysis(_6334.GearMeshDynamicAnalysis):
    """CylindricalGearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMeshDynamicAnalysis")

    class _Cast_CylindricalGearMeshDynamicAnalysis:
        """Special nested class for casting CylindricalGearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearMeshDynamicAnalysis._Cast_CylindricalGearMeshDynamicAnalysis",
            parent: "CylindricalGearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_dynamic_analysis(
            self: "CylindricalGearMeshDynamicAnalysis._Cast_CylindricalGearMeshDynamicAnalysis",
        ):
            return self._parent._cast(_6334.GearMeshDynamicAnalysis)

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "CylindricalGearMeshDynamicAnalysis._Cast_CylindricalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6340

            return self._parent._cast(
                _6340.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "CylindricalGearMeshDynamicAnalysis._Cast_CylindricalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "CylindricalGearMeshDynamicAnalysis._Cast_CylindricalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7536

            return self._parent._cast(_7536.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CylindricalGearMeshDynamicAnalysis._Cast_CylindricalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7537

            return self._parent._cast(_7537.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshDynamicAnalysis._Cast_CylindricalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7534

            return self._parent._cast(_7534.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshDynamicAnalysis._Cast_CylindricalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshDynamicAnalysis._Cast_CylindricalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshDynamicAnalysis._Cast_CylindricalGearMeshDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_dynamic_analysis(
            self: "CylindricalGearMeshDynamicAnalysis._Cast_CylindricalGearMeshDynamicAnalysis",
        ) -> "CylindricalGearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshDynamicAnalysis._Cast_CylindricalGearMeshDynamicAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearMeshDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2306.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6860.CylindricalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[CylindricalGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearMeshDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshDynamicAnalysis._Cast_CylindricalGearMeshDynamicAnalysis":
        return self._Cast_CylindricalGearMeshDynamicAnalysis(self)
