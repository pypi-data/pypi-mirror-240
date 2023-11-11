"""AbstractAssemblyCompoundDynamicAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6483
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "AbstractAssemblyCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6273


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundDynamicAnalysis")


class AbstractAssemblyCompoundDynamicAnalysis(_6483.PartCompoundDynamicAnalysis):
    """AbstractAssemblyCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundDynamicAnalysis"
    )

    class _Cast_AbstractAssemblyCompoundDynamicAnalysis:
        """Special nested class for casting AbstractAssemblyCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
            parent: "AbstractAssemblyCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def part_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            return self._parent._cast(_6483.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7539

            return self._parent._cast(_7539.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6410,
            )

            return self._parent._cast(
                _6410.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6411,
            )

            return self._parent._cast(_6411.AssemblyCompoundDynamicAnalysis)

        @property
        def belt_drive_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6414,
            )

            return self._parent._cast(_6414.BeltDriveCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6417,
            )

            return self._parent._cast(
                _6417.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6422,
            )

            return self._parent._cast(_6422.BevelGearSetCompoundDynamicAnalysis)

        @property
        def bolted_joint_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6424,
            )

            return self._parent._cast(_6424.BoltedJointCompoundDynamicAnalysis)

        @property
        def clutch_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6425,
            )

            return self._parent._cast(_6425.ClutchCompoundDynamicAnalysis)

        @property
        def concept_coupling_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6430,
            )

            return self._parent._cast(_6430.ConceptCouplingCompoundDynamicAnalysis)

        @property
        def concept_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6435,
            )

            return self._parent._cast(_6435.ConceptGearSetCompoundDynamicAnalysis)

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6438,
            )

            return self._parent._cast(_6438.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def coupling_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6441,
            )

            return self._parent._cast(_6441.CouplingCompoundDynamicAnalysis)

        @property
        def cvt_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6445,
            )

            return self._parent._cast(_6445.CVTCompoundDynamicAnalysis)

        @property
        def cycloidal_assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6447,
            )

            return self._parent._cast(_6447.CycloidalAssemblyCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6453,
            )

            return self._parent._cast(_6453.CylindricalGearSetCompoundDynamicAnalysis)

        @property
        def face_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.FaceGearSetCompoundDynamicAnalysis)

        @property
        def flexible_pin_assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6461,
            )

            return self._parent._cast(_6461.FlexiblePinAssemblyCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.GearSetCompoundDynamicAnalysis)

        @property
        def hypoid_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.HypoidGearSetCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(
                _6472.KlingelnbergCycloPalloidConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6475,
            )

            return self._parent._cast(
                _6475.KlingelnbergCycloPalloidHypoidGearSetCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(
                _6478.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6484,
            )

            return self._parent._cast(
                _6484.PartToPartShearCouplingCompoundDynamicAnalysis
            )

        @property
        def planetary_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(_6488.PlanetaryGearSetCompoundDynamicAnalysis)

        @property
        def rolling_ring_assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6495,
            )

            return self._parent._cast(_6495.RollingRingAssemblyCompoundDynamicAnalysis)

        @property
        def root_assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6498,
            )

            return self._parent._cast(_6498.RootAssemblyCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6502,
            )

            return self._parent._cast(_6502.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6505,
            )

            return self._parent._cast(_6505.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def spring_damper_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6506,
            )

            return self._parent._cast(_6506.SpringDamperCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6511,
            )

            return self._parent._cast(
                _6511.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6514,
            )

            return self._parent._cast(_6514.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def synchroniser_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(_6517.SynchroniserCompoundDynamicAnalysis)

        @property
        def torque_converter_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(_6521.TorqueConverterCompoundDynamicAnalysis)

        @property
        def worm_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6529,
            )

            return self._parent._cast(_6529.WormGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6532,
            )

            return self._parent._cast(_6532.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
        ) -> "AbstractAssemblyCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6273.AbstractAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractAssemblyDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6273.AbstractAssemblyDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AbstractAssemblyDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyCompoundDynamicAnalysis._Cast_AbstractAssemblyCompoundDynamicAnalysis":
        return self._Cast_AbstractAssemblyCompoundDynamicAnalysis(self)
