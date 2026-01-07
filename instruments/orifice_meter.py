import numpy as np
import matplotlib.pyplot as plt

def orifice_flow_rate(D, d, h, Cd=0.6, g=9.81):
    """
    Calculates flow rate through an orifice meter.
    D : pipe diameter (m)
    d : orifice diameter (m)
    h : pressure head (m)
    """
    A_o = np.pi * d**2 / 4
    beta = d / D

    Q = Cd * A_o * np.sqrt((2 * g * h) / (1 - beta**4))
    return Q

def plot_orifice_characteristic():
    D = 0.05     # pipe diameter (m)
    d = 0.025    # orifice diameter (m)

    h = np.linspace(0.01, 0.5, 50)
    Q = orifice_flow_rate(D, d, h)

    plt.figure()
    plt.plot(h, Q)
    plt.xlabel("Pressure Head h (m)")
    plt.ylabel("Flow Rate Q (m³/s)")
    plt.title("Orifice Meter: Flow Rate vs Pressure Head")
    plt.grid(True)
    plt.show()
