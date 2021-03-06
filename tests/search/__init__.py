from pathlib import Path, PurePath
from typing import Union


def get_test_resource(*nodes: Union[PurePath, str]) -> Path:
    """Gets a path of a test resource file under resources/."""
    return Path(Path(__file__).parent.parent, "resources", *nodes)
