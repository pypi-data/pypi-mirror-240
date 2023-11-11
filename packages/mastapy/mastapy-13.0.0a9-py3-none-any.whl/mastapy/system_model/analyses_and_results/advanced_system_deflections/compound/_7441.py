"""CouplingHalfCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7479,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CouplingHalfCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7309,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CouplingHalfCompoundAdvancedSystemDeflection")


class CouplingHalfCompoundAdvancedSystemDeflection(
    _7479.MountableComponentCompoundAdvancedSystemDeflection
):
    """CouplingHalfCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingHalfCompoundAdvancedSystemDeflection"
    )

    class _Cast_CouplingHalfCompoundAdvancedSystemDeflection:
        """Special nested class for casting CouplingHalfCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
            parent: "CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7479.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(_7427.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7481,
            )

            return self._parent._cast(_7481.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7425,
            )

            return self._parent._cast(_7425.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7430,
            )

            return self._parent._cast(
                _7430.ConceptCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7444,
            )

            return self._parent._cast(_7444.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7484,
            )

            return self._parent._cast(
                _7484.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def pulley_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7490,
            )

            return self._parent._cast(_7490.PulleyCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7494,
            )

            return self._parent._cast(_7494.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(
                _7506.SpringDamperHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7516,
            )

            return self._parent._cast(
                _7516.SynchroniserHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7517,
            )

            return self._parent._cast(
                _7517.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7518,
            )

            return self._parent._cast(
                _7518.SynchroniserSleeveCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_pump_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.TorqueConverterPumpCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7522,
            )

            return self._parent._cast(
                _7522.TorqueConverterTurbineCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "CouplingHalfCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection",
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
        self: Self,
        instance_to_wrap: "CouplingHalfCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7309.CouplingHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingHalfAdvancedSystemDeflection]

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
    ) -> "List[_7309.CouplingHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CouplingHalfAdvancedSystemDeflection]

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
    ) -> "CouplingHalfCompoundAdvancedSystemDeflection._Cast_CouplingHalfCompoundAdvancedSystemDeflection":
        return self._Cast_CouplingHalfCompoundAdvancedSystemDeflection(self)
