# PL-python-project
Conversion of basic parser/lexer to PLY from C
## Install Requirements
This project requires a python environment with PLY installed.

## Directory Structure
There are three main files contained within the project. 
* `projectOne.py` is for running the first programming assignment.
* `projectTwo.py` is for running the second programming asignment.
* `projectTwoLexer.py` stores the lexer for project two. Do not attempt to run this file.

## Execution instructions
Both project drivers accept `stdin` as their input. Meaning there are a variety of ways to input data:

* `python projectTwo.py < inputs/expr1_pass.smp`
  + A series of example inputs are located within the `inputs/` directory
* `echo "2+2=6" | python projectOne.py`
* Input directly from console
  + Note: `ProjectTwo.py` requires you press CTRL+D after completing your program input in order to run.
