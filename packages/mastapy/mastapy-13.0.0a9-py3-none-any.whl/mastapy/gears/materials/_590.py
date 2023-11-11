"""CylindricalGearMaterialDatabase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.materials import _268
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "CylindricalGearMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.gears.materials import _589


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMaterialDatabase",)


Self = TypeVar("Self", bound="CylindricalGearMaterialDatabase")
T = TypeVar("T", bound="_589.CylindricalGearMaterial")


class CylindricalGearMaterialDatabase(_268.MaterialDatabase[T]):
    """CylindricalGearMaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _CYLINDRICAL_GEAR_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearMaterialDatabase")

    class _Cast_CylindricalGearMaterialDatabase:
        """Special nested class for casting CylindricalGearMaterialDatabase to subclasses."""

        def __init__(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
            parent: "CylindricalGearMaterialDatabase",
        ):
            self._parent = parent

        @property
        def material_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ):
            return self._parent._cast(_268.MaterialDatabase)

        @property
        def named_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ):
            from mastapy.utility.databases import _1825

            return self._parent._cast(_1825.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1828

            return self._parent._cast(_1828.SQLDatabase)

        @property
        def database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ):
            pass

            from mastapy.utility.databases import _1821

            return self._parent._cast(_1821.Database)

        @property
        def cylindrical_gear_agma_material_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ):
            from mastapy.gears.materials import _587

            return self._parent._cast(_587.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ):
            from mastapy.gears.materials import _588

            return self._parent._cast(_588.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ):
            from mastapy.gears.materials import _591

            return self._parent._cast(_591.CylindricalGearPlasticMaterialDatabase)

        @property
        def cylindrical_gear_material_database(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
        ) -> "CylindricalGearMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMaterialDatabase._Cast_CylindricalGearMaterialDatabase":
        return self._Cast_CylindricalGearMaterialDatabase(self)
