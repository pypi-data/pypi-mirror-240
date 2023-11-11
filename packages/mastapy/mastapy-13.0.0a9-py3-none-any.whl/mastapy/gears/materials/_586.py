"""BevelGearMaterialDatabase"""
from __future__ import annotations

from typing import TypeVar

from mastapy.gears.materials import _593
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "BevelGearMaterialDatabase"
)


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMaterialDatabase",)


Self = TypeVar("Self", bound="BevelGearMaterialDatabase")


class BevelGearMaterialDatabase(_593.GearMaterialDatabase["_585.BevelGearMaterial"]):
    """BevelGearMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMaterialDatabase")

    class _Cast_BevelGearMaterialDatabase:
        """Special nested class for casting BevelGearMaterialDatabase to subclasses."""

        def __init__(
            self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase",
            parent: "BevelGearMaterialDatabase",
        ):
            self._parent = parent

        @property
        def gear_material_database(
            self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase",
        ):
            return self._parent._cast(_593.GearMaterialDatabase)

        @property
        def named_database(
            self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase",
        ):
            from mastapy.utility.databases import _1825

            return self._parent._cast(_1825.NamedDatabase)

        @property
        def sql_database(
            self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.SQLDatabase)

        @property
        def database(self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase"):
            pass

            from mastapy.utility.databases import _1821

            return self._parent._cast(_1821.Database)

        @property
        def bevel_gear_material_database(
            self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase",
        ) -> "BevelGearMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearMaterialDatabase._Cast_BevelGearMaterialDatabase":
        return self._Cast_BevelGearMaterialDatabase(self)
