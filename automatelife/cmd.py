import argparse
import os
import sys

from .config import Config
from .core import Project
from .exceptions import ProjectExistsException
from .utils import discover_supported_languages


def __setup_args_parser__(config):
    """Sets up command line arguments."""

    parser = argparse.ArgumentParser(description='Create a project structure and some common files for the given '
                                                 'programing language.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers(help="choose command", dest="command")
    subparsers.required = True

    config_parser = subparsers.add_parser("config", help="create a program configuration",
                                          formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    config_parser.add_argument("-i", "--interactive", action="store_true",
                               help="create configuration file interactively")
    possible_settings_group = config_parser.add_argument_group(description="Possible settings")

    for setting in vars(config).keys():
        possible_settings_group.add_argument(f"--{setting}", default=None)

    project_parser = subparsers.add_parser("project", help="create a new project",
                                           formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    project_parser.add_argument("name", metavar="name", type=str, help="name of the project")
    project_parser.add_argument("-d", "--directory", help="path to the directory where new project will be created",
                                default=config.projects_dir, type=str)
    project_parser.add_argument("-l", "--language", help="project programming language",
                                choices=discover_supported_languages(config.languages_dir), default="python", type=str)
    project_parser.add_argument("-dsc", "--description", help="description of the project", default="TODO", type=str)

    return parser.parse_args()


def command_line_run():
    """ Parse the command line arguments and execute appropriate functions."""
    print("TESTINGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
    config = Config()
    args = __setup_args_parser__(config)
    print(args)
    if args.command == "project":
        project = Project(args.project_name, args.description, args.lang, project_path=args.dir)
        try:
            project_path = project.run()
            if sys.platform == "win32":
                os.startfile(project_path)
            else:
                print(f"Project created: {project_path}")
        except ProjectExistsException:
            print(f"Project ({args.project_name}) already exists")
            exit(-1)
    elif args.command == "config":
        for setting in vars(config).keys():
            value = getattr(args, setting)
            if value is not None:
                setattr(config, setting, value)
        print(config.save())
    else:
        raise TypeError


if __name__ == '__main__':
    command_line_run()
