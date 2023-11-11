"""AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7437,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7269,
    )


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
)


class AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection(
    _7437.ConnectionCompoundAdvancedSystemDeflection
):
    """AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
            parent: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_compound_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            return self._parent._cast(_7437.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7426,
            )

            return self._parent._cast(
                _7426.CoaxialConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7446,
            )

            return self._parent._cast(
                _7446.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7448,
            )

            return self._parent._cast(
                _7448.CycloidalDiscPlanetaryBearingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_connection_compound_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(
                _7485.PlanetaryConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7499,
            )

            return self._parent._cast(
                _7499.ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7269.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7269.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection(
            self
        )
