"""AbstractShaftToMountableComponentConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractShaftToMountableComponentConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2262


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionLoadCase",)


Self = TypeVar("Self", bound="AbstractShaftToMountableComponentConnectionLoadCase")


class AbstractShaftToMountableComponentConnectionLoadCase(_6846.ConnectionLoadCase):
    """AbstractShaftToMountableComponentConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftToMountableComponentConnectionLoadCase"
    )

    class _Cast_AbstractShaftToMountableComponentConnectionLoadCase:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionLoadCase to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase",
            parent: "AbstractShaftToMountableComponentConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def connection_load_case(
            self: "AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase",
        ):
            return self._parent._cast(_6846.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_load_case(
            self: "AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.CoaxialConnectionLoadCase)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(
            self: "AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(
                _6855.CycloidalDiscCentralBearingConnectionLoadCase
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_load_case(
            self: "AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(
                _6857.CycloidalDiscPlanetaryBearingConnectionLoadCase
            )

        @property
        def planetary_connection_load_case(
            self: "AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PlanetaryConnectionLoadCase)

        @property
        def shaft_to_mountable_component_connection_load_case(
            self: "AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.ShaftToMountableComponentConnectionLoadCase)

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(
            self: "AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase",
        ) -> "AbstractShaftToMountableComponentConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionLoadCase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2262.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionLoadCase._Cast_AbstractShaftToMountableComponentConnectionLoadCase":
        return self._Cast_AbstractShaftToMountableComponentConnectionLoadCase(self)
