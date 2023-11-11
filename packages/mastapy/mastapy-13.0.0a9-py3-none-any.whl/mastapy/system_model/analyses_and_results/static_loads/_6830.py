"""ClutchHalfLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6849
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ClutchHalfLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2576


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfLoadCase",)


Self = TypeVar("Self", bound="ClutchHalfLoadCase")


class ClutchHalfLoadCase(_6849.CouplingHalfLoadCase):
    """ClutchHalfLoadCase

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfLoadCase")

    class _Cast_ClutchHalfLoadCase:
        """Special nested class for casting ClutchHalfLoadCase to subclasses."""

        def __init__(
            self: "ClutchHalfLoadCase._Cast_ClutchHalfLoadCase",
            parent: "ClutchHalfLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_half_load_case(
            self: "ClutchHalfLoadCase._Cast_ClutchHalfLoadCase",
        ):
            return self._parent._cast(_6849.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "ClutchHalfLoadCase._Cast_ClutchHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6921

            return self._parent._cast(_6921.MountableComponentLoadCase)

        @property
        def component_load_case(self: "ClutchHalfLoadCase._Cast_ClutchHalfLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.ComponentLoadCase)

        @property
        def part_load_case(self: "ClutchHalfLoadCase._Cast_ClutchHalfLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.PartLoadCase)

        @property
        def part_analysis(self: "ClutchHalfLoadCase._Cast_ClutchHalfLoadCase"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchHalfLoadCase._Cast_ClutchHalfLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "ClutchHalfLoadCase._Cast_ClutchHalfLoadCase"):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_load_case(
            self: "ClutchHalfLoadCase._Cast_ClutchHalfLoadCase",
        ) -> "ClutchHalfLoadCase":
            return self._parent

        def __getattr__(self: "ClutchHalfLoadCase._Cast_ClutchHalfLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchHalfLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2576.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ClutchHalfLoadCase._Cast_ClutchHalfLoadCase":
        return self._Cast_ClutchHalfLoadCase(self)
