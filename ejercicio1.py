#Escriba el codigo necesario para que al ejecutar
#python ejercicio1.py se impriman los enteros del 10 al 1 en cuenta regresiva.

import numpy as np
import matplotlib.pyplot as plt

lista=[]
for i in range (11):
    lista.append(i)
    
num=0    
for i in lista:
    num+=1
    print (lista[-num])
    

    