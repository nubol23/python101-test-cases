# Función de ayuda para graficar los círculos

import numpy as np
import matplotlib.pyplot as plt

def graficar_circulo(x1, y1, r1, x2, y2, r2):
    theta = np.linspace(0, 2*np.pi, 100) 

    figure, axes = plt.subplots(1)
    
    a1 = r1*np.cos(theta) + x1
    b1 = r1*np.sin(theta) + y1
    axes.plot(a1, b1)
    
    a2 = r2*np.cos(theta) + x2
    b2 = r2*np.sin(theta) + y2
    axes.plot(a2, b2)
    
    axes.set_aspect(1)
    plt.grid(True)

    plt.title('Circulos')
    plt.show()
