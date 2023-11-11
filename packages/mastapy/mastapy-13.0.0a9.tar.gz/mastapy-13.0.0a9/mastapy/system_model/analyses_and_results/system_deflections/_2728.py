"""CouplingSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2803
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CouplingSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2580
    from mastapy.system_model.analyses_and_results.power_flows import _4068


__docformat__ = "restructuredtext en"
__all__ = ("CouplingSystemDeflection",)


Self = TypeVar("Self", bound="CouplingSystemDeflection")


class CouplingSystemDeflection(_2803.SpecialisedAssemblySystemDeflection):
    """CouplingSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COUPLING_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingSystemDeflection")

    class _Cast_CouplingSystemDeflection:
        """Special nested class for casting CouplingSystemDeflection to subclasses."""

        def __init__(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
            parent: "CouplingSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            return self._parent._cast(_2803.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2682,
            )

            return self._parent._cast(_2682.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def clutch_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.ClutchSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2716,
            )

            return self._parent._cast(_2716.ConceptCouplingSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2785,
            )

            return self._parent._cast(_2785.PartToPartShearCouplingSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(_2809.SpringDamperSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2827,
            )

            return self._parent._cast(_2827.TorqueConverterSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection",
        ) -> "CouplingSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CouplingSystemDeflection._Cast_CouplingSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2580.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4068.CouplingPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CouplingPowerFlow

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
    ) -> "CouplingSystemDeflection._Cast_CouplingSystemDeflection":
        return self._Cast_CouplingSystemDeflection(self)
