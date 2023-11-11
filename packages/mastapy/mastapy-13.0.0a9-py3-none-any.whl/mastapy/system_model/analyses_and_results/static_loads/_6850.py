"""CouplingLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6949
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CouplingLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580


__docformat__ = "restructuredtext en"
__all__ = ("CouplingLoadCase",)


Self = TypeVar("Self", bound="CouplingLoadCase")


class CouplingLoadCase(_6949.SpecialisedAssemblyLoadCase):
    """CouplingLoadCase

    This is a mastapy class.
    """

    TYPE = _COUPLING_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingLoadCase")

    class _Cast_CouplingLoadCase:
        """Special nested class for casting CouplingLoadCase to subclasses."""

        def __init__(
            self: "CouplingLoadCase._Cast_CouplingLoadCase", parent: "CouplingLoadCase"
        ):
            self._parent = parent

        @property
        def specialised_assembly_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ):
            return self._parent._cast(_6949.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6803

            return self._parent._cast(_6803.AbstractAssemblyLoadCase)

        @property
        def part_load_case(self: "CouplingLoadCase._Cast_CouplingLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.PartLoadCase)

        @property
        def part_analysis(self: "CouplingLoadCase._Cast_CouplingLoadCase"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "CouplingLoadCase._Cast_CouplingLoadCase"):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_load_case(self: "CouplingLoadCase._Cast_CouplingLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(_6831.ClutchLoadCase)

        @property
        def concept_coupling_load_case(self: "CouplingLoadCase._Cast_CouplingLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ConceptCouplingLoadCase)

        @property
        def part_to_part_shear_coupling_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6928

            return self._parent._cast(_6928.PartToPartShearCouplingLoadCase)

        @property
        def spring_damper_load_case(self: "CouplingLoadCase._Cast_CouplingLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.SpringDamperLoadCase)

        @property
        def torque_converter_load_case(self: "CouplingLoadCase._Cast_CouplingLoadCase"):
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.TorqueConverterLoadCase)

        @property
        def coupling_load_case(
            self: "CouplingLoadCase._Cast_CouplingLoadCase",
        ) -> "CouplingLoadCase":
            return self._parent

        def __getattr__(self: "CouplingLoadCase._Cast_CouplingLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2580.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingLoadCase._Cast_CouplingLoadCase":
        return self._Cast_CouplingLoadCase(self)
