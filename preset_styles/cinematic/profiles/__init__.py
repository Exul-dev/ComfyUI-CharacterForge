"""
CharacterForge Cinematic Profiles
=================================

Profili condivisi usati dai preset cinematografici.

Questi file NON contengono registi.
Contengono soltanto librerie riutilizzabili.
"""

from .skin import SKIN_PROFILES
from .lighting import LIGHTING_PROFILES
from .lenses import LENS_PROFILES
from .film_stock import FILM_STOCKS
from .grain import GRAIN_PROFILES
from .color import COLOR_PROFILES
from .atmosphere import ATMOSPHERE_PROFILES
from .camera import CAMERA_PROFILES

__all__ = [
    "SKIN_PROFILES",
    "LIGHTING_PROFILES",
    "LENS_PROFILES",
    "FILM_STOCKS",
    "GRAIN_PROFILES",
    "COLOR_PROFILES",
    "ATMOSPHERE_PROFILES",
    "CAMERA_PROFILES",
]