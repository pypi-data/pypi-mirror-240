"""AbstractShaftCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2850
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "AbstractShaftCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2684


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundSystemDeflection",)


Self = TypeVar("Self", bound="AbstractShaftCompoundSystemDeflection")


class AbstractShaftCompoundSystemDeflection(
    _2850.AbstractShaftOrHousingCompoundSystemDeflection
):
    """AbstractShaftCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundSystemDeflection"
    )

    class _Cast_AbstractShaftCompoundSystemDeflection:
        """Special nested class for casting AbstractShaftCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundSystemDeflection._Cast_AbstractShaftCompoundSystemDeflection",
            parent: "AbstractShaftCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_system_deflection(
            self: "AbstractShaftCompoundSystemDeflection._Cast_AbstractShaftCompoundSystemDeflection",
        ):
            return self._parent._cast(
                _2850.AbstractShaftOrHousingCompoundSystemDeflection
            )

        @property
        def component_compound_system_deflection(
            self: "AbstractShaftCompoundSystemDeflection._Cast_AbstractShaftCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2873,
            )

            return self._parent._cast(_2873.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "AbstractShaftCompoundSystemDeflection._Cast_AbstractShaftCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2928,
            )

            return self._parent._cast(_2928.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundSystemDeflection._Cast_AbstractShaftCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundSystemDeflection._Cast_AbstractShaftCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundSystemDeflection._Cast_AbstractShaftCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_system_deflection(
            self: "AbstractShaftCompoundSystemDeflection._Cast_AbstractShaftCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2893,
            )

            return self._parent._cast(_2893.CycloidalDiscCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(
            self: "AbstractShaftCompoundSystemDeflection._Cast_AbstractShaftCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2944,
            )

            return self._parent._cast(_2944.ShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_compound_system_deflection(
            self: "AbstractShaftCompoundSystemDeflection._Cast_AbstractShaftCompoundSystemDeflection",
        ) -> "AbstractShaftCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundSystemDeflection._Cast_AbstractShaftCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2684.AbstractShaftSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2684.AbstractShaftSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "AbstractShaftCompoundSystemDeflection._Cast_AbstractShaftCompoundSystemDeflection":
        return self._Cast_AbstractShaftCompoundSystemDeflection(self)
