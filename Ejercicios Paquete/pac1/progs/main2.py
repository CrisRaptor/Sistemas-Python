from sys import path
import os
#path.append('C:\\Users\\ALUMNO2425\\Documents\\VSCode\\Python\\Ejercicios Paquete\\pac1')
path.append(os.path.join(os.path.dirname(__file__),".."))

import packages.extra.iota as iota
print(iota.FunI())

import packages.extra.good.best.sigma as sigma
from packages.extra.good.best.tau import FunT

print(sigma.FunS())
print(FunT())

