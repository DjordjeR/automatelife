# Automate life

This tool was made to make my life easier. Every time a need to create a new
project I start with the same basic structure, most of my python projects start 
the same, I need a directory, I need a readme and so on. This is why I decided 
to create this tool. To make it a little bit more usefully, the structure of 
the desired project can be defined as a JSON file. You can define some 
templates, directories and files you want to be created. Project definition in 
JSON file will change often since this is still very much work in progress. 
Other things might also change.

## Installation

```shell script
pip install -U git+https://github.com/djordjer/automatelife # Windows
pip3 install -U git+https://github.com/djordjer/automatelife # Linux
```

It is also possible to clone the repository and install it with pip.

```shell script
pip install . # Windows
pip3 install . # Linux
```

This will install the tool for usage if you want to develop the tool use:

 ```shell script
pip install -e . # Windows
pip3 install -e . # Linux
```

## Usage
```shell script
automate-life -h # To show help
automate-life project projectName --dir=/home/Projects --type=python
automate-life config -h # See all config options
```

## Author

* Djordje Rajic

## License
[GNU General Public License v3.0](LICENSE)


## TODOs

* [x] Create permanent config
* [ ] Templates for files
* [ ] Documentation
* [X] Basic Readme
