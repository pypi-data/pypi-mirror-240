"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1485 import Range
    from ._1486 import AcousticWeighting
    from ._1487 import AlignmentAxis
    from ._1488 import Axis
    from ._1489 import CirclesOnAxis
    from ._1490 import ComplexMatrix
    from ._1491 import ComplexPartDisplayOption
    from ._1492 import ComplexVector
    from ._1493 import ComplexVector3D
    from ._1494 import ComplexVector6D
    from ._1495 import CoordinateSystem3D
    from ._1496 import CoordinateSystemEditor
    from ._1497 import CoordinateSystemForRotation
    from ._1498 import CoordinateSystemForRotationOrigin
    from ._1499 import DataPrecision
    from ._1500 import DegreeOfFreedom
    from ._1501 import DynamicsResponseScalarResult
    from ._1502 import DynamicsResponseScaling
    from ._1503 import Eigenmode
    from ._1504 import Eigenmodes
    from ._1505 import EulerParameters
    from ._1506 import ExtrapolationOptions
    from ._1507 import FacetedBody
    from ._1508 import FacetedSurface
    from ._1509 import FourierSeries
    from ._1510 import GenericMatrix
    from ._1511 import GriddedSurface
    from ._1512 import HarmonicValue
    from ._1513 import InertiaTensor
    from ._1514 import MassProperties
    from ._1515 import MaxMinMean
    from ._1516 import ComplexMagnitudeMethod
    from ._1517 import MultipleFourierSeriesInterpolator
    from ._1518 import Named2DLocation
    from ._1519 import PIDControlUpdateMethod
    from ._1520 import Quaternion
    from ._1521 import RealMatrix
    from ._1522 import RealVector
    from ._1523 import ResultOptionsFor3DVector
    from ._1524 import RotationAxis
    from ._1525 import RoundedOrder
    from ._1526 import SinCurve
    from ._1527 import SquareMatrix
    from ._1528 import StressPoint
    from ._1529 import TransformMatrix3D
    from ._1530 import TranslationRotation
    from ._1531 import Vector2DListAccessor
    from ._1532 import Vector6D
else:
    import_structure = {
        "_1485": ["Range"],
        "_1486": ["AcousticWeighting"],
        "_1487": ["AlignmentAxis"],
        "_1488": ["Axis"],
        "_1489": ["CirclesOnAxis"],
        "_1490": ["ComplexMatrix"],
        "_1491": ["ComplexPartDisplayOption"],
        "_1492": ["ComplexVector"],
        "_1493": ["ComplexVector3D"],
        "_1494": ["ComplexVector6D"],
        "_1495": ["CoordinateSystem3D"],
        "_1496": ["CoordinateSystemEditor"],
        "_1497": ["CoordinateSystemForRotation"],
        "_1498": ["CoordinateSystemForRotationOrigin"],
        "_1499": ["DataPrecision"],
        "_1500": ["DegreeOfFreedom"],
        "_1501": ["DynamicsResponseScalarResult"],
        "_1502": ["DynamicsResponseScaling"],
        "_1503": ["Eigenmode"],
        "_1504": ["Eigenmodes"],
        "_1505": ["EulerParameters"],
        "_1506": ["ExtrapolationOptions"],
        "_1507": ["FacetedBody"],
        "_1508": ["FacetedSurface"],
        "_1509": ["FourierSeries"],
        "_1510": ["GenericMatrix"],
        "_1511": ["GriddedSurface"],
        "_1512": ["HarmonicValue"],
        "_1513": ["InertiaTensor"],
        "_1514": ["MassProperties"],
        "_1515": ["MaxMinMean"],
        "_1516": ["ComplexMagnitudeMethod"],
        "_1517": ["MultipleFourierSeriesInterpolator"],
        "_1518": ["Named2DLocation"],
        "_1519": ["PIDControlUpdateMethod"],
        "_1520": ["Quaternion"],
        "_1521": ["RealMatrix"],
        "_1522": ["RealVector"],
        "_1523": ["ResultOptionsFor3DVector"],
        "_1524": ["RotationAxis"],
        "_1525": ["RoundedOrder"],
        "_1526": ["SinCurve"],
        "_1527": ["SquareMatrix"],
        "_1528": ["StressPoint"],
        "_1529": ["TransformMatrix3D"],
        "_1530": ["TranslationRotation"],
        "_1531": ["Vector2DListAccessor"],
        "_1532": ["Vector6D"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Range",
    "AcousticWeighting",
    "AlignmentAxis",
    "Axis",
    "CirclesOnAxis",
    "ComplexMatrix",
    "ComplexPartDisplayOption",
    "ComplexVector",
    "ComplexVector3D",
    "ComplexVector6D",
    "CoordinateSystem3D",
    "CoordinateSystemEditor",
    "CoordinateSystemForRotation",
    "CoordinateSystemForRotationOrigin",
    "DataPrecision",
    "DegreeOfFreedom",
    "DynamicsResponseScalarResult",
    "DynamicsResponseScaling",
    "Eigenmode",
    "Eigenmodes",
    "EulerParameters",
    "ExtrapolationOptions",
    "FacetedBody",
    "FacetedSurface",
    "FourierSeries",
    "GenericMatrix",
    "GriddedSurface",
    "HarmonicValue",
    "InertiaTensor",
    "MassProperties",
    "MaxMinMean",
    "ComplexMagnitudeMethod",
    "MultipleFourierSeriesInterpolator",
    "Named2DLocation",
    "PIDControlUpdateMethod",
    "Quaternion",
    "RealMatrix",
    "RealVector",
    "ResultOptionsFor3DVector",
    "RotationAxis",
    "RoundedOrder",
    "SinCurve",
    "SquareMatrix",
    "StressPoint",
    "TransformMatrix3D",
    "TranslationRotation",
    "Vector2DListAccessor",
    "Vector6D",
)
