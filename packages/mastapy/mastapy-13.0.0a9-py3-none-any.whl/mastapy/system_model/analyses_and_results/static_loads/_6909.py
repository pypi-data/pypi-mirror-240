"""KlingelnbergCycloPalloidConicalGearLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6841
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidConicalGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2533


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearLoadCase",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearLoadCase")


class KlingelnbergCycloPalloidConicalGearLoadCase(_6841.ConicalGearLoadCase):
    """KlingelnbergCycloPalloidConicalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearLoadCase"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearLoadCase:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearLoadCase to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
            parent: "KlingelnbergCycloPalloidConicalGearLoadCase",
        ):
            self._parent = parent

        @property
        def conical_gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ):
            return self._parent._cast(_6841.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6887

            return self._parent._cast(_6887.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6921

            return self._parent._cast(_6921.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.ComponentLoadCase)

        @property
        def part_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.PartLoadCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(
                _6915.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
        ) -> "KlingelnbergCycloPalloidConicalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidConicalGearLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2533.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearLoadCase._Cast_KlingelnbergCycloPalloidConicalGearLoadCase":
        return self._Cast_KlingelnbergCycloPalloidConicalGearLoadCase(self)
