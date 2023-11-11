"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1963 import BallBearingAnalysisMethod
    from ._1964 import BallBearingContactCalculation
    from ._1965 import BallBearingRaceContactGeometry
    from ._1966 import DIN7322010Results
    from ._1967 import ForceAtLaminaGroupReportable
    from ._1968 import ForceAtLaminaReportable
    from ._1969 import FrictionModelForGyroscopicMoment
    from ._1970 import InternalClearance
    from ._1971 import ISO14179Settings
    from ._1972 import ISO14179SettingsDatabase
    from ._1973 import ISO14179SettingsPerBearingType
    from ._1974 import ISO153122018Results
    from ._1975 import ISOTR1417912001Results
    from ._1976 import ISOTR141792001Results
    from ._1977 import ISOTR1417922001Results
    from ._1978 import LoadedAbstractSphericalRollerBearingStripLoadResults
    from ._1979 import LoadedAngularContactBallBearingElement
    from ._1980 import LoadedAngularContactBallBearingResults
    from ._1981 import LoadedAngularContactBallBearingRow
    from ._1982 import LoadedAngularContactThrustBallBearingElement
    from ._1983 import LoadedAngularContactThrustBallBearingResults
    from ._1984 import LoadedAngularContactThrustBallBearingRow
    from ._1985 import LoadedAsymmetricSphericalRollerBearingElement
    from ._1986 import LoadedAsymmetricSphericalRollerBearingResults
    from ._1987 import LoadedAsymmetricSphericalRollerBearingRow
    from ._1988 import LoadedAsymmetricSphericalRollerBearingStripLoadResults
    from ._1989 import LoadedAxialThrustCylindricalRollerBearingDutyCycle
    from ._1990 import LoadedAxialThrustCylindricalRollerBearingElement
    from ._1991 import LoadedAxialThrustCylindricalRollerBearingResults
    from ._1992 import LoadedAxialThrustCylindricalRollerBearingRow
    from ._1993 import LoadedAxialThrustNeedleRollerBearingElement
    from ._1994 import LoadedAxialThrustNeedleRollerBearingResults
    from ._1995 import LoadedAxialThrustNeedleRollerBearingRow
    from ._1996 import LoadedBallBearingDutyCycle
    from ._1997 import LoadedBallBearingElement
    from ._1998 import LoadedBallBearingRaceResults
    from ._1999 import LoadedBallBearingResults
    from ._2000 import LoadedBallBearingRow
    from ._2001 import LoadedCrossedRollerBearingElement
    from ._2002 import LoadedCrossedRollerBearingResults
    from ._2003 import LoadedCrossedRollerBearingRow
    from ._2004 import LoadedCylindricalRollerBearingDutyCycle
    from ._2005 import LoadedCylindricalRollerBearingElement
    from ._2006 import LoadedCylindricalRollerBearingResults
    from ._2007 import LoadedCylindricalRollerBearingRow
    from ._2008 import LoadedDeepGrooveBallBearingElement
    from ._2009 import LoadedDeepGrooveBallBearingResults
    from ._2010 import LoadedDeepGrooveBallBearingRow
    from ._2011 import LoadedElement
    from ._2012 import LoadedFourPointContactBallBearingElement
    from ._2013 import LoadedFourPointContactBallBearingRaceResults
    from ._2014 import LoadedFourPointContactBallBearingResults
    from ._2015 import LoadedFourPointContactBallBearingRow
    from ._2016 import LoadedMultiPointContactBallBearingElement
    from ._2017 import LoadedNeedleRollerBearingElement
    from ._2018 import LoadedNeedleRollerBearingResults
    from ._2019 import LoadedNeedleRollerBearingRow
    from ._2020 import LoadedNonBarrelRollerBearingDutyCycle
    from ._2021 import LoadedNonBarrelRollerBearingResults
    from ._2022 import LoadedNonBarrelRollerBearingRow
    from ._2023 import LoadedNonBarrelRollerBearingStripLoadResults
    from ._2024 import LoadedNonBarrelRollerElement
    from ._2025 import LoadedRollerBearingElement
    from ._2026 import LoadedRollerBearingResults
    from ._2027 import LoadedRollerBearingRow
    from ._2028 import LoadedRollerStripLoadResults
    from ._2029 import LoadedRollingBearingRaceResults
    from ._2030 import LoadedRollingBearingResults
    from ._2031 import LoadedRollingBearingRow
    from ._2032 import LoadedSelfAligningBallBearingElement
    from ._2033 import LoadedSelfAligningBallBearingResults
    from ._2034 import LoadedSelfAligningBallBearingRow
    from ._2035 import LoadedSphericalRadialRollerBearingElement
    from ._2036 import LoadedSphericalRollerBearingElement
    from ._2037 import LoadedSphericalRollerRadialBearingResults
    from ._2038 import LoadedSphericalRollerRadialBearingRow
    from ._2039 import LoadedSphericalRollerRadialBearingStripLoadResults
    from ._2040 import LoadedSphericalRollerThrustBearingResults
    from ._2041 import LoadedSphericalRollerThrustBearingRow
    from ._2042 import LoadedSphericalThrustRollerBearingElement
    from ._2043 import LoadedTaperRollerBearingDutyCycle
    from ._2044 import LoadedTaperRollerBearingElement
    from ._2045 import LoadedTaperRollerBearingResults
    from ._2046 import LoadedTaperRollerBearingRow
    from ._2047 import LoadedThreePointContactBallBearingElement
    from ._2048 import LoadedThreePointContactBallBearingResults
    from ._2049 import LoadedThreePointContactBallBearingRow
    from ._2050 import LoadedThrustBallBearingElement
    from ._2051 import LoadedThrustBallBearingResults
    from ._2052 import LoadedThrustBallBearingRow
    from ._2053 import LoadedToroidalRollerBearingElement
    from ._2054 import LoadedToroidalRollerBearingResults
    from ._2055 import LoadedToroidalRollerBearingRow
    from ._2056 import LoadedToroidalRollerBearingStripLoadResults
    from ._2057 import MaximumStaticContactStress
    from ._2058 import MaximumStaticContactStressDutyCycle
    from ._2059 import MaximumStaticContactStressResultsAbstract
    from ._2060 import MaxStripLoadStressObject
    from ._2061 import PermissibleContinuousAxialLoadResults
    from ._2062 import PowerRatingF1EstimationMethod
    from ._2063 import PreloadFactorLookupTable
    from ._2064 import ResultsAtRollerOffset
    from ._2065 import RingForceAndDisplacement
    from ._2066 import RollerAnalysisMethod
    from ._2067 import RollingBearingFrictionCoefficients
    from ._2068 import RollingBearingSpeedResults
    from ._2069 import SMTRibStressResults
    from ._2070 import StressAtPosition
    from ._2071 import ThreePointContactInternalClearance
    from ._2072 import TrackTruncationSafetyFactorResults
else:
    import_structure = {
        "_1963": ["BallBearingAnalysisMethod"],
        "_1964": ["BallBearingContactCalculation"],
        "_1965": ["BallBearingRaceContactGeometry"],
        "_1966": ["DIN7322010Results"],
        "_1967": ["ForceAtLaminaGroupReportable"],
        "_1968": ["ForceAtLaminaReportable"],
        "_1969": ["FrictionModelForGyroscopicMoment"],
        "_1970": ["InternalClearance"],
        "_1971": ["ISO14179Settings"],
        "_1972": ["ISO14179SettingsDatabase"],
        "_1973": ["ISO14179SettingsPerBearingType"],
        "_1974": ["ISO153122018Results"],
        "_1975": ["ISOTR1417912001Results"],
        "_1976": ["ISOTR141792001Results"],
        "_1977": ["ISOTR1417922001Results"],
        "_1978": ["LoadedAbstractSphericalRollerBearingStripLoadResults"],
        "_1979": ["LoadedAngularContactBallBearingElement"],
        "_1980": ["LoadedAngularContactBallBearingResults"],
        "_1981": ["LoadedAngularContactBallBearingRow"],
        "_1982": ["LoadedAngularContactThrustBallBearingElement"],
        "_1983": ["LoadedAngularContactThrustBallBearingResults"],
        "_1984": ["LoadedAngularContactThrustBallBearingRow"],
        "_1985": ["LoadedAsymmetricSphericalRollerBearingElement"],
        "_1986": ["LoadedAsymmetricSphericalRollerBearingResults"],
        "_1987": ["LoadedAsymmetricSphericalRollerBearingRow"],
        "_1988": ["LoadedAsymmetricSphericalRollerBearingStripLoadResults"],
        "_1989": ["LoadedAxialThrustCylindricalRollerBearingDutyCycle"],
        "_1990": ["LoadedAxialThrustCylindricalRollerBearingElement"],
        "_1991": ["LoadedAxialThrustCylindricalRollerBearingResults"],
        "_1992": ["LoadedAxialThrustCylindricalRollerBearingRow"],
        "_1993": ["LoadedAxialThrustNeedleRollerBearingElement"],
        "_1994": ["LoadedAxialThrustNeedleRollerBearingResults"],
        "_1995": ["LoadedAxialThrustNeedleRollerBearingRow"],
        "_1996": ["LoadedBallBearingDutyCycle"],
        "_1997": ["LoadedBallBearingElement"],
        "_1998": ["LoadedBallBearingRaceResults"],
        "_1999": ["LoadedBallBearingResults"],
        "_2000": ["LoadedBallBearingRow"],
        "_2001": ["LoadedCrossedRollerBearingElement"],
        "_2002": ["LoadedCrossedRollerBearingResults"],
        "_2003": ["LoadedCrossedRollerBearingRow"],
        "_2004": ["LoadedCylindricalRollerBearingDutyCycle"],
        "_2005": ["LoadedCylindricalRollerBearingElement"],
        "_2006": ["LoadedCylindricalRollerBearingResults"],
        "_2007": ["LoadedCylindricalRollerBearingRow"],
        "_2008": ["LoadedDeepGrooveBallBearingElement"],
        "_2009": ["LoadedDeepGrooveBallBearingResults"],
        "_2010": ["LoadedDeepGrooveBallBearingRow"],
        "_2011": ["LoadedElement"],
        "_2012": ["LoadedFourPointContactBallBearingElement"],
        "_2013": ["LoadedFourPointContactBallBearingRaceResults"],
        "_2014": ["LoadedFourPointContactBallBearingResults"],
        "_2015": ["LoadedFourPointContactBallBearingRow"],
        "_2016": ["LoadedMultiPointContactBallBearingElement"],
        "_2017": ["LoadedNeedleRollerBearingElement"],
        "_2018": ["LoadedNeedleRollerBearingResults"],
        "_2019": ["LoadedNeedleRollerBearingRow"],
        "_2020": ["LoadedNonBarrelRollerBearingDutyCycle"],
        "_2021": ["LoadedNonBarrelRollerBearingResults"],
        "_2022": ["LoadedNonBarrelRollerBearingRow"],
        "_2023": ["LoadedNonBarrelRollerBearingStripLoadResults"],
        "_2024": ["LoadedNonBarrelRollerElement"],
        "_2025": ["LoadedRollerBearingElement"],
        "_2026": ["LoadedRollerBearingResults"],
        "_2027": ["LoadedRollerBearingRow"],
        "_2028": ["LoadedRollerStripLoadResults"],
        "_2029": ["LoadedRollingBearingRaceResults"],
        "_2030": ["LoadedRollingBearingResults"],
        "_2031": ["LoadedRollingBearingRow"],
        "_2032": ["LoadedSelfAligningBallBearingElement"],
        "_2033": ["LoadedSelfAligningBallBearingResults"],
        "_2034": ["LoadedSelfAligningBallBearingRow"],
        "_2035": ["LoadedSphericalRadialRollerBearingElement"],
        "_2036": ["LoadedSphericalRollerBearingElement"],
        "_2037": ["LoadedSphericalRollerRadialBearingResults"],
        "_2038": ["LoadedSphericalRollerRadialBearingRow"],
        "_2039": ["LoadedSphericalRollerRadialBearingStripLoadResults"],
        "_2040": ["LoadedSphericalRollerThrustBearingResults"],
        "_2041": ["LoadedSphericalRollerThrustBearingRow"],
        "_2042": ["LoadedSphericalThrustRollerBearingElement"],
        "_2043": ["LoadedTaperRollerBearingDutyCycle"],
        "_2044": ["LoadedTaperRollerBearingElement"],
        "_2045": ["LoadedTaperRollerBearingResults"],
        "_2046": ["LoadedTaperRollerBearingRow"],
        "_2047": ["LoadedThreePointContactBallBearingElement"],
        "_2048": ["LoadedThreePointContactBallBearingResults"],
        "_2049": ["LoadedThreePointContactBallBearingRow"],
        "_2050": ["LoadedThrustBallBearingElement"],
        "_2051": ["LoadedThrustBallBearingResults"],
        "_2052": ["LoadedThrustBallBearingRow"],
        "_2053": ["LoadedToroidalRollerBearingElement"],
        "_2054": ["LoadedToroidalRollerBearingResults"],
        "_2055": ["LoadedToroidalRollerBearingRow"],
        "_2056": ["LoadedToroidalRollerBearingStripLoadResults"],
        "_2057": ["MaximumStaticContactStress"],
        "_2058": ["MaximumStaticContactStressDutyCycle"],
        "_2059": ["MaximumStaticContactStressResultsAbstract"],
        "_2060": ["MaxStripLoadStressObject"],
        "_2061": ["PermissibleContinuousAxialLoadResults"],
        "_2062": ["PowerRatingF1EstimationMethod"],
        "_2063": ["PreloadFactorLookupTable"],
        "_2064": ["ResultsAtRollerOffset"],
        "_2065": ["RingForceAndDisplacement"],
        "_2066": ["RollerAnalysisMethod"],
        "_2067": ["RollingBearingFrictionCoefficients"],
        "_2068": ["RollingBearingSpeedResults"],
        "_2069": ["SMTRibStressResults"],
        "_2070": ["StressAtPosition"],
        "_2071": ["ThreePointContactInternalClearance"],
        "_2072": ["TrackTruncationSafetyFactorResults"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BallBearingAnalysisMethod",
    "BallBearingContactCalculation",
    "BallBearingRaceContactGeometry",
    "DIN7322010Results",
    "ForceAtLaminaGroupReportable",
    "ForceAtLaminaReportable",
    "FrictionModelForGyroscopicMoment",
    "InternalClearance",
    "ISO14179Settings",
    "ISO14179SettingsDatabase",
    "ISO14179SettingsPerBearingType",
    "ISO153122018Results",
    "ISOTR1417912001Results",
    "ISOTR141792001Results",
    "ISOTR1417922001Results",
    "LoadedAbstractSphericalRollerBearingStripLoadResults",
    "LoadedAngularContactBallBearingElement",
    "LoadedAngularContactBallBearingResults",
    "LoadedAngularContactBallBearingRow",
    "LoadedAngularContactThrustBallBearingElement",
    "LoadedAngularContactThrustBallBearingResults",
    "LoadedAngularContactThrustBallBearingRow",
    "LoadedAsymmetricSphericalRollerBearingElement",
    "LoadedAsymmetricSphericalRollerBearingResults",
    "LoadedAsymmetricSphericalRollerBearingRow",
    "LoadedAsymmetricSphericalRollerBearingStripLoadResults",
    "LoadedAxialThrustCylindricalRollerBearingDutyCycle",
    "LoadedAxialThrustCylindricalRollerBearingElement",
    "LoadedAxialThrustCylindricalRollerBearingResults",
    "LoadedAxialThrustCylindricalRollerBearingRow",
    "LoadedAxialThrustNeedleRollerBearingElement",
    "LoadedAxialThrustNeedleRollerBearingResults",
    "LoadedAxialThrustNeedleRollerBearingRow",
    "LoadedBallBearingDutyCycle",
    "LoadedBallBearingElement",
    "LoadedBallBearingRaceResults",
    "LoadedBallBearingResults",
    "LoadedBallBearingRow",
    "LoadedCrossedRollerBearingElement",
    "LoadedCrossedRollerBearingResults",
    "LoadedCrossedRollerBearingRow",
    "LoadedCylindricalRollerBearingDutyCycle",
    "LoadedCylindricalRollerBearingElement",
    "LoadedCylindricalRollerBearingResults",
    "LoadedCylindricalRollerBearingRow",
    "LoadedDeepGrooveBallBearingElement",
    "LoadedDeepGrooveBallBearingResults",
    "LoadedDeepGrooveBallBearingRow",
    "LoadedElement",
    "LoadedFourPointContactBallBearingElement",
    "LoadedFourPointContactBallBearingRaceResults",
    "LoadedFourPointContactBallBearingResults",
    "LoadedFourPointContactBallBearingRow",
    "LoadedMultiPointContactBallBearingElement",
    "LoadedNeedleRollerBearingElement",
    "LoadedNeedleRollerBearingResults",
    "LoadedNeedleRollerBearingRow",
    "LoadedNonBarrelRollerBearingDutyCycle",
    "LoadedNonBarrelRollerBearingResults",
    "LoadedNonBarrelRollerBearingRow",
    "LoadedNonBarrelRollerBearingStripLoadResults",
    "LoadedNonBarrelRollerElement",
    "LoadedRollerBearingElement",
    "LoadedRollerBearingResults",
    "LoadedRollerBearingRow",
    "LoadedRollerStripLoadResults",
    "LoadedRollingBearingRaceResults",
    "LoadedRollingBearingResults",
    "LoadedRollingBearingRow",
    "LoadedSelfAligningBallBearingElement",
    "LoadedSelfAligningBallBearingResults",
    "LoadedSelfAligningBallBearingRow",
    "LoadedSphericalRadialRollerBearingElement",
    "LoadedSphericalRollerBearingElement",
    "LoadedSphericalRollerRadialBearingResults",
    "LoadedSphericalRollerRadialBearingRow",
    "LoadedSphericalRollerRadialBearingStripLoadResults",
    "LoadedSphericalRollerThrustBearingResults",
    "LoadedSphericalRollerThrustBearingRow",
    "LoadedSphericalThrustRollerBearingElement",
    "LoadedTaperRollerBearingDutyCycle",
    "LoadedTaperRollerBearingElement",
    "LoadedTaperRollerBearingResults",
    "LoadedTaperRollerBearingRow",
    "LoadedThreePointContactBallBearingElement",
    "LoadedThreePointContactBallBearingResults",
    "LoadedThreePointContactBallBearingRow",
    "LoadedThrustBallBearingElement",
    "LoadedThrustBallBearingResults",
    "LoadedThrustBallBearingRow",
    "LoadedToroidalRollerBearingElement",
    "LoadedToroidalRollerBearingResults",
    "LoadedToroidalRollerBearingRow",
    "LoadedToroidalRollerBearingStripLoadResults",
    "MaximumStaticContactStress",
    "MaximumStaticContactStressDutyCycle",
    "MaximumStaticContactStressResultsAbstract",
    "MaxStripLoadStressObject",
    "PermissibleContinuousAxialLoadResults",
    "PowerRatingF1EstimationMethod",
    "PreloadFactorLookupTable",
    "ResultsAtRollerOffset",
    "RingForceAndDisplacement",
    "RollerAnalysisMethod",
    "RollingBearingFrictionCoefficients",
    "RollingBearingSpeedResults",
    "SMTRibStressResults",
    "StressAtPosition",
    "ThreePointContactInternalClearance",
    "TrackTruncationSafetyFactorResults",
)
