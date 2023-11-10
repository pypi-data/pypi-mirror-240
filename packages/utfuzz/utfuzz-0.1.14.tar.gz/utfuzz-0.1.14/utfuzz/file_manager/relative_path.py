import pathlib
import typing


def make_relative(
    path: typing.Union[pathlib.Path, str], project_dir: pathlib.Path
) -> pathlib.Path:
    if isinstance(path, str):
        path = pathlib.Path(path)
    if path.is_absolute():
        return path.resolve().absolute()
    return (project_dir / path).resolve().absolute()
