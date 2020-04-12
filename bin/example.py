from automatelife.core import Project
from automatelife.language import SupportedLanguages

if __name__ == "__main__":
    pr = Project("ExampleProject", "Some awesome description", SupportedLanguages.PYTHON)
    pr.run()
