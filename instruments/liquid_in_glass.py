import numpy as np
import matplotlib.pyplot as plt

def liquid_column_height(T, beta, V0, K=1):
    """
    Calculates liquid column height change.
    T    : temperature (°C)
    beta : volumetric expansion coefficient
    V0   : initial volume
    K    : proportionality constant
    """
    return K * V0 * beta * T

def plot_liquid_in_glass_response():
    T = np.linspace(0, 100, 50)   # Temperature range (°C)

    beta = 1.8e-4   # Mercury (approx)
    V0 = 1e-6       # Initial volume (m^3)

    height = liquid_column_height(T, beta, V0)

    plt.figure()
    plt.plot(T, height)
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Liquid Column Height (arbitrary units)")
    plt.title("Liquid-in-Glass Thermometer Response")
    plt.grid(True)
    plt.show()
