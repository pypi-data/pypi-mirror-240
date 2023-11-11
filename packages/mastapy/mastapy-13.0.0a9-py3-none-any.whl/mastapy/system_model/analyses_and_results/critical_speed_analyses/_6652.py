"""StraightBevelGearSetCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6557
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "StraightBevelGearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.static_loads import _6961
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6650,
        _6651,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearSetCriticalSpeedAnalysis")


class StraightBevelGearSetCriticalSpeedAnalysis(
    _6557.BevelGearSetCriticalSpeedAnalysis
):
    """StraightBevelGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearSetCriticalSpeedAnalysis"
    )

    class _Cast_StraightBevelGearSetCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
            parent: "StraightBevelGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_critical_speed_analysis(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6557.BevelGearSetCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_critical_speed_analysis(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6545,
            )

            return self._parent._cast(
                _6545.AGMAGleasonConicalGearSetCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_critical_speed_analysis(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.ConicalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6602,
            )

            return self._parent._cast(_6602.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6640,
            )

            return self._parent._cast(_6640.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6539,
            )

            return self._parent._cast(_6539.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_critical_speed_analysis(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
        ) -> "StraightBevelGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelGearSetCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2545.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6961.StraightBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_gears_critical_speed_analysis(
        self: Self,
    ) -> "List[_6650.StraightBevelGearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelGearCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_critical_speed_analysis(
        self: Self,
    ) -> "List[_6651.StraightBevelGearMeshCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelGearMeshCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearSetCriticalSpeedAnalysis._Cast_StraightBevelGearSetCriticalSpeedAnalysis":
        return self._Cast_StraightBevelGearSetCriticalSpeedAnalysis(self)
