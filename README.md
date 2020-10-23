# interfaz_terminal
# Description
This project is a basic interfaz by terminal, for incorpore in other python projects. 
The program, request 'rules' and after request to the user specific credentials for each rule (like user name, password, email...)
You need to specify the path where the 'rules' (configurations of credentials) and credentials, will be, both in json files. 
# How to use

## Instance of the class

#To use the program, you need to make a instance of the Interfaz class, in your current project

...
**from interfaz import Interfaz** # import class from the module

**pathCredentials = 'usr/myProject/credentials.json')** # indicate the json files

**pathConfig = 'usr/myProject/config.json')**

**my = Interfaz(pathCredentials, pathConfig)** # Instance of the class
...


## Credentials configuration request

## Credentials request
