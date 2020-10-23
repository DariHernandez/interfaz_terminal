import os
from interfaz import Interfaz

path = os.path.dirname (__file__)
pathCredentials = os.path.join (path, 'credentials.json')
pathConfig = os.path.join (path, 'config.json')

currentInterfaz = Interfaz(pathCredentials, pathConfig)
credentials = currentInterfaz.getCredentials()