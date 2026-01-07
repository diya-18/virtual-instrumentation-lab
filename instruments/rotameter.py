import numpy as np
import matplotlib.pyplot as plt

def rotameter_flow(area, volume, rho_float, rho_fluid, Cd=0.62):
    g = 9.81
    Q = Cd * area * np.sqrt((2 * g * volume * (rho_float - rho_fluid)) / rho_fluid)
    return Q

def plot_rotameter_characteristic():
    area = np.linspace(1e-4, 5e-4, 20)  # increasing annular area
    volume = 5e-5
    rho_float = 7800     # steel
    rho_fluid = 1000     # water

    Q = rotameter_flow(area, volume, rho_float, rho_fluid)

    plt.plot(area, Q)
    plt.xlabel("Annular Area (m²)")
    plt.ylabel("Flow Rate (m³/s)")
    plt.title("Rotameter Flow Characteristic")
    plt.grid()
    plt.show()
