"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1739 import AdHocCustomTable
    from ._1740 import AxisSettings
    from ._1741 import BlankRow
    from ._1742 import CadPageOrientation
    from ._1743 import CadPageSize
    from ._1744 import CadTableBorderType
    from ._1745 import ChartDefinition
    from ._1746 import SMTChartPointShape
    from ._1747 import CustomChart
    from ._1748 import CustomDrawing
    from ._1749 import CustomGraphic
    from ._1750 import CustomImage
    from ._1751 import CustomReport
    from ._1752 import CustomReportCadDrawing
    from ._1753 import CustomReportChart
    from ._1754 import CustomReportChartItem
    from ._1755 import CustomReportColumn
    from ._1756 import CustomReportColumns
    from ._1757 import CustomReportDefinitionItem
    from ._1758 import CustomReportHorizontalLine
    from ._1759 import CustomReportHtmlItem
    from ._1760 import CustomReportItem
    from ._1761 import CustomReportItemContainer
    from ._1762 import CustomReportItemContainerCollection
    from ._1763 import CustomReportItemContainerCollectionBase
    from ._1764 import CustomReportItemContainerCollectionItem
    from ._1765 import CustomReportKey
    from ._1766 import CustomReportMultiPropertyItem
    from ._1767 import CustomReportMultiPropertyItemBase
    from ._1768 import CustomReportNameableItem
    from ._1769 import CustomReportNamedItem
    from ._1770 import CustomReportPropertyItem
    from ._1771 import CustomReportStatusItem
    from ._1772 import CustomReportTab
    from ._1773 import CustomReportTabs
    from ._1774 import CustomReportText
    from ._1775 import CustomRow
    from ._1776 import CustomSubReport
    from ._1777 import CustomTable
    from ._1778 import DefinitionBooleanCheckOptions
    from ._1779 import DynamicCustomReportItem
    from ._1780 import FontStyle
    from ._1781 import FontWeight
    from ._1782 import HeadingSize
    from ._1783 import SimpleChartDefinition
    from ._1784 import UserTextRow
else:
    import_structure = {
        "_1739": ["AdHocCustomTable"],
        "_1740": ["AxisSettings"],
        "_1741": ["BlankRow"],
        "_1742": ["CadPageOrientation"],
        "_1743": ["CadPageSize"],
        "_1744": ["CadTableBorderType"],
        "_1745": ["ChartDefinition"],
        "_1746": ["SMTChartPointShape"],
        "_1747": ["CustomChart"],
        "_1748": ["CustomDrawing"],
        "_1749": ["CustomGraphic"],
        "_1750": ["CustomImage"],
        "_1751": ["CustomReport"],
        "_1752": ["CustomReportCadDrawing"],
        "_1753": ["CustomReportChart"],
        "_1754": ["CustomReportChartItem"],
        "_1755": ["CustomReportColumn"],
        "_1756": ["CustomReportColumns"],
        "_1757": ["CustomReportDefinitionItem"],
        "_1758": ["CustomReportHorizontalLine"],
        "_1759": ["CustomReportHtmlItem"],
        "_1760": ["CustomReportItem"],
        "_1761": ["CustomReportItemContainer"],
        "_1762": ["CustomReportItemContainerCollection"],
        "_1763": ["CustomReportItemContainerCollectionBase"],
        "_1764": ["CustomReportItemContainerCollectionItem"],
        "_1765": ["CustomReportKey"],
        "_1766": ["CustomReportMultiPropertyItem"],
        "_1767": ["CustomReportMultiPropertyItemBase"],
        "_1768": ["CustomReportNameableItem"],
        "_1769": ["CustomReportNamedItem"],
        "_1770": ["CustomReportPropertyItem"],
        "_1771": ["CustomReportStatusItem"],
        "_1772": ["CustomReportTab"],
        "_1773": ["CustomReportTabs"],
        "_1774": ["CustomReportText"],
        "_1775": ["CustomRow"],
        "_1776": ["CustomSubReport"],
        "_1777": ["CustomTable"],
        "_1778": ["DefinitionBooleanCheckOptions"],
        "_1779": ["DynamicCustomReportItem"],
        "_1780": ["FontStyle"],
        "_1781": ["FontWeight"],
        "_1782": ["HeadingSize"],
        "_1783": ["SimpleChartDefinition"],
        "_1784": ["UserTextRow"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AdHocCustomTable",
    "AxisSettings",
    "BlankRow",
    "CadPageOrientation",
    "CadPageSize",
    "CadTableBorderType",
    "ChartDefinition",
    "SMTChartPointShape",
    "CustomChart",
    "CustomDrawing",
    "CustomGraphic",
    "CustomImage",
    "CustomReport",
    "CustomReportCadDrawing",
    "CustomReportChart",
    "CustomReportChartItem",
    "CustomReportColumn",
    "CustomReportColumns",
    "CustomReportDefinitionItem",
    "CustomReportHorizontalLine",
    "CustomReportHtmlItem",
    "CustomReportItem",
    "CustomReportItemContainer",
    "CustomReportItemContainerCollection",
    "CustomReportItemContainerCollectionBase",
    "CustomReportItemContainerCollectionItem",
    "CustomReportKey",
    "CustomReportMultiPropertyItem",
    "CustomReportMultiPropertyItemBase",
    "CustomReportNameableItem",
    "CustomReportNamedItem",
    "CustomReportPropertyItem",
    "CustomReportStatusItem",
    "CustomReportTab",
    "CustomReportTabs",
    "CustomReportText",
    "CustomRow",
    "CustomSubReport",
    "CustomTable",
    "DefinitionBooleanCheckOptions",
    "DynamicCustomReportItem",
    "FontStyle",
    "FontWeight",
    "HeadingSize",
    "SimpleChartDefinition",
    "UserTextRow",
)
