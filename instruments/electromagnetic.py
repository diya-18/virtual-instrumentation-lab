import numpy as np
import matplotlib.pyplot as plt

def induced_voltage(B, L, v):
    """
    Calculates induced EMF in an electromagnetic flow meter.
    B : magnetic flux density (Tesla)
    L : electrode spacing / pipe diameter (m)
    v : fluid velocity (m/s)
    """
    return B * L * v

def plot_em_flowmeter_response():
    B = 0.5        # Tesla
    L = 0.05       # Pipe diameter (m)

    v = np.linspace(0.1, 5, 50)   # Velocity range (m/s)
    E = induced_voltage(B, L, v)

    plt.figure()
    plt.plot(v, E)
    plt.xlabel("Fluid Velocity (m/s)")
    plt.ylabel("Induced Voltage (V)")
    plt.title("Electromagnetic Flow Meter Response")
    plt.grid(True)
    plt.show()
