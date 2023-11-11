"""AbstractShaftOrHousingSystemDeflection"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2712
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AbstractShaftOrHousingSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2433
    from mastapy.system_model.analyses_and_results.power_flows import _4030


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingSystemDeflection",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingSystemDeflection")


class AbstractShaftOrHousingSystemDeflection(_2712.ComponentSystemDeflection):
    """AbstractShaftOrHousingSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingSystemDeflection"
    )

    class _Cast_AbstractShaftOrHousingSystemDeflection:
        """Special nested class for casting AbstractShaftOrHousingSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
            parent: "AbstractShaftOrHousingSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ):
            return self._parent._cast(_2712.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def abstract_shaft_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2684,
            )

            return self._parent._cast(_2684.AbstractShaftSystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.CycloidalDiscSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.FEPartSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2801,
            )

            return self._parent._cast(_2801.ShaftSystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
        ) -> "AbstractShaftOrHousingSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mass_including_connected_components(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassIncludingConnectedComponents

        if temp is None:
            return 0.0

        return temp

    @property
    def polar_inertia_including_connected_components(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PolarInertiaIncludingConnectedComponents

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2433.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4030.AbstractShaftOrHousingPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AbstractShaftOrHousingPowerFlow

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
    ) -> "AbstractShaftOrHousingSystemDeflection._Cast_AbstractShaftOrHousingSystemDeflection":
        return self._Cast_AbstractShaftOrHousingSystemDeflection(self)
