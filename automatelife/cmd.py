import argparse
import os
import sys

from .constants import DEFAULT_PROJECTS_DIR, LANGUAGES_DIR
from .core import Project
from .exceptions import ProjectExistsException
from .utils import discover_supported_languages


def __setup_args_parser__():
    """Sets up command line arguments."""
    parser = argparse.ArgumentParser(description='Create a project structure and some common files for the given '
                                                 'programing language.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("project_name", metavar="project_name", type=str, help="name of the project to be created")
    parser.add_argument("--dir", help="path to the directory where new project will be created",
                        default=DEFAULT_PROJECTS_DIR, type=str)
    parser.add_argument("--lang", help="project programming language",
                        choices=discover_supported_languages(LANGUAGES_DIR), default="python", type=str)
    parser.add_argument("--description", help="description of the project", default="TODO", type=str)
    return parser.parse_args()


def command_line_run():
    args = __setup_args_parser__()
    project = Project(args.project_name, args.description, args.lang, projects_root=args.dir)
    try:
        project_path = project.run()
        if sys.platform == "win32":
            os.startfile(project_path)
        else:
            print(f"Project created: {project_path}")
    except ProjectExistsException:
        print(f"Project ({args.project_name}) already exists")
        exit(-1)


if __name__ == '__main__':
    command_line_run()
