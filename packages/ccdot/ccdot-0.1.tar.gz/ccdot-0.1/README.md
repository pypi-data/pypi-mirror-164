# cc
Utility to manage blocks of env variables, and paths, as a single context. 

Applications:
* facilitate multiple experiments with inter-process apps 
* repeat identical interaction with multiple remote devices
* switch easily among different folders when working with multiple datasets 

## How it works
The script command takes in a context name or id and changes a group of env variables and console settings based on a configuration file. 

## Setup
Requires python 3.9 or later (https://www.python.org/downloads/release/python-3912/)
 
pip install ccdot


## Usage
| command | effect |
| --- | --- |
|cc. | show current computing context   |
|cc. mycontext | change context to context namd 'mycontext'   |
|cc. info | list all available contexts   |
|cc. help | show help   |

## Customizing Config File
Edit the cc/cfg/command.json to add new context commands. 




 
