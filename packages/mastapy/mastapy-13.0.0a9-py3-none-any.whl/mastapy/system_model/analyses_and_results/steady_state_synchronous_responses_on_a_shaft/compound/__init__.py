"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._3372 import AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3373 import AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3374 import (
        AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3375 import (
        AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3376 import (
        AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3377 import (
        AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3378 import (
        AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3379 import AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3380 import BearingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3381 import BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3382 import BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3383 import (
        BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3384 import (
        BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3385 import (
        BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3386 import (
        BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3387 import (
        BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3388 import BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3389 import BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3390 import BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3391 import BoltCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3392 import BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3393 import ClutchCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3394 import ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3395 import ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3396 import CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3397 import ComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3398 import ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3399 import (
        ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3400 import ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3401 import ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3402 import ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3403 import ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3404 import ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3405 import ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3406 import ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3407 import ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3408 import ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3409 import CouplingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3410 import CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3411 import CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3412 import CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3413 import CVTCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3414 import CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3415 import CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3416 import (
        CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3417 import CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3418 import (
        CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3419 import CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3420 import CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3421 import CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3422 import (
        CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3423 import DatumCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3424 import ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3425 import FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3426 import FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3427 import FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3428 import FEPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3429 import FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3430 import GearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3431 import GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3432 import GearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3433 import GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3434 import HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3435 import HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3436 import HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3437 import (
        InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3438 import (
        KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3439 import (
        KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3440 import (
        KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3441 import (
        KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3442 import (
        KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3443 import (
        KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3444 import (
        KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3445 import (
        KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3446 import (
        KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3447 import MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3448 import (
        MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3449 import MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3450 import OilSealCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3451 import PartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3452 import (
        PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3453 import (
        PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3454 import (
        PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3455 import PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3456 import PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3457 import PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3458 import PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3459 import PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3460 import PulleyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3461 import RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3462 import (
        RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3463 import RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3464 import RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3465 import (
        RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3466 import RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3467 import ShaftCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3468 import ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3469 import (
        ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3470 import SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3471 import SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3472 import SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3473 import SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3474 import SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3475 import (
        SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3476 import SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3477 import (
        StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3478 import (
        StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3479 import (
        StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3480 import StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3481 import (
        StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3482 import (
        StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3483 import (
        StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3484 import (
        StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3485 import SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3486 import SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3487 import SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3488 import SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3489 import TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3490 import (
        TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3491 import TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3492 import (
        TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft,
    )
    from ._3493 import UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3494 import VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3495 import WormGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3496 import WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3497 import WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3498 import ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3499 import ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
    from ._3500 import ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
else:
    import_structure = {
        "_3372": ["AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3373": ["AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3374": [
            "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3375": [
            "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3376": [
            "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3377": [
            "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3378": [
            "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3379": ["AssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3380": ["BearingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3381": ["BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3382": ["BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3383": [
            "BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3384": [
            "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3385": [
            "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3386": [
            "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3387": [
            "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3388": ["BevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3389": ["BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3390": ["BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3391": ["BoltCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3392": ["BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3393": ["ClutchCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3394": ["ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3395": ["ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3396": ["CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3397": ["ComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3398": ["ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3399": [
            "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3400": ["ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3401": ["ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3402": ["ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3403": ["ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3404": ["ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3405": ["ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3406": ["ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3407": ["ConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3408": ["ConnectorCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3409": ["CouplingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3410": ["CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3411": ["CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3412": ["CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3413": ["CVTCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3414": ["CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3415": ["CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3416": [
            "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3417": ["CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3418": [
            "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3419": ["CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3420": ["CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3421": ["CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3422": [
            "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3423": ["DatumCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3424": ["ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3425": ["FaceGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3426": ["FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3427": ["FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3428": ["FEPartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3429": ["FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3430": ["GearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3431": ["GearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3432": ["GearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3433": ["GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3434": ["HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3435": ["HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3436": ["HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3437": [
            "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3438": [
            "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3439": [
            "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3440": [
            "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3441": [
            "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3442": [
            "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3443": [
            "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3444": [
            "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3445": [
            "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3446": [
            "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3447": ["MassDiscCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3448": ["MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3449": ["MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3450": ["OilSealCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3451": ["PartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3452": [
            "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3453": [
            "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3454": [
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3455": ["PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3456": ["PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3457": ["PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3458": ["PointLoadCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3459": ["PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3460": ["PulleyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3461": ["RingPinsCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3462": [
            "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3463": ["RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3464": ["RollingRingCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3465": [
            "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3466": ["RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3467": ["ShaftCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3468": ["ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3469": [
            "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3470": ["SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3471": ["SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3472": ["SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3473": ["SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3474": ["SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3475": [
            "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3476": ["SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3477": [
            "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3478": [
            "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3479": [
            "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3480": ["StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3481": [
            "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3482": ["StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3483": [
            "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3484": ["StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3485": ["SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3486": ["SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3487": ["SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3488": ["SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3489": ["TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3490": [
            "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3491": ["TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3492": [
            "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft"
        ],
        "_3493": ["UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3494": ["VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3495": ["WormGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3496": ["WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3497": ["WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3498": ["ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3499": ["ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"],
        "_3500": ["ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft",
    "AbstractShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "AssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "BearingCompoundSteadyStateSynchronousResponseOnAShaft",
    "BeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "BoltCompoundSteadyStateSynchronousResponseOnAShaft",
    "BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "CoaxialConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTBeltConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTCompoundSteadyStateSynchronousResponseOnAShaft",
    "CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscCentralBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft",
    "CycloidalDiscPlanetaryBearingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "DatumCompoundSteadyStateSynchronousResponseOnAShaft",
    "ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "FEPartCompoundSteadyStateSynchronousResponseOnAShaft",
    "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "GearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "MassDiscCompoundSteadyStateSynchronousResponseOnAShaft",
    "MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "OilSealCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetaryConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft",
    "PointLoadCompoundSteadyStateSynchronousResponseOnAShaft",
    "PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft",
    "PulleyCompoundSteadyStateSynchronousResponseOnAShaft",
    "RingPinsCompoundSteadyStateSynchronousResponseOnAShaft",
    "RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingCompoundSteadyStateSynchronousResponseOnAShaft",
    "RollingRingConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "ShaftToMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft",
    "SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterConnectionCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft",
    "TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft",
    "UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft",
    "VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    "ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)
