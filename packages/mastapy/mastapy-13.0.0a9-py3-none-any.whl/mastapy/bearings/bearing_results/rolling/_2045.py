"""LoadedTaperRollerBearingResults"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_results.rolling import _2021
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_TAPER_ROLLER_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedTaperRollerBearingResults"
)


__docformat__ = "restructuredtext en"
__all__ = ("LoadedTaperRollerBearingResults",)


Self = TypeVar("Self", bound="LoadedTaperRollerBearingResults")


class LoadedTaperRollerBearingResults(_2021.LoadedNonBarrelRollerBearingResults):
    """LoadedTaperRollerBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_TAPER_ROLLER_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedTaperRollerBearingResults")

    class _Cast_LoadedTaperRollerBearingResults:
        """Special nested class for casting LoadedTaperRollerBearingResults to subclasses."""

        def __init__(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
            parent: "LoadedTaperRollerBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ):
            return self._parent._cast(_2021.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2026

            return self._parent._cast(_2026.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results.rolling import _2030

            return self._parent._cast(_2030.LoadedRollingBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1951

            return self._parent._cast(_1951.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1954

            return self._parent._cast(_1954.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ):
            from mastapy.bearings.bearing_results import _1946

            return self._parent._cast(_1946.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ):
            from mastapy.bearings import _1872

            return self._parent._cast(_1872.BearingLoadCaseResultsLightweight)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
        ) -> "LoadedTaperRollerBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedTaperRollerBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedTaperRollerBearingResults._Cast_LoadedTaperRollerBearingResults":
        return self._Cast_LoadedTaperRollerBearingResults(self)
