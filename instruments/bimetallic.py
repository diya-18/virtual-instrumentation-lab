import numpy as np
import matplotlib.pyplot as plt

def bimetallic_deflection(alpha1, alpha2, delta_T, K=1):
    return K * (alpha1 - alpha2) * delta_T

def plot_bimetallic_response():
    T = np.linspace(0, 200, 50)   # Temperature range (°C)

    alpha1 = 19e-6   # Brass
    alpha2 = 11e-6   # Steel

    deflection = bimetallic_deflection(alpha1, alpha2, T)

    plt.plot(T, deflection)
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Deflection (arbitrary units)")
    plt.title("Bimetallic Thermometer Response")
    plt.grid()
    plt.show()
