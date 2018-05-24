# Escriba el codigo necesario para que al ejecutar python ejercicio2.py
# se cree una grafica con una funcion sinusoidal entre 0 y 2pi.

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def seno(x):
    return np.sin(x)

x=np.linspace(0.0,2.0*np.pi,100)
y=seno(x)

plt.figure()
plt.plot(x,y)
plt.savefig('Graph.png')
plt.show()