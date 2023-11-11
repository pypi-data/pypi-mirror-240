"""BearingConnectionComponent"""
from __future__ import annotations

from typing import TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_CONNECTION_COMPONENT = python_net_import(
    "SMT.MastaAPI.Bearings.Tolerances", "BearingConnectionComponent"
)


__docformat__ = "restructuredtext en"
__all__ = ("BearingConnectionComponent",)


Self = TypeVar("Self", bound="BearingConnectionComponent")


class BearingConnectionComponent(_0.APIBase):
    """BearingConnectionComponent

    This is a mastapy class.
    """

    TYPE = _BEARING_CONNECTION_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingConnectionComponent")

    class _Cast_BearingConnectionComponent:
        """Special nested class for casting BearingConnectionComponent to subclasses."""

        def __init__(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
            parent: "BearingConnectionComponent",
        ):
            self._parent = parent

        @property
        def inner_ring_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ):
            from mastapy.bearings.tolerances import _1903

            return self._parent._cast(_1903.InnerRingTolerance)

        @property
        def inner_support_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ):
            from mastapy.bearings.tolerances import _1904

            return self._parent._cast(_1904.InnerSupportTolerance)

        @property
        def interference_detail(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ):
            from mastapy.bearings.tolerances import _1905

            return self._parent._cast(_1905.InterferenceDetail)

        @property
        def interference_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ):
            from mastapy.bearings.tolerances import _1906

            return self._parent._cast(_1906.InterferenceTolerance)

        @property
        def mounting_sleeve_diameter_detail(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ):
            from mastapy.bearings.tolerances import _1908

            return self._parent._cast(_1908.MountingSleeveDiameterDetail)

        @property
        def outer_ring_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ):
            from mastapy.bearings.tolerances import _1909

            return self._parent._cast(_1909.OuterRingTolerance)

        @property
        def outer_support_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ):
            from mastapy.bearings.tolerances import _1910

            return self._parent._cast(_1910.OuterSupportTolerance)

        @property
        def race_detail(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ):
            from mastapy.bearings.tolerances import _1911

            return self._parent._cast(_1911.RaceDetail)

        @property
        def ring_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ):
            from mastapy.bearings.tolerances import _1914

            return self._parent._cast(_1914.RingTolerance)

        @property
        def support_detail(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ):
            from mastapy.bearings.tolerances import _1917

            return self._parent._cast(_1917.SupportDetail)

        @property
        def support_tolerance(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ):
            from mastapy.bearings.tolerances import _1919

            return self._parent._cast(_1919.SupportTolerance)

        @property
        def bearing_connection_component(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
        ) -> "BearingConnectionComponent":
            return self._parent

        def __getattr__(
            self: "BearingConnectionComponent._Cast_BearingConnectionComponent",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BearingConnectionComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BearingConnectionComponent._Cast_BearingConnectionComponent":
        return self._Cast_BearingConnectionComponent(self)
