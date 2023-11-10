import json
import pathlib

from utfuzz import my_print
from utfuzz.config.config import Config


def save_config(config: Config):
    with open(str(config.project_dir / "utfuzz_config.json"), "w") as conf:
        print(
            json.dumps(
                {
                    "java": config.java,
                    "sys_paths": [str(p) for p in config.sys_paths],
                    "analyze_targets": [str(t) for t in config.analyze_targets],
                    "generate_only_error_suite": config.generate_only_error_suite,
                    "timeout": config.timeout,
                    "output": str(config.output_dir),
                    "project": str(config.project_dir),
                    "requirements": None
                    if config.requirements_file is None
                    else str(config.requirements_file),
                },
                indent=2,
            ),
            file=conf,
        )


def load_config(path: pathlib.Path):
    try:
        with open(str(path), "r") as conf:
            data = "\n".join(conf.readlines())
            return json.loads(data)
    except OSError:
        my_print(f"Cannot read config file {path}")
        return {}
