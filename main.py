print("Virtual Instrumentation Lab Initialized")
from instruments import venturimeter

# Example parameters
D1 = 0.05   # inlet diameter (m)
D2 = 0.025  # throat diameter (m)

venturimeter.plot_flow_rate_vs_head(0.05, 0.025)
