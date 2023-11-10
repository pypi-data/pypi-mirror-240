from .psense_aws_itfc import PSenseAWSInterface
from .psense_parser import PSenseParser

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

try:
    # This will read version from pyproject.toml
    __version__ = importlib_metadata.version(__name__)
except Exception:
    __version__ = "unknown"
