"""ShaftToMountableComponentConnectionLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6806
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ShaftToMountableComponentConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2292


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionLoadCase",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionLoadCase")


class ShaftToMountableComponentConnectionLoadCase(
    _6806.AbstractShaftToMountableComponentConnectionLoadCase
):
    """ShaftToMountableComponentConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftToMountableComponentConnectionLoadCase"
    )

    class _Cast_ShaftToMountableComponentConnectionLoadCase:
        """Special nested class for casting ShaftToMountableComponentConnectionLoadCase to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
            parent: "ShaftToMountableComponentConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_load_case(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            return self._parent._cast(
                _6806.AbstractShaftToMountableComponentConnectionLoadCase
            )

        @property
        def connection_load_case(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2646

            return self._parent._cast(_2646.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def coaxial_connection_load_case(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.CoaxialConnectionLoadCase)

        @property
        def cycloidal_disc_central_bearing_connection_load_case(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(
                _6855.CycloidalDiscCentralBearingConnectionLoadCase
            )

        @property
        def planetary_connection_load_case(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.PlanetaryConnectionLoadCase)

        @property
        def shaft_to_mountable_component_connection_load_case(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
        ) -> "ShaftToMountableComponentConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase",
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
        self: Self, instance_to_wrap: "ShaftToMountableComponentConnectionLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2292.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

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
    ) -> "ShaftToMountableComponentConnectionLoadCase._Cast_ShaftToMountableComponentConnectionLoadCase":
        return self._Cast_ShaftToMountableComponentConnectionLoadCase(self)
