# interfaz_terminal
# Description
This project is a basic interfaz by terminal, for incorpore in other python projects. 
The program, request 'rules' and after ask to the user specific credentials for each rule (for example user name, password, email...)
You need to specify the path where the 'rules' (configurations of credentials) and credentials json files, will be. 
# Functions
## printCredentials ()
Print by terminal all credentials inside credentials json file. 
## printConfigCredentials ()
Print by terminal the rules/the configuration of the credentials inside the configuration file.
## requestCredentials ()
Ask to the user by terminal, for each credential from the configuration file. 
## requestConfigCredentials ()
Ask to the user by terminal, for configuration of each credential: name, description, and validation.
## getCredentials ()
Return a dictionary with the credentials information. 

# How to use

## Instance of the class

To use the program, you need to **make a instance of the Interfaz class**, in your current project

```python
# import class from the module
from interfaz import Interfaz 

...

# Instance of the class
myInterfaz = Interfaz(pathCredentials, pathConfig)
```

## Credentials configuration

The first time that you run the program, **it will request the configutation of the credentials**: 

### Name: 
Is the **name of the credential**. After, you will access to the user information with this name. 
Example: *name, email, phone, address...*
### Description
An aditional **text to help user** to set a correct input.
Example: *Type your complite email address*
### Validation
This is an **rule to verify** if **the user** input is correct.
Validation has tree options: 

* **character:** if you type *only a character/word* (for example: @), the program will check if the **user input has this in the text**.
* **list:** if you type *a list of characters/words* (for example: ["@", ".","com"]) the program will check if **all of characters/words are in the text**.
* **number:** if you type *only a number* (for example 10), the program will check if the **extension of the input is at least** this number of characters.

You need to write **a rule** for **each of the credentials** that you will request from the user

## Credentials input

After set the configuration of the credentials, *if the credentials file does not exist or is empty*, the system will request them.

The program will request the credentials **one by one, displaying the name and description** on the screen.
**Only if the user input pass the validation, it will continue**. 

## Get credentials
You can get the credentials using the **getCredentials function**. It returns a dictionary, where each key is the name of the credential

## Terminal help and opcions

Running the program by terminal, you can:
* Get information. 
* List credentials or configurations.
* Edit credentials or configurations.

```bash
$ python3 main.py --help
* #Run the to request credentials or configuration of credentials if it doesn't exist. 
* #write '-l --cred' to see all credentials \
* #write '-l --config' to see all credentials configuration options. \
* #write '-e --config' to edit all credentials configuration options. \
* #write '-e --cred' to edit all credentials"
```

# How to use example

## Make a instance

```python
# import class from the module
from interfaz import Interfaz 

# indicate the json files
pathCredentials = 'usr/myProject/credentials.json') 
pathConfig = 'usr/myProject/config.json')

# Instance of the class
myInterfaz = Interfaz(pathCredentials, pathConfig)
```

## Credentials configuration

* Credential 1 name: **email**
* Credential 1 description: **Type your complite email address**
* Credential 1 validation: **["@", '.']**
* Other credential? (y/n): **y**
* Credential 2 name: **password**
* Credential 2 description: **Type the password of your email**
* Credential 2 validation: 5

## Credentials input

* Plase, capture your information
* email (Type your complite email address): **emailexample@gmail.com**
* password (Type the password of your email): **my passowrd 123**

## Get credentials

```python
...

# Instance of the class
myInterfaz = Interfaz(pathCredentials, pathConfig)
credentials = myInterfaz.getCredentials()

print (credentials['email'])
# emailexample@gmail.com

print (credentials['password'])
# my passowrd 123

```