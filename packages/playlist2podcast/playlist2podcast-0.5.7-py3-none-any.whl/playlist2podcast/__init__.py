"""Package 'playlist2podcast' level definitions."""
from typing_extensions import Final

CODE_VERSION_MAJOR: Final[int] = 0  # Current major version of this code
CODE_VERSION_MINOR: Final[int] = 5  # Current minor version of this code
CODE_VERSION_PATCH: Final[int] = 7  # Current patch version of this code

__version__: Final[
    str
] = f"{CODE_VERSION_MAJOR}.{CODE_VERSION_MINOR}.{CODE_VERSION_PATCH}"
__package_name__: Final[str] = "playlist2podcast"
__display_name__: Final[str] = "Playlist2Podcast"
