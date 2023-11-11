"""StraightBevelPlanetGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6956
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelPlanetGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2546


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearLoadCase",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearLoadCase")


class StraightBevelPlanetGearLoadCase(_6956.StraightBevelDiffGearLoadCase):
    """StraightBevelPlanetGearLoadCase

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelPlanetGearLoadCase")

    class _Cast_StraightBevelPlanetGearLoadCase:
        """Special nested class for casting StraightBevelPlanetGearLoadCase to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
            parent: "StraightBevelPlanetGearLoadCase",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ):
            return self._parent._cast(_6956.StraightBevelDiffGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.BevelGearLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6810

            return self._parent._cast(_6810.AGMAGleasonConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6887

            return self._parent._cast(_6887.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6921

            return self._parent._cast(_6921.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.ComponentLoadCase)

        @property
        def part_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.PartLoadCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
        ) -> "StraightBevelPlanetGearLoadCase":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelPlanetGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2546.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearLoadCase._Cast_StraightBevelPlanetGearLoadCase":
        return self._Cast_StraightBevelPlanetGearLoadCase(self)
