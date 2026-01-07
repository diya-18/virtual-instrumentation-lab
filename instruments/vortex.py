import numpy as np
import matplotlib.pyplot as plt

def vortex_frequency(v, d, St=0.2):
    """
    Calculates vortex shedding frequency.
    v  : fluid velocity (m/s)
    d  : bluff body width (m)
    St : Strouhal number
    """
    return St * v / d

def plot_vortex_response():
    d = 0.02  # bluff body width (m)
    v = np.linspace(0.1, 5, 50)

    f = vortex_frequency(v, d)

    plt.figure()
    plt.plot(v, f)
    plt.xlabel("Fluid Velocity (m/s)")
    plt.ylabel("Vortex Frequency (Hz)")
    plt.title("Vortex Flow Meter Response")
    plt.grid(True)
    plt.show()
