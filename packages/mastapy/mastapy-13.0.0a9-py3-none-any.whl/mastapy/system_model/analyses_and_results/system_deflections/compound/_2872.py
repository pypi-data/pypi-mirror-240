"""CoaxialConnectionCompoundSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2947
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CoaxialConnectionCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2266
    from mastapy.system_model.analyses_and_results.system_deflections import _2711


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundSystemDeflection")


class CoaxialConnectionCompoundSystemDeflection(
    _2947.ShaftToMountableComponentConnectionCompoundSystemDeflection
):
    """CoaxialConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionCompoundSystemDeflection"
    )

    class _Cast_CoaxialConnectionCompoundSystemDeflection:
        """Special nested class for casting CoaxialConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
            parent: "CoaxialConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_system_deflection(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ):
            return self._parent._cast(
                _2947.ShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2851,
            )

            return self._parent._cast(
                _2851.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2883,
            )

            return self._parent._cast(_2883.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7535

            return self._parent._cast(_7535.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_system_deflection(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2892,
            )

            return self._parent._cast(
                _2892.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
            )

        @property
        def coaxial_connection_compound_system_deflection(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ) -> "CoaxialConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "CoaxialConnectionCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2266.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2266.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2711.CoaxialConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2711.CoaxialConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection":
        return self._Cast_CoaxialConnectionCompoundSystemDeflection(self)
