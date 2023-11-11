"""NonLinearBearing"""
from __future__ import annotations

from typing import TypeVar

from mastapy.bearings.bearing_designs import _2127
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NON_LINEAR_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "NonLinearBearing"
)


__docformat__ = "restructuredtext en"
__all__ = ("NonLinearBearing",)


Self = TypeVar("Self", bound="NonLinearBearing")


class NonLinearBearing(_2127.BearingDesign):
    """NonLinearBearing

    This is a mastapy class.
    """

    TYPE = _NON_LINEAR_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NonLinearBearing")

    class _Cast_NonLinearBearing:
        """Special nested class for casting NonLinearBearing to subclasses."""

        def __init__(
            self: "NonLinearBearing._Cast_NonLinearBearing", parent: "NonLinearBearing"
        ):
            self._parent = parent

        @property
        def bearing_design(self: "NonLinearBearing._Cast_NonLinearBearing"):
            return self._parent._cast(_2127.BearingDesign)

        @property
        def detailed_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs import _2128

            return self._parent._cast(_2128.DetailedBearing)

        @property
        def angular_contact_ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2132

            return self._parent._cast(_2132.AngularContactBallBearing)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2133

            return self._parent._cast(_2133.AngularContactThrustBallBearing)

        @property
        def asymmetric_spherical_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2134

            return self._parent._cast(_2134.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2135

            return self._parent._cast(_2135.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2136

            return self._parent._cast(_2136.AxialThrustNeedleRollerBearing)

        @property
        def ball_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2137

            return self._parent._cast(_2137.BallBearing)

        @property
        def barrel_roller_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2139

            return self._parent._cast(_2139.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2145

            return self._parent._cast(_2145.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2146

            return self._parent._cast(_2146.CylindricalRollerBearing)

        @property
        def deep_groove_ball_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2147

            return self._parent._cast(_2147.DeepGrooveBallBearing)

        @property
        def four_point_contact_ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2151

            return self._parent._cast(_2151.FourPointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2156

            return self._parent._cast(_2156.MultiPointContactBallBearing)

        @property
        def needle_roller_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2157

            return self._parent._cast(_2157.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2158

            return self._parent._cast(_2158.NonBarrelRollerBearing)

        @property
        def roller_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2159

            return self._parent._cast(_2159.RollerBearing)

        @property
        def rolling_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2162

            return self._parent._cast(_2162.RollingBearing)

        @property
        def self_aligning_ball_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2163

            return self._parent._cast(_2163.SelfAligningBallBearing)

        @property
        def spherical_roller_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2166

            return self._parent._cast(_2166.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2167

            return self._parent._cast(_2167.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2168

            return self._parent._cast(_2168.TaperRollerBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.rolling import _2169

            return self._parent._cast(_2169.ThreePointContactBallBearing)

        @property
        def thrust_ball_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2170

            return self._parent._cast(_2170.ThrustBallBearing)

        @property
        def toroidal_roller_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.rolling import _2171

            return self._parent._cast(_2171.ToroidalRollerBearing)

        @property
        def pad_fluid_film_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.fluid_film import _2184

            return self._parent._cast(_2184.PadFluidFilmBearing)

        @property
        def plain_grease_filled_journal_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.fluid_film import _2186

            return self._parent._cast(_2186.PlainGreaseFilledJournalBearing)

        @property
        def plain_journal_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.fluid_film import _2188

            return self._parent._cast(_2188.PlainJournalBearing)

        @property
        def plain_oil_fed_journal_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.fluid_film import _2190

            return self._parent._cast(_2190.PlainOilFedJournalBearing)

        @property
        def tilting_pad_journal_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.fluid_film import _2191

            return self._parent._cast(_2191.TiltingPadJournalBearing)

        @property
        def tilting_pad_thrust_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.fluid_film import _2192

            return self._parent._cast(_2192.TiltingPadThrustBearing)

        @property
        def concept_axial_clearance_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.concept import _2194

            return self._parent._cast(_2194.ConceptAxialClearanceBearing)

        @property
        def concept_clearance_bearing(self: "NonLinearBearing._Cast_NonLinearBearing"):
            from mastapy.bearings.bearing_designs.concept import _2195

            return self._parent._cast(_2195.ConceptClearanceBearing)

        @property
        def concept_radial_clearance_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ):
            from mastapy.bearings.bearing_designs.concept import _2196

            return self._parent._cast(_2196.ConceptRadialClearanceBearing)

        @property
        def non_linear_bearing(
            self: "NonLinearBearing._Cast_NonLinearBearing",
        ) -> "NonLinearBearing":
            return self._parent

        def __getattr__(self: "NonLinearBearing._Cast_NonLinearBearing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NonLinearBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "NonLinearBearing._Cast_NonLinearBearing":
        return self._Cast_NonLinearBearing(self)
