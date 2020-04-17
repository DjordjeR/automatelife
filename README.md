# Automate life

This tool was made to make my life easier. Every time a need to create a new project I start with the same
basic structure, most of my python projects start the same, I need directory, I need a readme and so on. This 
is why I decided to create this tool. In order to make it a little bit more usefully the structure of the 
desired project can be defined as a json file. You can define some templates, directories and files you want created. 

Project definition in json file will change often since this is still very much work in progress. Other things might also
change. 

## Installation

Right now it is possible to clone this repository and install it with pip.

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
automatelife -h # To show help
automatelife projectName --dir=/home/Projects --lang=python
```

## Author

* Djordje Rajic

## License
[GNU General Public License v3.0](LICENSE)


## TODOs

* [ ] Create permanent config
* [ ] Publish to pypi
* [ ] Add changelog
* [ ] Semantic versioning
* [ ] Documentation
* [ ] Unit tests
* [X] Basic Readme
