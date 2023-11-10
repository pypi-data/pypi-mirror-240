import pathlib
from typing import Iterable, Union, Optional, List


def get_or_create(directory: pathlib.Path):
    if not directory.exists():
        directory.touch()


def get_path_or_none(
    str_path: Optional[Union[str, Iterable[str]]]
) -> Optional[Union[pathlib.Path, List[pathlib.Path]]]:
    if str_path is None:
        return None
    if isinstance(str_path, str):
        return pathlib.Path(str_path)
    return [pathlib.Path(path) for path in str_path]
