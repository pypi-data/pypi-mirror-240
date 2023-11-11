"""ConicalGearSet"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2529
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1154
    from mastapy.system_model.part_model.gears import _2520


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSet",)


Self = TypeVar("Self", bound="ConicalGearSet")


class ConicalGearSet(_2529.GearSet):
    """ConicalGearSet

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSet")

    class _Cast_ConicalGearSet:
        """Special nested class for casting ConicalGearSet to subclasses."""

        def __init__(
            self: "ConicalGearSet._Cast_ConicalGearSet", parent: "ConicalGearSet"
        ):
            self._parent = parent

        @property
        def gear_set(self: "ConicalGearSet._Cast_ConicalGearSet"):
            return self._parent._cast(_2529.GearSet)

        @property
        def specialised_assembly(self: "ConicalGearSet._Cast_ConicalGearSet"):
            from mastapy.system_model.part_model import _2473

            return self._parent._cast(_2473.SpecialisedAssembly)

        @property
        def abstract_assembly(self: "ConicalGearSet._Cast_ConicalGearSet"):
            from mastapy.system_model.part_model import _2431

            return self._parent._cast(_2431.AbstractAssembly)

        @property
        def part(self: "ConicalGearSet._Cast_ConicalGearSet"):
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.Part)

        @property
        def design_entity(self: "ConicalGearSet._Cast_ConicalGearSet"):
            from mastapy.system_model import _2200

            return self._parent._cast(_2200.DesignEntity)

        @property
        def agma_gleason_conical_gear_set(self: "ConicalGearSet._Cast_ConicalGearSet"):
            from mastapy.system_model.part_model.gears import _2511

            return self._parent._cast(_2511.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear_set(self: "ConicalGearSet._Cast_ConicalGearSet"):
            from mastapy.system_model.part_model.gears import _2513

            return self._parent._cast(_2513.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(self: "ConicalGearSet._Cast_ConicalGearSet"):
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.BevelGearSet)

        @property
        def hypoid_gear_set(self: "ConicalGearSet._Cast_ConicalGearSet"):
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ):
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def spiral_bevel_gear_set(self: "ConicalGearSet._Cast_ConicalGearSet"):
            from mastapy.system_model.part_model.gears import _2541

            return self._parent._cast(_2541.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(self: "ConicalGearSet._Cast_ConicalGearSet"):
            from mastapy.system_model.part_model.gears import _2543

            return self._parent._cast(_2543.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(self: "ConicalGearSet._Cast_ConicalGearSet"):
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.StraightBevelGearSet)

        @property
        def zerol_bevel_gear_set(self: "ConicalGearSet._Cast_ConicalGearSet"):
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.ZerolBevelGearSet)

        @property
        def conical_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "ConicalGearSet":
            return self._parent

        def __getattr__(self: "ConicalGearSet._Cast_ConicalGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self: Self) -> "_1154.ConicalGearSetDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_set_design(self: Self) -> "_1154.ConicalGearSetDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gears(self: Self) -> "List[_2520.ConicalGear]":
        """List[mastapy.system_model.part_model.gears.ConicalGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConicalGearSet._Cast_ConicalGearSet":
        return self._Cast_ConicalGearSet(self)
