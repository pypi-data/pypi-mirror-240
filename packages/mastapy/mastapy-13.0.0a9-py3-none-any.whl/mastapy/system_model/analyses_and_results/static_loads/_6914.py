"""KlingelnbergCycloPalloidHypoidGearSetLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2536
    from mastapy.system_model.analyses_and_results.static_loads import _6912, _6913


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetLoadCase",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearSetLoadCase")


class KlingelnbergCycloPalloidHypoidGearSetLoadCase(
    _6911.KlingelnbergCycloPalloidConicalGearSetLoadCase
):
    """KlingelnbergCycloPalloidHypoidGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetLoadCase to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
            parent: "KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ):
            return self._parent._cast(
                _6911.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def conical_gear_set_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6892

            return self._parent._cast(_6892.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6803

            return self._parent._cast(_6803.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.PartLoadCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetLoadCase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2536.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_6912.KlingelnbergCycloPalloidHypoidGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_load_case(
        self: Self,
    ) -> "List[_6912.KlingelnbergCycloPalloidHypoidGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_load_case(
        self: Self,
    ) -> "List[_6913.KlingelnbergCycloPalloidHypoidGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetLoadCase._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetLoadCase(self)
