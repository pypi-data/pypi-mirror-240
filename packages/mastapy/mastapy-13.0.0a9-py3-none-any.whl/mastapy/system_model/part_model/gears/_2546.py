"""StraightBevelPlanetGear"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelPlanetGear"
)

if TYPE_CHECKING:
    from mastapy.gears import _338


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGear",)


Self = TypeVar("Self", bound="StraightBevelPlanetGear")


class StraightBevelPlanetGear(_2542.StraightBevelDiffGear):
    """StraightBevelPlanetGear

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelPlanetGear")

    class _Cast_StraightBevelPlanetGear:
        """Special nested class for casting StraightBevelPlanetGear to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
            parent: "StraightBevelPlanetGear",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ):
            return self._parent._cast(_2542.StraightBevelDiffGear)

        @property
        def bevel_gear(self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear"):
            from mastapy.system_model.part_model.gears import _2516

            return self._parent._cast(_2516.BevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ):
            from mastapy.system_model.part_model.gears import _2510

            return self._parent._cast(_2510.AGMAGleasonConicalGear)

        @property
        def conical_gear(self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear"):
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.ConicalGear)

        @property
        def gear(self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear"):
            from mastapy.system_model.part_model.gears import _2527

            return self._parent._cast(_2527.Gear)

        @property
        def mountable_component(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ):
            from mastapy.system_model.part_model import _2461

            return self._parent._cast(_2461.MountableComponent)

        @property
        def component(self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear"):
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.Component)

        @property
        def part(self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear"):
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.Part)

        @property
        def design_entity(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ):
            from mastapy.system_model import _2200

            return self._parent._cast(_2200.DesignEntity)

        @property
        def straight_bevel_planet_gear(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear",
        ) -> "StraightBevelPlanetGear":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelPlanetGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetary_details(self: Self) -> "_338.PlanetaryDetail":
        """mastapy.gears.PlanetaryDetail

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetaryDetails

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "StraightBevelPlanetGear._Cast_StraightBevelPlanetGear":
        return self._Cast_StraightBevelPlanetGear(self)
