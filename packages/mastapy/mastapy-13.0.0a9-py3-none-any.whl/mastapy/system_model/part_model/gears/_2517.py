"""BevelGearSet"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model.gears import _2511
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGearSet"
)


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSet",)


Self = TypeVar("Self", bound="BevelGearSet")


class BevelGearSet(_2511.AGMAGleasonConicalGearSet):
    """BevelGearSet

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSet")

    class _Cast_BevelGearSet:
        """Special nested class for casting BevelGearSet to subclasses."""

        def __init__(self: "BevelGearSet._Cast_BevelGearSet", parent: "BevelGearSet"):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            return self._parent._cast(_2511.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2521

            return self._parent._cast(_2521.ConicalGearSet)

        @property
        def gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2529

            return self._parent._cast(_2529.GearSet)

        @property
        def specialised_assembly(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.SpecialisedAssembly)

        @property
        def abstract_assembly(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model import _2431

            return self._parent._cast(_2431.AbstractAssembly)

        @property
        def part(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.Part)

        @property
        def design_entity(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model import _2200

            return self._parent._cast(_2200.DesignEntity)

        @property
        def bevel_differential_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2513

            return self._parent._cast(_2513.BevelDifferentialGearSet)

        @property
        def spiral_bevel_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.StraightBevelGearSet)

        @property
        def zerol_bevel_gear_set(self: "BevelGearSet._Cast_BevelGearSet"):
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.ZerolBevelGearSet)

        @property
        def bevel_gear_set(self: "BevelGearSet._Cast_BevelGearSet") -> "BevelGearSet":
            return self._parent

        def __getattr__(self: "BevelGearSet._Cast_BevelGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BevelGearSet._Cast_BevelGearSet":
        return self._Cast_BevelGearSet(self)
