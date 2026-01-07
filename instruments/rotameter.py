import numpy as np
import matplotlib.pyplot as plt

# -------- Linear (Practical Rotameter) --------
def linear_rotameter(area, volume, rho_float, rho_fluid, Cd=0.62):
    g = 9.81
    Q = Cd * area * np.sqrt((2 * g * volume * (rho_float - rho_fluid)) / rho_fluid)
    return Q

# -------- Non-linear (Theoretical Rotameter) --------
def nonlinear_rotameter(height, volume, rho_float, rho_fluid, Cd=0.62):
    g = 9.81
    # Annular area increases nonlinearly with height (ideal case)
    area = height**2
    Q = Cd * area * np.sqrt((2 * g * volume * (rho_float - rho_fluid)) / rho_fluid)
    return Q

def plot_rotameter_comparison():
    volume = 5e-5
    rho_float = 7800   # steel
    rho_fluid = 1000   # water

    # ----- Practical (Linear) -----
    area = np.linspace(1e-4, 5e-4, 20)
    Q_linear = linear_rotameter(area, volume, rho_float, rho_fluid)

    x_linear = (area - area.min()) / (area.max() - area.min())  # normalize

    # ----- Theoretical (Non-linear) -----
    height = np.linspace(0.01, 0.05, 20)
    Q_nonlinear = nonlinear_rotameter(height, volume, rho_float, rho_fluid)

    x_nonlinear = (height - height.min()) / (height.max() - height.min())  # normalize

    # ----- Plot -----
    plt.figure()
    plt.plot(x_linear, Q_linear, 'o-', label="Practical (Linear)")
    plt.plot(x_nonlinear, Q_nonlinear, 's-', label="Theoretical (Non-linear)")

    plt.xlabel("Normalized Float Position")
    plt.ylabel("Flow Rate (m³/s)")
    plt.title("Rotameter Characteristics: Practical vs Theoretical")
    plt.legend()
    plt.grid(True)
    plt.show()


"""
The non-linear curve represents the theoretical square-root behavior of a rotameter, 
while the linear curve represents practical instruments where tube taper and float geometry are designed
to linearize the output.
Since practical and theoretical rotameter models use different physical parameters, 
I normalized the float position to compare their characteristics on the same scale.
"""