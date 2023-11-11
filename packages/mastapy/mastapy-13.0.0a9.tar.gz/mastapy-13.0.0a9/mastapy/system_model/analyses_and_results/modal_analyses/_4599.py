"""ConceptGearSetModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4633
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ConceptGearSetModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2519
    from mastapy.system_model.analyses_and_results.static_loads import _6840
    from mastapy.system_model.analyses_and_results.system_deflections import _2718
    from mastapy.system_model.analyses_and_results.modal_analyses import _4598, _4597


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetModalAnalysis",)


Self = TypeVar("Self", bound="ConceptGearSetModalAnalysis")


class ConceptGearSetModalAnalysis(_4633.GearSetModalAnalysis):
    """ConceptGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSetModalAnalysis")

    class _Cast_ConceptGearSetModalAnalysis:
        """Special nested class for casting ConceptGearSetModalAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
            parent: "ConceptGearSetModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_modal_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ):
            return self._parent._cast(_4633.GearSetModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4568

            return self._parent._cast(_4568.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
        ) -> "ConceptGearSetModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearSetModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2519.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6840.ConceptGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2718.ConceptGearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gears_modal_analysis(
        self: Self,
    ) -> "List[_4598.ConceptGearModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_modal_analysis(
        self: Self,
    ) -> "List[_4597.ConceptGearMeshModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConceptGearMeshModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearSetModalAnalysis._Cast_ConceptGearSetModalAnalysis":
        return self._Cast_ConceptGearSetModalAnalysis(self)
