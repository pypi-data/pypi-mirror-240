"""DataScalingOptions"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import enum_with_selected_value
from mastapy.math_utility import _1502
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.utility.units_and_measurements.measurements import (
    _1609,
    _1610,
    _1614,
    _1618,
    _1626,
    _1633,
    _1639,
    _1645,
    _1673,
    _1681,
    _1662,
    _1686,
    _1687,
    _1691,
    _1690,
    _1696,
    _1706,
    _1664,
    _1720,
    _1612,
    _1636,
    _1729,
    _1711,
    _1712,
    _1723,
    _1724,
    _1722,
    _1685,
    _1728,
    _1667,
    _1721,
    _1613,
)
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATA_SCALING_OPTIONS = python_net_import(
    "SMT.MastaAPI.MathUtility.MeasuredDataScaling", "DataScalingOptions"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1486
    from mastapy.math_utility.measured_data_scaling import _1567


__docformat__ = "restructuredtext en"
__all__ = ("DataScalingOptions",)


Self = TypeVar("Self", bound="DataScalingOptions")


class DataScalingOptions(_0.APIBase):
    """DataScalingOptions

    This is a mastapy class.
    """

    TYPE = _DATA_SCALING_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DataScalingOptions")

    class _Cast_DataScalingOptions:
        """Special nested class for casting DataScalingOptions to subclasses."""

        def __init__(
            self: "DataScalingOptions._Cast_DataScalingOptions",
            parent: "DataScalingOptions",
        ):
            self._parent = parent

        @property
        def data_scaling_options(
            self: "DataScalingOptions._Cast_DataScalingOptions",
        ) -> "DataScalingOptions":
            return self._parent

        def __getattr__(self: "DataScalingOptions._Cast_DataScalingOptions", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DataScalingOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_scaling(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling":
        """EnumWithSelectedValue[mastapy.math_utility.DynamicsResponseScaling]"""
        temp = self.wrapped.DynamicScaling

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @dynamic_scaling.setter
    @enforce_parameter_types
    def dynamic_scaling(self: Self, value: "_1502.DynamicsResponseScaling"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DynamicScaling = value

    @property
    def weighting(self: Self) -> "_1486.AcousticWeighting":
        """mastapy.math_utility.AcousticWeighting"""
        temp = self.wrapped.Weighting

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.MathUtility.AcousticWeighting"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.math_utility._1486", "AcousticWeighting"
        )(value)

    @weighting.setter
    @enforce_parameter_types
    def weighting(self: Self, value: "_1486.AcousticWeighting"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.MathUtility.AcousticWeighting"
        )
        self.wrapped.Weighting = value

    @property
    def acceleration_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1609.Acceleration]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Acceleration]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AccelerationReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1609.Acceleration](temp)

    @property
    def angle_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1610.Angle]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Angle]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngleReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1610.Angle](temp)

    @property
    def angular_acceleration_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1614.AngularAcceleration]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.AngularAcceleration]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularAccelerationReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1614.AngularAcceleration](
            temp
        )

    @property
    def angular_velocity_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1618.AngularVelocity]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.AngularVelocity]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularVelocityReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1618.AngularVelocity](temp)

    @property
    def damage_rate(self: Self) -> "_1567.DataScalingReferenceValues[_1626.DamageRate]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.DamageRate]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DamageRate

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1626.DamageRate](temp)

    @property
    def energy_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1633.Energy]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Energy]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1633.Energy](temp)

    @property
    def force_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1639.Force]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Force]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1639.Force](temp)

    @property
    def frequency_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1645.Frequency]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Frequency]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FrequencyReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1645.Frequency](temp)

    @property
    def linear_stiffness_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1673.LinearStiffness]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.LinearStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearStiffnessReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1673.LinearStiffness](temp)

    @property
    def mass_per_unit_time_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1681.MassPerUnitTime]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.MassPerUnitTime]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPerUnitTimeReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1681.MassPerUnitTime](temp)

    @property
    def medium_length_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1662.LengthMedium]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.LengthMedium]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MediumLengthReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1662.LengthMedium](temp)

    @property
    def percentage(self: Self) -> "_1567.DataScalingReferenceValues[_1686.Percentage]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Percentage]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Percentage

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1686.Percentage](temp)

    @property
    def power_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1687.Power]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Power]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1687.Power](temp)

    @property
    def power_small_per_unit_area_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1691.PowerSmallPerArea]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.PowerSmallPerArea]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerSmallPerUnitAreaReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1691.PowerSmallPerArea](
            temp
        )

    @property
    def power_small_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1690.PowerSmall]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.PowerSmall]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerSmallReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1690.PowerSmall](temp)

    @property
    def pressure_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1696.Pressure]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Pressure]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PressureReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1696.Pressure](temp)

    @property
    def safety_factor(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1706.SafetyFactor]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.SafetyFactor]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SafetyFactor

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1706.SafetyFactor](temp)

    @property
    def short_length_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1664.LengthShort]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.LengthShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShortLengthReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1664.LengthShort](temp)

    @property
    def short_time_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1720.TimeShort]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.TimeShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShortTimeReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1720.TimeShort](temp)

    @property
    def small_angle_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1612.AngleSmall]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.AngleSmall]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallAngleReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1612.AngleSmall](temp)

    @property
    def small_energy_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1636.EnergySmall]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.EnergySmall]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallEnergyReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1636.EnergySmall](temp)

    @property
    def small_velocity_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1729.VelocitySmall]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.VelocitySmall]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SmallVelocityReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1729.VelocitySmall](temp)

    @property
    def stress_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1711.Stress]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Stress]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StressReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1711.Stress](temp)

    @property
    def temperature_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1712.Temperature]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Temperature]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TemperatureReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1712.Temperature](temp)

    @property
    def torque_converter_inverse_k(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1723.TorqueConverterInverseK]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.TorqueConverterInverseK]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueConverterInverseK

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[
            _1723.TorqueConverterInverseK
        ](temp)

    @property
    def torque_converter_k(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1724.TorqueConverterK]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.TorqueConverterK]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueConverterK

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1724.TorqueConverterK](
            temp
        )

    @property
    def torque_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1722.Torque]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Torque]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1722.Torque](temp)

    @property
    def unmeasureable(self: Self) -> "_1567.DataScalingReferenceValues[_1685.Number]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Number]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Unmeasureable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1685.Number](temp)

    @property
    def velocity_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1728.Velocity]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.Velocity]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VelocityReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1728.Velocity](temp)

    @property
    def very_short_length_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1667.LengthVeryShort]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.LengthVeryShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VeryShortLengthReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1667.LengthVeryShort](temp)

    @property
    def very_short_time_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1721.TimeVeryShort]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.TimeVeryShort]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VeryShortTimeReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1721.TimeVeryShort](temp)

    @property
    def very_small_angle_reference_values(
        self: Self,
    ) -> "_1567.DataScalingReferenceValues[_1613.AngleVerySmall]":
        """mastapy.math_utility.measured_data_scaling.DataScalingReferenceValues[mastapy.utility.units_and_measurements.measurements.AngleVerySmall]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VerySmallAngleReferenceValues

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1613.AngleVerySmall](temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(self: Self) -> "DataScalingOptions._Cast_DataScalingOptions":
        return self._Cast_DataScalingOptions(self)
