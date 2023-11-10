"""UnitTestBot for Python"""
import pathlib
import sys

import tqdm as tqdm

from utfuzz.config.config import Config
from utfuzz.file_manager.directory_manager import get_path_or_none
from utfuzz.file_manager.relative_path import make_relative
from utfuzz.user_interface.printer import my_print

from utfuzz.config.config_manager import save_config, load_config
from utfuzz.exceptions.exceptions import (
    EnvironmentException,
    NotFoundRequirementsTxt,
    MultipleRequirementsTxt,
)
from utfuzz.file_manager.file_finder import find_config, get_py_files
from utfuzz.parser import parse
from utfuzz.requirements_managers.java_requirements_manager import (
    JavaRequirementsManager,
    JavaResult,
)
from utfuzz.requirements_managers.python_requirements_manger import (
    PythonRequirementsManager,
)
from utfuzz.user_interface.reader import (
    my_read,
    read_with_action,
    check_int_with_default,
    check_exists_path_with_default,
    check_valid_path_with_default,
    check_yes_no_with_default,
)
from utfuzz.utbot_manager.utbot_manager import generate_tests


def main():
    args = parse()
    config = Config.make_empty_config()
    config.project_dir = pathlib.Path(args.project_dir).resolve().absolute()

    # Firstly we use config file
    if args.use_config_file:
        try:
            config_file = find_config(config.project_dir)
        except EnvironmentException:
            my_print("Cannot find config file.")
            return
        config_params = load_config(config_file)
        config.project_dir = get_path_or_none(config_params.get("project"))
        config.analyze_targets = get_path_or_none(config_params.get("analyze_targets"))
        config.sys_paths = get_path_or_none(config_params.get("sys_paths"))
        config.output_dir = get_path_or_none(config_params.get("output"))
        config.requirements_file = get_path_or_none(config_params.get("requirements"))
        config.java = config_params.get("java")
        config.timeout = config_params.get("timeout")
        config.generate_only_error_suite = config_params.get(
            "generate_only_error_suite"
        )
        config.debug_mode = config_params.get("debug_mode")

    # Secondly we use cli-arguments
    if "--output-dir" in sys.argv or "-o" in sys.argv:
        config.output_dir = make_relative(
            pathlib.Path(args.output_dir), config.project_dir
        )
    if "--java" in sys.argv or "-j" in sys.argv:
        config.java = args.java
    if "--timeout" in sys.argv or "-t" in sys.argv:
        config.timeout = args.timeout
    if "--generate-only-error-suite" in sys.argv:
        config.generate_only_error_suite = args.generate_only_error_suite
    if "--analyze-targets" in sys.argv:
        config.analyze_targets = [
            make_relative(t, config.project_dir)
            for t in get_path_or_none(args.analyze_targets)
        ]
    if "--sys-paths" in sys.argv:
        config.sys_paths = get_path_or_none(args.sys_paths)
    if "--requirements-file" in sys.argv:
        config.requirements_file = get_path_or_none(args.requirements_file)
    if "--debug" in sys.argv:
        config.debug_mode = args.debug

    my_print("utfuzz started...")
    java_manager = JavaRequirementsManager(config.project_dir)

    # Java
    java_result, java = java_manager.check_base_java(config.java)
    if java_result != JavaResult.ValidJava:
        if not args.skip_dialog:
            install = read_with_action(
                "utfuzz depends on Java 17. Would you like to install? (Y/n) ",
                check_yes_no_with_default(True),
            )
            if install:
                my_print("Start Java installation...")
                java = java_manager.install_java()
                my_print(
                    f"Installed Java 17 to {java}. To set the path to it, use --java argument next time."
                )
            else:
                return

    if java is None:
        my_print(
            "Some problems with Java! To set a correct path to Java 17, use --java argument. "
            "See installation instructions in README.md."
        )
        return
    else:
        config.java = java
    my_print(f"Current Java: {config.java}")

    # Thirdly we use dialog
    if not args.skip_dialog:
        # Timeout
        timeout = config.get_or_default("timeout")
        my_print(
            f"Set timeout in seconds: per one class or top-level functions in one file. Leave empty to choose {timeout} s."
        )
        config.timeout = read_with_action(
            f"Timeout in seconds (default = {timeout} s): ",
            check_int_with_default(timeout),
        )

        # Project directory
        project_dir = config.get_or_default("project_dir")
        config.project_dir = read_with_action(
            f"Set your project root directory (default = {project_dir}): ",
            check_exists_path_with_default(project_dir),
        )

        # Analyze targets
        analyze_targets = config.get_or_default("analyze_targets")
        my_print(
            f"Specify files and directories to analyze: print one file/directory in a row; empty input "
            f"marks the end (by default, all files "
            f"{'from the project directory' if len(analyze_targets) == 0 else 'from configuration'} will be analyzed):"
        )
        while target := my_read(" * "):
            file_path = pathlib.Path(target)
            if not file_path.is_absolute():
                file_path = project_dir / file_path
            if not file_path.exists():
                my_print("   ^-- this file does not exists")
            if file_path.is_file():
                analyze_targets.append(file_path)
            elif file_path.is_dir():
                analyze_targets += get_py_files(file_path)
        if len(analyze_targets) == 0:
            analyze_targets = get_py_files(config.project_dir)
        config.analyze_targets = analyze_targets

        # Output directory
        output_dir = config.get_or_default("output_dir")
        config.output_dir = read_with_action(
            f"Set directory for tests (default = {output_dir}): ",
            check_valid_path_with_default(output_dir),
        )

        # Generate error suite
        generate_only_error_suite = config.get_or_default("generate_only_error_suite")
        config.generate_only_error_suite = read_with_action(
            f'Do you want to generate only an error suite? ({"Y/n" if generate_only_error_suite else "y/N"})  ',
            check_yes_no_with_default(generate_only_error_suite),
        )

    config.fill_default()
    config.resolve_paths()

    python_manager = PythonRequirementsManager(config.project_dir)
    if not python_manager.check_python():
        my_print("Please use Python 3.8 or newer.")
        return
    my_print("Installing Python dependencies...")
    python_manager.python_requirements_install()
    try:
        if config.requirements_file is None:
            python_manager.project_requirements_install()
        else:
            python_manager.project_requirements_install(config.requirements_file)
    except NotFoundRequirementsTxt:
        my_print(
            "Cannot find requirements.txt file. "
            "If your project has Python dependencies, please specify them in requirements.txt."
        )
    except MultipleRequirementsTxt:
        my_print(
            "Too many requirements.txt files found! Please use --requirements_file argument to set right"
        )
        return

    if len(config.analyze_targets) == 0:
        config.analyze_targets = get_py_files(config.project_dir)

    jar_path = (
        (pathlib.Path(__file__).parent / "utbot-cli-python.jar").resolve().absolute()
    )

    # Save config before test generation process
    save_config(config)

    my_print(f"Found {len(config.analyze_targets)} Python files to analyze.")
    for f in tqdm.tqdm(config.analyze_targets, desc="Progress"):
        test_file_name = f'test_{"_".join(f.relative_to(config.project_dir).parts)}'
        generate_tests(
            config.java,
            str(jar_path),
            [str(s) for s in config.sys_paths],
            sys.executable,
            str(f.resolve().absolute()),
            config.generate_only_error_suite,
            config.timeout,
            str((config.output_dir / test_file_name).resolve().absolute()),
            config.debug_mode,
        )
