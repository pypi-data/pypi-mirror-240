from __future__ import annotations
import dataclasses
import pathlib
import typing
from pathlib import Path
from typing import Optional, List, Any

from utfuzz.file_manager.file_finder import get_py_files


@dataclasses.dataclass
class Config(object):
    project_dir: Optional[Path]
    output_dir: Optional[Path]
    requirements_file: Optional[Path]
    sys_paths: Optional[List[Path]]
    analyze_targets: Optional[List[Path]]
    java: Optional[str]
    timeout: Optional[int]
    generate_only_error_suite: Optional[bool]
    debug_mode: Optional[bool]

    @staticmethod
    def make_empty_config() -> Config:
        return Config(
            project_dir=None,
            output_dir=None,
            requirements_file=None,
            sys_paths=None,
            analyze_targets=None,
            java=None,
            timeout=None,
            generate_only_error_suite=None,
            debug_mode=None,
        )

    def get_or_default(self, field: str) -> Any:
        if field == "project_dir":
            return self.my_getattr(field, pathlib.Path(".").resolve().absolute())
        elif field == "output_dir":
            return self.my_getattr(
                field, self.get_or_default("project_dir") / "utfuzz_tests"
            )
        elif field == "sys_paths":
            return self.my_getattr(field, [self.get_or_default("project_dir")])
        elif field == "analyze_targets":
            return self.my_getattr(
                field, []  # get_py_files(self.get_or_default("project_dir"))
            )
        elif field == "java":
            return self.my_getattr(field, "java")
        elif field == "timeout":
            return self.my_getattr(field, 60)
        elif field == "generate_only_error_suite":
            return self.my_getattr(field, False)
        elif field == "debug_mode":
            return self.my_getattr(field, False)
        elif field == "requirements_file":
            return self.my_getattr(field, None)

    def fill_default(self):
        if self.project_dir is None:
            self.project_dir = self.get_or_default("project_dir")
        if self.output_dir is None:
            self.output_dir = self.get_or_default("output_dir")
        if self.sys_paths is None:
            self.sys_paths = self.get_or_default("sys_paths")
        if self.analyze_targets is None:
            self.analyze_targets = self.get_or_default("analyze_targets")
        if self.java is None:
            self.java = self.get_or_default("java")
        if self.timeout is None:
            self.timeout = self.get_or_default("timeout")
        if self.generate_only_error_suite is None:
            self.generate_only_error_suite = self.get_or_default(
                "generate_only_error_suite"
            )
        if self.debug_mode is None:
            self.debug_mode = self.get_or_default("debug_mode")

        if self.project_dir not in self.sys_paths:
            self.sys_paths.append(self.project_dir)

    def resolve_paths(self):
        self.project_dir = self.project_dir.resolve().absolute()
        self.output_dir = self.output_dir.resolve().absolute()
        self.sys_paths = list(
            dict.fromkeys([p.resolve().absolute() for p in self.sys_paths])
        )
        self.analyze_targets = list(
            dict.fromkeys([p.resolve().absolute() for p in self.analyze_targets])
        )
        if self.requirements_file is not None:
            self.requirements_file.resolve().absolute()

    def my_getattr(self, field: str, default: typing.Any):
        field_value = getattr(self, field, default)
        if field_value is None:
            return default
        return field_value
