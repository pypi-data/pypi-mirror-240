"""PlanetaryGearSetCriticalSpeedAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6591
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "PlanetaryGearSetCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetCriticalSpeedAnalysis")


class PlanetaryGearSetCriticalSpeedAnalysis(
    _6591.CylindricalGearSetCriticalSpeedAnalysis
):
    """PlanetaryGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCriticalSpeedAnalysis"
    )

    class _Cast_PlanetaryGearSetCriticalSpeedAnalysis:
        """Special nested class for casting PlanetaryGearSetCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
            parent: "PlanetaryGearSetCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_critical_speed_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ):
            return self._parent._cast(_6591.CylindricalGearSetCriticalSpeedAnalysis)

        @property
        def gear_set_critical_speed_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6602,
            )

            return self._parent._cast(_6602.GearSetCriticalSpeedAnalysis)

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6640,
            )

            return self._parent._cast(_6640.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6539,
            )

            return self._parent._cast(_6539.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6621,
            )

            return self._parent._cast(_6621.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def planetary_gear_set_critical_speed_analysis(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
        ) -> "PlanetaryGearSetCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2539.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCriticalSpeedAnalysis._Cast_PlanetaryGearSetCriticalSpeedAnalysis":
        return self._Cast_PlanetaryGearSetCriticalSpeedAnalysis(self)
