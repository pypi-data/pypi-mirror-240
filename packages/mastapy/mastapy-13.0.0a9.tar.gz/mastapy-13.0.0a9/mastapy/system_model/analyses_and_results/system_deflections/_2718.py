"""ConceptGearSetSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2757
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ConceptGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2519
    from mastapy.system_model.analyses_and_results.static_loads import _6840
    from mastapy.gears.rating.concept import _551
    from mastapy.system_model.analyses_and_results.power_flows import _4060
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2719,
        _2717,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetSystemDeflection",)


Self = TypeVar("Self", bound="ConceptGearSetSystemDeflection")


class ConceptGearSetSystemDeflection(_2757.GearSetSystemDeflection):
    """ConceptGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptGearSetSystemDeflection")

    class _Cast_ConceptGearSetSystemDeflection:
        """Special nested class for casting ConceptGearSetSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection",
            parent: "ConceptGearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_set_system_deflection(
            self: "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection",
        ):
            return self._parent._cast(_2757.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2682,
            )

            return self._parent._cast(_2682.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def concept_gear_set_system_deflection(
            self: "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection",
        ) -> "ConceptGearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptGearSetSystemDeflection.TYPE"):
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
    def rating(self: Self) -> "_551.ConceptGearSetRating":
        """mastapy.gears.rating.concept.ConceptGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_551.ConceptGearSetRating":
        """mastapy.gears.rating.concept.ConceptGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4060.ConceptGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ConceptGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def concept_gears_system_deflection(
        self: Self,
    ) -> "List[_2719.ConceptGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConceptGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_system_deflection(
        self: Self,
    ) -> "List[_2717.ConceptGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConceptGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearSetSystemDeflection._Cast_ConceptGearSetSystemDeflection":
        return self._Cast_ConceptGearSetSystemDeflection(self)
