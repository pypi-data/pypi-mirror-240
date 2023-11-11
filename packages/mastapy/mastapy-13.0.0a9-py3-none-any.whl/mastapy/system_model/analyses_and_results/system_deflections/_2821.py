"""SynchroniserSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2803
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SynchroniserSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.static_loads import _6965
    from mastapy.system_model.analyses_and_results.power_flows import _4148
    from mastapy.system_model.analyses_and_results.system_deflections import _2818


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSystemDeflection",)


Self = TypeVar("Self", bound="SynchroniserSystemDeflection")


class SynchroniserSystemDeflection(_2803.SpecialisedAssemblySystemDeflection):
    """SynchroniserSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserSystemDeflection")

    class _Cast_SynchroniserSystemDeflection:
        """Special nested class for casting SynchroniserSystemDeflection to subclasses."""

        def __init__(
            self: "SynchroniserSystemDeflection._Cast_SynchroniserSystemDeflection",
            parent: "SynchroniserSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_system_deflection(
            self: "SynchroniserSystemDeflection._Cast_SynchroniserSystemDeflection",
        ):
            return self._parent._cast(_2803.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "SynchroniserSystemDeflection._Cast_SynchroniserSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2682,
            )

            return self._parent._cast(_2682.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "SynchroniserSystemDeflection._Cast_SynchroniserSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "SynchroniserSystemDeflection._Cast_SynchroniserSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSystemDeflection._Cast_SynchroniserSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSystemDeflection._Cast_SynchroniserSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSystemDeflection._Cast_SynchroniserSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSystemDeflection._Cast_SynchroniserSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSystemDeflection._Cast_SynchroniserSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def synchroniser_system_deflection(
            self: "SynchroniserSystemDeflection._Cast_SynchroniserSystemDeflection",
        ) -> "SynchroniserSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SynchroniserSystemDeflection._Cast_SynchroniserSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2599.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6965.SynchroniserLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4148.SynchroniserPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SynchroniserPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cones(self: Self) -> "List[_2818.SynchroniserHalfSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.SynchroniserHalfSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Cones

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserSystemDeflection._Cast_SynchroniserSystemDeflection":
        return self._Cast_SynchroniserSystemDeflection(self)
