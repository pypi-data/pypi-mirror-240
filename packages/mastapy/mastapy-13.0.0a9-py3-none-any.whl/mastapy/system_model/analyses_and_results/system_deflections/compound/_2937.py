"""PulleyCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2887
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "PulleyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2587
    from mastapy.system_model.analyses_and_results.system_deflections import _2790


__docformat__ = "restructuredtext en"
__all__ = ("PulleyCompoundSystemDeflection",)


Self = TypeVar("Self", bound="PulleyCompoundSystemDeflection")


class PulleyCompoundSystemDeflection(_2887.CouplingHalfCompoundSystemDeflection):
    """PulleyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PULLEY_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyCompoundSystemDeflection")

    class _Cast_PulleyCompoundSystemDeflection:
        """Special nested class for casting PulleyCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "PulleyCompoundSystemDeflection._Cast_PulleyCompoundSystemDeflection",
            parent: "PulleyCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_system_deflection(
            self: "PulleyCompoundSystemDeflection._Cast_PulleyCompoundSystemDeflection",
        ):
            return self._parent._cast(_2887.CouplingHalfCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "PulleyCompoundSystemDeflection._Cast_PulleyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(_2926.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "PulleyCompoundSystemDeflection._Cast_PulleyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "PulleyCompoundSystemDeflection._Cast_PulleyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(_2928.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "PulleyCompoundSystemDeflection._Cast_PulleyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PulleyCompoundSystemDeflection._Cast_PulleyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyCompoundSystemDeflection._Cast_PulleyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "PulleyCompoundSystemDeflection._Cast_PulleyCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2890,
            )

            return self._parent._cast(_2890.CVTPulleyCompoundSystemDeflection)

        @property
        def pulley_compound_system_deflection(
            self: "PulleyCompoundSystemDeflection._Cast_PulleyCompoundSystemDeflection",
        ) -> "PulleyCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PulleyCompoundSystemDeflection._Cast_PulleyCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2790.PulleySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PulleySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(self: Self) -> "List[_2790.PulleySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PulleySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PulleyCompoundSystemDeflection._Cast_PulleyCompoundSystemDeflection":
        return self._Cast_PulleyCompoundSystemDeflection(self)
