"""BevelDifferentialGearSetSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2704
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BevelDifferentialGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2513
    from mastapy.system_model.analyses_and_results.static_loads import _6821
    from mastapy.gears.rating.bevel import _554
    from mastapy.system_model.analyses_and_results.power_flows import _4042
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2700,
        _2698,
    )


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetSystemDeflection")


class BevelDifferentialGearSetSystemDeflection(_2704.BevelGearSetSystemDeflection):
    """BevelDifferentialGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetSystemDeflection"
    )

    class _Cast_BevelDifferentialGearSetSystemDeflection:
        """Special nested class for casting BevelDifferentialGearSetSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
            parent: "BevelDifferentialGearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ):
            return self._parent._cast(_2704.BevelGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.ConicalGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2682,
            )

            return self._parent._cast(_2682.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "BevelDifferentialGearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearSetSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2513.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6821.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_554.BevelGearSetRating":
        """mastapy.gears.rating.bevel.BevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_554.BevelGearSetRating":
        """mastapy.gears.rating.bevel.BevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4042.BevelDifferentialGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_differential_gears_system_deflection(
        self: Self,
    ) -> "List[_2700.BevelDifferentialGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_system_deflection(
        self: Self,
    ) -> "List[_2698.BevelDifferentialGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection":
        return self._Cast_BevelDifferentialGearSetSystemDeflection(self)
