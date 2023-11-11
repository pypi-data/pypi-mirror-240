"""VirtualComponent"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.part_model import _2461
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "VirtualComponent"
)


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponent",)


Self = TypeVar("Self", bound="VirtualComponent")


class VirtualComponent(_2461.MountableComponent):
    """VirtualComponent

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponent")

    class _Cast_VirtualComponent:
        """Special nested class for casting VirtualComponent to subclasses."""

        def __init__(
            self: "VirtualComponent._Cast_VirtualComponent", parent: "VirtualComponent"
        ):
            self._parent = parent

        @property
        def mountable_component(self: "VirtualComponent._Cast_VirtualComponent"):
            return self._parent._cast(_2461.MountableComponent)

        @property
        def component(self: "VirtualComponent._Cast_VirtualComponent"):
            from mastapy.system_model.part_model import _2441

            return self._parent._cast(_2441.Component)

        @property
        def part(self: "VirtualComponent._Cast_VirtualComponent"):
            from mastapy.system_model.part_model import _2465

            return self._parent._cast(_2465.Part)

        @property
        def design_entity(self: "VirtualComponent._Cast_VirtualComponent"):
            from mastapy.system_model import _2200

            return self._parent._cast(_2200.DesignEntity)

        @property
        def mass_disc(self: "VirtualComponent._Cast_VirtualComponent"):
            from mastapy.system_model.part_model import _2459

            return self._parent._cast(_2459.MassDisc)

        @property
        def measurement_component(self: "VirtualComponent._Cast_VirtualComponent"):
            from mastapy.system_model.part_model import _2460

            return self._parent._cast(_2460.MeasurementComponent)

        @property
        def point_load(self: "VirtualComponent._Cast_VirtualComponent"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.PointLoad)

        @property
        def power_load(self: "VirtualComponent._Cast_VirtualComponent"):
            from mastapy.system_model.part_model import _2469

            return self._parent._cast(_2469.PowerLoad)

        @property
        def unbalanced_mass(self: "VirtualComponent._Cast_VirtualComponent"):
            from mastapy.system_model.part_model import _2474

            return self._parent._cast(_2474.UnbalancedMass)

        @property
        def virtual_component(
            self: "VirtualComponent._Cast_VirtualComponent",
        ) -> "VirtualComponent":
            return self._parent

        def __getattr__(self: "VirtualComponent._Cast_VirtualComponent", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "VirtualComponent._Cast_VirtualComponent":
        return self._Cast_VirtualComponent(self)
