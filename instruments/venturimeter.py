import numpy as np
import matplotlib.pyplot as plt
def venturimeter_flow_rate(D1,D2,h,Cd=0.97,g=9.81):
    """
    Calculates discharge through a venturimeter.
    Parameters:
    D1 : inlet diameter(m)
    D2 : throat diameter(m)
    h : manometer head(m)
    Cd : discharge coefficient (default is 0.97)
    g : acceleration due to gravity (default is 9.81 m/s^2)
    Returns:
    Q : flow rate (m^3/s)
    """
    A1=np.pi*D1**2/4
    A2=np.pi*D2**2/4
    Q=Cd*A2*np.sqrt((2*g*h)/(1-(A2/A1)**2))
    return Q
def plot_flow_rate_vs_head(D1,D2):
    h=np.linspace(0.01,0.5,50)
    Q=venturimeter_flow_rate(D1,D2,h)
    plt.figure()
    plt.plot(h,Q)
    plt.xlabel('Manometer Head (m)')
    plt.ylabel('Flow Rate (m^3/s)')
    plt.title('Flow Rate vs Manometer Head for Venturimeter')
    plt.grid(True)
    plt.show()