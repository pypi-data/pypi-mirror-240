"""AGMAGleasonConicalGearSetSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2722
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AGMAGleasonConicalGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2511
    from mastapy.system_model.analyses_and_results.power_flows import _4035


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetSystemDeflection")


class AGMAGleasonConicalGearSetSystemDeflection(_2722.ConicalGearSetSystemDeflection):
    """AGMAGleasonConicalGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearSetSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearSetSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
            parent: "AGMAGleasonConicalGearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            return self._parent._cast(_2722.ConicalGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2682,
            )

            return self._parent._cast(_2682.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2699,
            )

            return self._parent._cast(_2699.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2704,
            )

            return self._parent._cast(_2704.BevelGearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2761,
            )

            return self._parent._cast(_2761.HypoidGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.SpiralBevelGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.StraightBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.ZerolBevelGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
        ) -> "AGMAGleasonConicalGearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2511.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4035.AGMAGleasonConicalGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetSystemDeflection._Cast_AGMAGleasonConicalGearSetSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearSetSystemDeflection(self)
