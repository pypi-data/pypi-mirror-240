"""LoadedNonLinearBearingDutyCycleResults"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results import _1945
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_LINEAR_BEARING_DUTY_CYCLE_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedNonLinearBearingDutyCycleResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonLinearBearingDutyCycleResults",)


Self = TypeVar("Self", bound="LoadedNonLinearBearingDutyCycleResults")


class LoadedNonLinearBearingDutyCycleResults(_1945.LoadedBearingDutyCycle):
    """LoadedNonLinearBearingDutyCycleResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_LINEAR_BEARING_DUTY_CYCLE_RESULTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedNonLinearBearingDutyCycleResults"
    )

    class _Cast_LoadedNonLinearBearingDutyCycleResults:
        """Special nested class for casting LoadedNonLinearBearingDutyCycleResults to subclasses."""

        def __init__(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
            parent: "LoadedNonLinearBearingDutyCycleResults",
        ):
            self._parent = parent

        @property
        def loaded_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ):
            return self._parent._cast(_1945.LoadedBearingDutyCycle)

        @property
        def loaded_rolling_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ):
            from mastapy.bearings.bearing_results import _1956

            return self._parent._cast(_1956.LoadedRollingBearingDutyCycle)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1989

            return self._parent._cast(
                _1989.LoadedAxialThrustCylindricalRollerBearingDutyCycle
            )

        @property
        def loaded_ball_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _1996

            return self._parent._cast(_1996.LoadedBallBearingDutyCycle)

        @property
        def loaded_cylindrical_roller_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2004

            return self._parent._cast(_2004.LoadedCylindricalRollerBearingDutyCycle)

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2020

            return self._parent._cast(_2020.LoadedNonBarrelRollerBearingDutyCycle)

        @property
        def loaded_taper_roller_bearing_duty_cycle(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2043

            return self._parent._cast(_2043.LoadedTaperRollerBearingDutyCycle)

        @property
        def loaded_non_linear_bearing_duty_cycle_results(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
        ) -> "LoadedNonLinearBearingDutyCycleResults":
            return self._parent

        def __getattr__(
            self: "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults",
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
        self: Self, instance_to_wrap: "LoadedNonLinearBearingDutyCycleResults.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def total_power_loss(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalPowerLoss

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedNonLinearBearingDutyCycleResults._Cast_LoadedNonLinearBearingDutyCycleResults":
        return self._Cast_LoadedNonLinearBearingDutyCycleResults(self)
