from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# REF: https://github.com/pypa/sampleproject/blob/master/setup.py
setup(name='automatelife',
      version='0.1',
      description='Simple project creation automation :)',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/DjordjeR/automatelife',
      author='Djordje Rajic',
      author_email='rajicdj@gmail.com',
      license='MIT',
      packages=['automatelife'],
      install_requires=['GitPython'],
      entry_points={  # Optional
          'console_scripts': [
              'automatelife=automatelife:command_line_run',
          ],
      },
      package_data={
            "automatelife": ["templates/*.md", "templates/languages/*.json"],
      },
      zip_safe=False)