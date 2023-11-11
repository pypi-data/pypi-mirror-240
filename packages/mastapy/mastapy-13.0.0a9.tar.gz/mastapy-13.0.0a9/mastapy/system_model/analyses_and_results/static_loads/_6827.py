"""BoltedJointLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6949
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BoltedJointLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2440


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointLoadCase",)


Self = TypeVar("Self", bound="BoltedJointLoadCase")


class BoltedJointLoadCase(_6949.SpecialisedAssemblyLoadCase):
    """BoltedJointLoadCase

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointLoadCase")

    class _Cast_BoltedJointLoadCase:
        """Special nested class for casting BoltedJointLoadCase to subclasses."""

        def __init__(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
            parent: "BoltedJointLoadCase",
        ):
            self._parent = parent

        @property
        def specialised_assembly_load_case(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
        ):
            return self._parent._cast(_6949.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6803

            return self._parent._cast(_6803.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.PartLoadCase)

        @property
        def part_analysis(self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bolted_joint_load_case(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase",
        ) -> "BoltedJointLoadCase":
            return self._parent

        def __getattr__(
            self: "BoltedJointLoadCase._Cast_BoltedJointLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2440.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BoltedJointLoadCase._Cast_BoltedJointLoadCase":
        return self._Cast_BoltedJointLoadCase(self)
