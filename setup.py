from setuptools import setup

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# REF: https://github.com/pypa/sampleproject/blob/master/setup.py
setup(name="automatelife",
      version="1.0.0-dev.1",
      description="Simple project creation automation :)",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/DjordjeR/automatelife",
      author="Djordje Rajic",
      author_email="rajicdj@gmail.com",
      license="GPL",
      packages=["automatelife"],
      install_requires=["GitPython"],
      entry_points={  # Optional
          "console_scripts": [
              "automatelife=automatelife:command_line_run",
          ],
      },
      package_data={
          "automatelife": ["templates/*.md", "templates/languages/*.json"],
      },
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Automation Tools",
          "License :: OSI Approved :: GPL-3.0  License",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
      ],
      python_requires='>=3.6',
      zip_safe=False)
