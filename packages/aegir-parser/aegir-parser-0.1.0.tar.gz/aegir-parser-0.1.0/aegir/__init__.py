import logging
from collections import namedtuple

from .format_error import FormatError
from aegir.aegir import Aegir

__version__ = "0.1.0"

logging.getLogger(__name__).addHandler(logging.NullHandler())
VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel serial")
version_info = VersionInfo(major=0, minor=1, micro=0, releaselevel="alpha", serial=0)

__all__ = ("Aegir", "FormatError")
