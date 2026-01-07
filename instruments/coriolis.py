import numpy as np
import matplotlib.pyplot as plt

def coriolis_phase_shift(m_dot, k=1):
    """
    Calculates phase shift proportional to mass flow rate.
    m_dot : mass flow rate (kg/s)
    k     : proportionality constant
    """
    return k * m_dot

def plot_coriolis_response():
    m_dot = np.linspace(0.1, 10, 50)  # mass flow rate (kg/s)

    phase_shift = coriolis_phase_shift(m_dot)

    plt.figure()
    plt.plot(m_dot, phase_shift)
    plt.xlabel("Mass Flow Rate (kg/s)")
    plt.ylabel("Phase Shift (arbitrary units)")
    plt.title("Coriolis Mass Flow Meter Response")
    plt.grid(True)
    plt.show()

"""
Linearity: Because mass measurement is direct and independent of fluid properties like viscosity or density, 
the meter operates in a linear fashion across its entire usable range.

"""