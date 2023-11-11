"""BevelGearSetAdvancedSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7275
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "BevelGearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearSetAdvancedSystemDeflection")


class BevelGearSetAdvancedSystemDeflection(
    _7275.AGMAGleasonConicalGearSetAdvancedSystemDeflection
):
    """BevelGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetAdvancedSystemDeflection")

    class _Cast_BevelGearSetAdvancedSystemDeflection:
        """Special nested class for casting BevelGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
            parent: "BevelGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            return self._parent._cast(
                _7275.AGMAGleasonConicalGearSetAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(_7303.ConicalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7370,
            )

            return self._parent._cast(_7370.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7266,
            )

            return self._parent._cast(_7266.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(_7351.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7282,
            )

            return self._parent._cast(
                _7282.BevelDifferentialGearSetAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(_7373.SpiralBevelGearSetAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(
                _7379.StraightBevelDiffGearSetAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7382,
            )

            return self._parent._cast(
                _7382.StraightBevelGearSetAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7401,
            )

            return self._parent._cast(_7401.ZerolBevelGearSetAdvancedSystemDeflection)

        @property
        def bevel_gear_set_advanced_system_deflection(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
        ) -> "BevelGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelGearSetAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2517.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetAdvancedSystemDeflection._Cast_BevelGearSetAdvancedSystemDeflection":
        return self._Cast_BevelGearSetAdvancedSystemDeflection(self)
