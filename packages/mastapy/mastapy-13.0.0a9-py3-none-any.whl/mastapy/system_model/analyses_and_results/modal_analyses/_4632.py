"""GearModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4654
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "GearModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.system_model.analyses_and_results.system_deflections import _2758


__docformat__ = "restructuredtext en"
__all__ = ("GearModalAnalysis",)


Self = TypeVar("Self", bound="GearModalAnalysis")


class GearModalAnalysis(_4654.MountableComponentModalAnalysis):
    """GearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearModalAnalysis")

    class _Cast_GearModalAnalysis:
        """Special nested class for casting GearModalAnalysis to subclasses."""

        def __init__(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
            parent: "GearModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            return self._parent._cast(_4654.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(self: "GearModalAnalysis._Cast_GearModalAnalysis"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.ComponentModalAnalysis)

        @property
        def part_modal_analysis(self: "GearModalAnalysis._Cast_GearModalAnalysis"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(self: "GearModalAnalysis._Cast_GearModalAnalysis"):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.PartAnalysisCase)

        @property
        def part_analysis(self: "GearModalAnalysis._Cast_GearModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2654

            return self._parent._cast(_2654.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(self: "GearModalAnalysis._Cast_GearModalAnalysis"):
            from mastapy.system_model.analyses_and_results import _2648

            return self._parent._cast(_2648.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573

            return self._parent._cast(_4573.AGMAGleasonConicalGearModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582

            return self._parent._cast(_4582.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4583

            return self._parent._cast(_4583.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4585

            return self._parent._cast(_4585.BevelGearModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(_4598.ConceptGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.ConicalGearModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(_4617.CylindricalGearModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(_4619.CylindricalPlanetGearModalAnalysis)

        @property
        def face_gear_modal_analysis(self: "GearModalAnalysis._Cast_GearModalAnalysis"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.FaceGearModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.HypoidGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640

            return self._parent._cast(
                _4640.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(
                _4643.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(
                _4646.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4680

            return self._parent._cast(_4680.SpiralBevelGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4691

            return self._parent._cast(_4691.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.StraightBevelSunGearModalAnalysis)

        @property
        def worm_gear_modal_analysis(self: "GearModalAnalysis._Cast_GearModalAnalysis"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.WormGearModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4710

            return self._parent._cast(_4710.ZerolBevelGearModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "GearModalAnalysis._Cast_GearModalAnalysis",
        ) -> "GearModalAnalysis":
            return self._parent

        def __getattr__(self: "GearModalAnalysis._Cast_GearModalAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2527.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2758.GearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearModalAnalysis._Cast_GearModalAnalysis":
        return self._Cast_GearModalAnalysis(self)
