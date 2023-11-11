"""FaceGearSetCompoundModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4784
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "FaceGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.modal_analyses import _4627
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4777,
        _4778,
    )


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="FaceGearSetCompoundModalAnalysis")


class FaceGearSetCompoundModalAnalysis(_4784.GearSetCompoundModalAnalysis):
    """FaceGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetCompoundModalAnalysis")

    class _Cast_FaceGearSetCompoundModalAnalysis:
        """Special nested class for casting FaceGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "FaceGearSetCompoundModalAnalysis._Cast_FaceGearSetCompoundModalAnalysis",
            parent: "FaceGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_modal_analysis(
            self: "FaceGearSetCompoundModalAnalysis._Cast_FaceGearSetCompoundModalAnalysis",
        ):
            return self._parent._cast(_4784.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "FaceGearSetCompoundModalAnalysis._Cast_FaceGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(_4822.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "FaceGearSetCompoundModalAnalysis._Cast_FaceGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4724,
            )

            return self._parent._cast(_4724.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "FaceGearSetCompoundModalAnalysis._Cast_FaceGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4803,
            )

            return self._parent._cast(_4803.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "FaceGearSetCompoundModalAnalysis._Cast_FaceGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearSetCompoundModalAnalysis._Cast_FaceGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetCompoundModalAnalysis._Cast_FaceGearSetCompoundModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def face_gear_set_compound_modal_analysis(
            self: "FaceGearSetCompoundModalAnalysis._Cast_FaceGearSetCompoundModalAnalysis",
        ) -> "FaceGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearSetCompoundModalAnalysis._Cast_FaceGearSetCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2526.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2526.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4627.FaceGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.FaceGearSetModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_gears_compound_modal_analysis(
        self: Self,
    ) -> "List[_4777.FaceGearCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.FaceGearCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_compound_modal_analysis(
        self: Self,
    ) -> "List[_4778.FaceGearMeshCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.FaceGearMeshCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4627.FaceGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.FaceGearSetModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetCompoundModalAnalysis._Cast_FaceGearSetCompoundModalAnalysis":
        return self._Cast_FaceGearSetCompoundModalAnalysis(self)
