# Make Default Files and Folder Structure
 
## How to run on windows
For most people this should be enough,
```cmd
python3 -O __pycache__/make.pyc
```
if that does not work then do,
```cmd
python3 make.py
```
***Use the above command as a lost resort as 'make.py' is not compiled in Cython and is very unstable***


## How to run on Bash
For most people this should be enough,
```bash
$ chmod +x make.py
$ ./make.py
```
if that does not work then do,
```bash
python make.py
```
***Use the above command as a lost resort as 'make.py' is not compiled in Cython and is very unstable***

## What does this program do?
- This program will automatically create the following folders
- logs 
- database 
- config 
- backups 
- build 
- backend 
- backend/classes 
- backend/functions 
- backend/core 
- backend/data 
- backend/modules 
- frontend 
- frontend/client 
- frontend/server 
- frontend/assets 
- frontend/data 
- frontend/core 
- frontend/functions 
- frontend/classes 
- src 
- src/client 
- src/server 
- src/assets 
- src/data 
- src/core 
- src/functions 
- src/classes 
- dependencies 

## It also makes a fairly basic but usefull python files
- It creates an innit program where you can start your code
- It also creates a basic handler program which can backup your whole code base and keep track of logs
- it is also bundled with a admin module

## Extra Features
- Creates Log files
- Keeps track of the log files and deletes the oldest one when the limit is reached (the limit can be modified in the basic_handlr.py file)
- Makes backups of the entire dir and saves it to ~/backups
- Keeps track of the backup files and deletes the oldest one when the limit is reached (the limit can be modified in the basic_handlr.py file)
- the innit file has a var that you can toggle to make the program run with admin permission
