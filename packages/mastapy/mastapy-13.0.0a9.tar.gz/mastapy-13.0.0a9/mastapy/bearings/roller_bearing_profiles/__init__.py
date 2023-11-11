"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1924 import ProfileDataToUse
    from ._1925 import ProfileSet
    from ._1926 import ProfileToFit
    from ._1927 import RollerBearingConicalProfile
    from ._1928 import RollerBearingCrownedProfile
    from ._1929 import RollerBearingDinLundbergProfile
    from ._1930 import RollerBearingFlatProfile
    from ._1931 import RollerBearingJohnsGoharProfile
    from ._1932 import RollerBearingLundbergProfile
    from ._1933 import RollerBearingProfile
    from ._1934 import RollerBearingUserSpecifiedProfile
    from ._1935 import RollerRaceProfilePoint
    from ._1936 import UserSpecifiedProfilePoint
    from ._1937 import UserSpecifiedRollerRaceProfilePoint
else:
    import_structure = {
        "_1924": ["ProfileDataToUse"],
        "_1925": ["ProfileSet"],
        "_1926": ["ProfileToFit"],
        "_1927": ["RollerBearingConicalProfile"],
        "_1928": ["RollerBearingCrownedProfile"],
        "_1929": ["RollerBearingDinLundbergProfile"],
        "_1930": ["RollerBearingFlatProfile"],
        "_1931": ["RollerBearingJohnsGoharProfile"],
        "_1932": ["RollerBearingLundbergProfile"],
        "_1933": ["RollerBearingProfile"],
        "_1934": ["RollerBearingUserSpecifiedProfile"],
        "_1935": ["RollerRaceProfilePoint"],
        "_1936": ["UserSpecifiedProfilePoint"],
        "_1937": ["UserSpecifiedRollerRaceProfilePoint"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ProfileDataToUse",
    "ProfileSet",
    "ProfileToFit",
    "RollerBearingConicalProfile",
    "RollerBearingCrownedProfile",
    "RollerBearingDinLundbergProfile",
    "RollerBearingFlatProfile",
    "RollerBearingJohnsGoharProfile",
    "RollerBearingLundbergProfile",
    "RollerBearingProfile",
    "RollerBearingUserSpecifiedProfile",
    "RollerRaceProfilePoint",
    "UserSpecifiedProfilePoint",
    "UserSpecifiedRollerRaceProfilePoint",
)
