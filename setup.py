# read the contents of your README file
from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# REF: https://github.com/pypa/sampleproject/blob/master/setup.py
setup(
    name="automatelife",
    version="0.0.1-dev.2",
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
            "automate-life=automatelife:command_line_run",
        ],
    },
    package_data={
        "automatelife": ["static/templates/*.md",
                         "static/lang_definitions/*.json"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Automation Tools",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.8",
    ],
    platforms=["any"],
    python_requires='>=3.8',
    zip_safe=False)
