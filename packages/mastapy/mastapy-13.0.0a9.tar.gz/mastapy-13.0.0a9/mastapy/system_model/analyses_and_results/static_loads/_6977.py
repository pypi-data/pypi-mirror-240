"""UnbalancedMassLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6978
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "UnbalancedMassLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassLoadCase",)


Self = TypeVar("Self", bound="UnbalancedMassLoadCase")


class UnbalancedMassLoadCase(_6978.VirtualComponentLoadCase):
    """UnbalancedMassLoadCase

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_UnbalancedMassLoadCase")

    class _Cast_UnbalancedMassLoadCase:
        """Special nested class for casting UnbalancedMassLoadCase to subclasses."""

        def __init__(
            self: "UnbalancedMassLoadCase._Cast_UnbalancedMassLoadCase",
            parent: "UnbalancedMassLoadCase",
        ):
            self._parent = parent

        @property
        def virtual_component_load_case(
            self: "UnbalancedMassLoadCase._Cast_UnbalancedMassLoadCase",
        ):
            return self._parent._cast(_6978.VirtualComponentLoadCase)

        @property
        def mountable_component_load_case(
            self: "UnbalancedMassLoadCase._Cast_UnbalancedMassLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6921

            return self._parent._cast(_6921.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "UnbalancedMassLoadCase._Cast_UnbalancedMassLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.ComponentLoadCase)

        @property
        def part_load_case(self: "UnbalancedMassLoadCase._Cast_UnbalancedMassLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.PartLoadCase)

        @property
        def part_analysis(self: "UnbalancedMassLoadCase._Cast_UnbalancedMassLoadCase"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassLoadCase._Cast_UnbalancedMassLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassLoadCase._Cast_UnbalancedMassLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def unbalanced_mass_load_case(
            self: "UnbalancedMassLoadCase._Cast_UnbalancedMassLoadCase",
        ) -> "UnbalancedMassLoadCase":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassLoadCase._Cast_UnbalancedMassLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "UnbalancedMassLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Angle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @angle.setter
    @enforce_parameter_types
    def angle(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Angle = value

    @property
    def mass(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @mass.setter
    @enforce_parameter_types
    def mass(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Mass = value

    @property
    def radius(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Radius

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @radius.setter
    @enforce_parameter_types
    def radius(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Radius = value

    @property
    def component_design(self: Self) -> "_2474.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "UnbalancedMassLoadCase._Cast_UnbalancedMassLoadCase":
        return self._Cast_UnbalancedMassLoadCase(self)
