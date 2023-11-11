# PYTHON_ARGCOMPLETE_OK
import argparse
import importlib
import pkgutil

import argcomplete

import dcsm


def main_PYTHON_ARGCOMPLETE_OK():
    """Entry point for the command line interface"""

    commands = get_available_commands()
    args = parse_args(commands)
    chosen_command = commands[args.command]
    chosen_command.run(args)


def get_available_commands() -> dict[str, importlib.types.ModuleType]:
    """Return a dictionary of available commands in dcsm/commands

    Underscrores in module names are replaced with hyphens in command names.
    """

    commands = {}
    module_names = get_available_command_module_names()

    for module_name in module_names:
        command_module = importlib.import_module(f"dcsm.commands.{module_name}")
        command_name = module_name.replace("_", "-")
        commands[command_name] = command_module

    return commands


def get_available_command_module_names() -> list[str]:
    """Return a list of available commands in dcsm/commands"""

    command_names = []

    for module in pkgutil.iter_modules(dcsm.commands.__path__):
        if module.name == "main":
            continue
        command_names.append(module.name)

    return command_names


def parse_args(commands: dict[str, importlib.types.ModuleType]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    # Create subparsers for each command
    command_parsers = parser.add_subparsers(dest="command", help="command to run")
    command_parsers.required = True

    for command_name, command_module in commands.items():
        command_help = getattr(command_module, "COMMAND_HELP", "")
        command_parser = command_parsers.add_parser(command_name, help=command_help)
        command_module.populate_arg_parser(command_parser)

    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main_PYTHON_ARGCOMPLETE_OK()
