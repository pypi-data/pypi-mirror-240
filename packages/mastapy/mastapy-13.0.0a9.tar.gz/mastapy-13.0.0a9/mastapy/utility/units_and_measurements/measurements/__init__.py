"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1609 import Acceleration
    from ._1610 import Angle
    from ._1611 import AnglePerUnitTemperature
    from ._1612 import AngleSmall
    from ._1613 import AngleVerySmall
    from ._1614 import AngularAcceleration
    from ._1615 import AngularCompliance
    from ._1616 import AngularJerk
    from ._1617 import AngularStiffness
    from ._1618 import AngularVelocity
    from ._1619 import Area
    from ._1620 import AreaSmall
    from ._1621 import CarbonEmissionFactor
    from ._1622 import CurrentDensity
    from ._1623 import CurrentPerLength
    from ._1624 import Cycles
    from ._1625 import Damage
    from ._1626 import DamageRate
    from ._1627 import DataSize
    from ._1628 import Decibel
    from ._1629 import Density
    from ._1630 import ElectricalResistance
    from ._1631 import ElectricalResistivity
    from ._1632 import ElectricCurrent
    from ._1633 import Energy
    from ._1634 import EnergyPerUnitArea
    from ._1635 import EnergyPerUnitAreaSmall
    from ._1636 import EnergySmall
    from ._1637 import Enum
    from ._1638 import FlowRate
    from ._1639 import Force
    from ._1640 import ForcePerUnitLength
    from ._1641 import ForcePerUnitPressure
    from ._1642 import ForcePerUnitTemperature
    from ._1643 import FractionMeasurementBase
    from ._1644 import FractionPerTemperature
    from ._1645 import Frequency
    from ._1646 import FuelConsumptionEngine
    from ._1647 import FuelEfficiencyVehicle
    from ._1648 import Gradient
    from ._1649 import HeatConductivity
    from ._1650 import HeatTransfer
    from ._1651 import HeatTransferCoefficientForPlasticGearTooth
    from ._1652 import HeatTransferResistance
    from ._1653 import Impulse
    from ._1654 import Index
    from ._1655 import Inductance
    from ._1656 import Integer
    from ._1657 import InverseShortLength
    from ._1658 import InverseShortTime
    from ._1659 import Jerk
    from ._1660 import KinematicViscosity
    from ._1661 import LengthLong
    from ._1662 import LengthMedium
    from ._1663 import LengthPerUnitTemperature
    from ._1664 import LengthShort
    from ._1665 import LengthToTheFourth
    from ._1666 import LengthVeryLong
    from ._1667 import LengthVeryShort
    from ._1668 import LengthVeryShortPerLengthShort
    from ._1669 import LinearAngularDamping
    from ._1670 import LinearAngularStiffnessCrossTerm
    from ._1671 import LinearDamping
    from ._1672 import LinearFlexibility
    from ._1673 import LinearStiffness
    from ._1674 import MagneticFieldStrength
    from ._1675 import MagneticFlux
    from ._1676 import MagneticFluxDensity
    from ._1677 import MagneticVectorPotential
    from ._1678 import MagnetomotiveForce
    from ._1679 import Mass
    from ._1680 import MassPerUnitLength
    from ._1681 import MassPerUnitTime
    from ._1682 import MomentOfInertia
    from ._1683 import MomentOfInertiaPerUnitLength
    from ._1684 import MomentPerUnitPressure
    from ._1685 import Number
    from ._1686 import Percentage
    from ._1687 import Power
    from ._1688 import PowerPerSmallArea
    from ._1689 import PowerPerUnitTime
    from ._1690 import PowerSmall
    from ._1691 import PowerSmallPerArea
    from ._1692 import PowerSmallPerMass
    from ._1693 import PowerSmallPerUnitAreaPerUnitTime
    from ._1694 import PowerSmallPerUnitTime
    from ._1695 import PowerSmallPerVolume
    from ._1696 import Pressure
    from ._1697 import PressurePerUnitTime
    from ._1698 import PressureVelocityProduct
    from ._1699 import PressureViscosityCoefficient
    from ._1700 import Price
    from ._1701 import PricePerUnitMass
    from ._1702 import QuadraticAngularDamping
    from ._1703 import QuadraticDrag
    from ._1704 import RescaledMeasurement
    from ._1705 import Rotatum
    from ._1706 import SafetyFactor
    from ._1707 import SpecificAcousticImpedance
    from ._1708 import SpecificHeat
    from ._1709 import SquareRootOfUnitForcePerUnitArea
    from ._1710 import StiffnessPerUnitFaceWidth
    from ._1711 import Stress
    from ._1712 import Temperature
    from ._1713 import TemperatureDifference
    from ._1714 import TemperaturePerUnitTime
    from ._1715 import Text
    from ._1716 import ThermalContactCoefficient
    from ._1717 import ThermalExpansionCoefficient
    from ._1718 import ThermoElasticFactor
    from ._1719 import Time
    from ._1720 import TimeShort
    from ._1721 import TimeVeryShort
    from ._1722 import Torque
    from ._1723 import TorqueConverterInverseK
    from ._1724 import TorqueConverterK
    from ._1725 import TorquePerCurrent
    from ._1726 import TorquePerSquareRootOfPower
    from ._1727 import TorquePerUnitTemperature
    from ._1728 import Velocity
    from ._1729 import VelocitySmall
    from ._1730 import Viscosity
    from ._1731 import Voltage
    from ._1732 import VoltagePerAngularVelocity
    from ._1733 import Volume
    from ._1734 import WearCoefficient
    from ._1735 import Yank
else:
    import_structure = {
        "_1609": ["Acceleration"],
        "_1610": ["Angle"],
        "_1611": ["AnglePerUnitTemperature"],
        "_1612": ["AngleSmall"],
        "_1613": ["AngleVerySmall"],
        "_1614": ["AngularAcceleration"],
        "_1615": ["AngularCompliance"],
        "_1616": ["AngularJerk"],
        "_1617": ["AngularStiffness"],
        "_1618": ["AngularVelocity"],
        "_1619": ["Area"],
        "_1620": ["AreaSmall"],
        "_1621": ["CarbonEmissionFactor"],
        "_1622": ["CurrentDensity"],
        "_1623": ["CurrentPerLength"],
        "_1624": ["Cycles"],
        "_1625": ["Damage"],
        "_1626": ["DamageRate"],
        "_1627": ["DataSize"],
        "_1628": ["Decibel"],
        "_1629": ["Density"],
        "_1630": ["ElectricalResistance"],
        "_1631": ["ElectricalResistivity"],
        "_1632": ["ElectricCurrent"],
        "_1633": ["Energy"],
        "_1634": ["EnergyPerUnitArea"],
        "_1635": ["EnergyPerUnitAreaSmall"],
        "_1636": ["EnergySmall"],
        "_1637": ["Enum"],
        "_1638": ["FlowRate"],
        "_1639": ["Force"],
        "_1640": ["ForcePerUnitLength"],
        "_1641": ["ForcePerUnitPressure"],
        "_1642": ["ForcePerUnitTemperature"],
        "_1643": ["FractionMeasurementBase"],
        "_1644": ["FractionPerTemperature"],
        "_1645": ["Frequency"],
        "_1646": ["FuelConsumptionEngine"],
        "_1647": ["FuelEfficiencyVehicle"],
        "_1648": ["Gradient"],
        "_1649": ["HeatConductivity"],
        "_1650": ["HeatTransfer"],
        "_1651": ["HeatTransferCoefficientForPlasticGearTooth"],
        "_1652": ["HeatTransferResistance"],
        "_1653": ["Impulse"],
        "_1654": ["Index"],
        "_1655": ["Inductance"],
        "_1656": ["Integer"],
        "_1657": ["InverseShortLength"],
        "_1658": ["InverseShortTime"],
        "_1659": ["Jerk"],
        "_1660": ["KinematicViscosity"],
        "_1661": ["LengthLong"],
        "_1662": ["LengthMedium"],
        "_1663": ["LengthPerUnitTemperature"],
        "_1664": ["LengthShort"],
        "_1665": ["LengthToTheFourth"],
        "_1666": ["LengthVeryLong"],
        "_1667": ["LengthVeryShort"],
        "_1668": ["LengthVeryShortPerLengthShort"],
        "_1669": ["LinearAngularDamping"],
        "_1670": ["LinearAngularStiffnessCrossTerm"],
        "_1671": ["LinearDamping"],
        "_1672": ["LinearFlexibility"],
        "_1673": ["LinearStiffness"],
        "_1674": ["MagneticFieldStrength"],
        "_1675": ["MagneticFlux"],
        "_1676": ["MagneticFluxDensity"],
        "_1677": ["MagneticVectorPotential"],
        "_1678": ["MagnetomotiveForce"],
        "_1679": ["Mass"],
        "_1680": ["MassPerUnitLength"],
        "_1681": ["MassPerUnitTime"],
        "_1682": ["MomentOfInertia"],
        "_1683": ["MomentOfInertiaPerUnitLength"],
        "_1684": ["MomentPerUnitPressure"],
        "_1685": ["Number"],
        "_1686": ["Percentage"],
        "_1687": ["Power"],
        "_1688": ["PowerPerSmallArea"],
        "_1689": ["PowerPerUnitTime"],
        "_1690": ["PowerSmall"],
        "_1691": ["PowerSmallPerArea"],
        "_1692": ["PowerSmallPerMass"],
        "_1693": ["PowerSmallPerUnitAreaPerUnitTime"],
        "_1694": ["PowerSmallPerUnitTime"],
        "_1695": ["PowerSmallPerVolume"],
        "_1696": ["Pressure"],
        "_1697": ["PressurePerUnitTime"],
        "_1698": ["PressureVelocityProduct"],
        "_1699": ["PressureViscosityCoefficient"],
        "_1700": ["Price"],
        "_1701": ["PricePerUnitMass"],
        "_1702": ["QuadraticAngularDamping"],
        "_1703": ["QuadraticDrag"],
        "_1704": ["RescaledMeasurement"],
        "_1705": ["Rotatum"],
        "_1706": ["SafetyFactor"],
        "_1707": ["SpecificAcousticImpedance"],
        "_1708": ["SpecificHeat"],
        "_1709": ["SquareRootOfUnitForcePerUnitArea"],
        "_1710": ["StiffnessPerUnitFaceWidth"],
        "_1711": ["Stress"],
        "_1712": ["Temperature"],
        "_1713": ["TemperatureDifference"],
        "_1714": ["TemperaturePerUnitTime"],
        "_1715": ["Text"],
        "_1716": ["ThermalContactCoefficient"],
        "_1717": ["ThermalExpansionCoefficient"],
        "_1718": ["ThermoElasticFactor"],
        "_1719": ["Time"],
        "_1720": ["TimeShort"],
        "_1721": ["TimeVeryShort"],
        "_1722": ["Torque"],
        "_1723": ["TorqueConverterInverseK"],
        "_1724": ["TorqueConverterK"],
        "_1725": ["TorquePerCurrent"],
        "_1726": ["TorquePerSquareRootOfPower"],
        "_1727": ["TorquePerUnitTemperature"],
        "_1728": ["Velocity"],
        "_1729": ["VelocitySmall"],
        "_1730": ["Viscosity"],
        "_1731": ["Voltage"],
        "_1732": ["VoltagePerAngularVelocity"],
        "_1733": ["Volume"],
        "_1734": ["WearCoefficient"],
        "_1735": ["Yank"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Acceleration",
    "Angle",
    "AnglePerUnitTemperature",
    "AngleSmall",
    "AngleVerySmall",
    "AngularAcceleration",
    "AngularCompliance",
    "AngularJerk",
    "AngularStiffness",
    "AngularVelocity",
    "Area",
    "AreaSmall",
    "CarbonEmissionFactor",
    "CurrentDensity",
    "CurrentPerLength",
    "Cycles",
    "Damage",
    "DamageRate",
    "DataSize",
    "Decibel",
    "Density",
    "ElectricalResistance",
    "ElectricalResistivity",
    "ElectricCurrent",
    "Energy",
    "EnergyPerUnitArea",
    "EnergyPerUnitAreaSmall",
    "EnergySmall",
    "Enum",
    "FlowRate",
    "Force",
    "ForcePerUnitLength",
    "ForcePerUnitPressure",
    "ForcePerUnitTemperature",
    "FractionMeasurementBase",
    "FractionPerTemperature",
    "Frequency",
    "FuelConsumptionEngine",
    "FuelEfficiencyVehicle",
    "Gradient",
    "HeatConductivity",
    "HeatTransfer",
    "HeatTransferCoefficientForPlasticGearTooth",
    "HeatTransferResistance",
    "Impulse",
    "Index",
    "Inductance",
    "Integer",
    "InverseShortLength",
    "InverseShortTime",
    "Jerk",
    "KinematicViscosity",
    "LengthLong",
    "LengthMedium",
    "LengthPerUnitTemperature",
    "LengthShort",
    "LengthToTheFourth",
    "LengthVeryLong",
    "LengthVeryShort",
    "LengthVeryShortPerLengthShort",
    "LinearAngularDamping",
    "LinearAngularStiffnessCrossTerm",
    "LinearDamping",
    "LinearFlexibility",
    "LinearStiffness",
    "MagneticFieldStrength",
    "MagneticFlux",
    "MagneticFluxDensity",
    "MagneticVectorPotential",
    "MagnetomotiveForce",
    "Mass",
    "MassPerUnitLength",
    "MassPerUnitTime",
    "MomentOfInertia",
    "MomentOfInertiaPerUnitLength",
    "MomentPerUnitPressure",
    "Number",
    "Percentage",
    "Power",
    "PowerPerSmallArea",
    "PowerPerUnitTime",
    "PowerSmall",
    "PowerSmallPerArea",
    "PowerSmallPerMass",
    "PowerSmallPerUnitAreaPerUnitTime",
    "PowerSmallPerUnitTime",
    "PowerSmallPerVolume",
    "Pressure",
    "PressurePerUnitTime",
    "PressureVelocityProduct",
    "PressureViscosityCoefficient",
    "Price",
    "PricePerUnitMass",
    "QuadraticAngularDamping",
    "QuadraticDrag",
    "RescaledMeasurement",
    "Rotatum",
    "SafetyFactor",
    "SpecificAcousticImpedance",
    "SpecificHeat",
    "SquareRootOfUnitForcePerUnitArea",
    "StiffnessPerUnitFaceWidth",
    "Stress",
    "Temperature",
    "TemperatureDifference",
    "TemperaturePerUnitTime",
    "Text",
    "ThermalContactCoefficient",
    "ThermalExpansionCoefficient",
    "ThermoElasticFactor",
    "Time",
    "TimeShort",
    "TimeVeryShort",
    "Torque",
    "TorqueConverterInverseK",
    "TorqueConverterK",
    "TorquePerCurrent",
    "TorquePerSquareRootOfPower",
    "TorquePerUnitTemperature",
    "Velocity",
    "VelocitySmall",
    "Viscosity",
    "Voltage",
    "VoltagePerAngularVelocity",
    "Volume",
    "WearCoefficient",
    "Yank",
)
