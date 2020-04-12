from automatelife.core import Project, SupportedLanguages


def command_line_run():
    pr = Project("ExampleProject", "Some awesome description", SupportedLanguages.PYTHON)
    pr.run()
