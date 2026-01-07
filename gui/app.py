import tkinter as tk
from tkinter import ttk

from instruments.venturimeter import plot_flow_rate_vs_head
from instruments.rotameter import plot_rotameter_comparison
from instruments.bimetallic import plot_bimetallic_response
from instruments.liquid_in_glass import plot_liquid_in_glass_response
from instruments.orifice_meter import plot_orifice_characteristic
from instruments.electromagnetic import plot_em_flowmeter_response
from instruments.vortex import plot_vortex_response
from instruments.coriolis import plot_coriolis_response


def run_simulation():
    instrument = selected.get()

    if instrument == "Venturimeter":
        plot_flow_rate_vs_head(0.05, 0.025)

    elif instrument == "Rotameter":
        plot_rotameter_comparison()

    elif instrument == "Bimetallic Thermometer":
        plot_bimetallic_response()

    elif instrument == "Liquid-in-Glass Thermometer":
        plot_liquid_in_glass_response()

    elif instrument == "Orifice Meter":
        plot_orifice_characteristic()

    elif instrument == "Electromagnetic Flow Meter":
        plot_em_flowmeter_response()

    elif instrument == "Vortex Flow Meter":
        plot_vortex_response()

    elif instrument == "Coriolis Mass Flow Meter":
        plot_coriolis_response()


# -------- GUI Window --------
root = tk.Tk()
root.title("Virtual Instrumentation Lab")
root.geometry("400x250")

title = tk.Label(root, text="Virtual Instrumentation Lab",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)

selected = tk.StringVar()

instrument_list = [
    "Venturimeter",
    "Rotameter",
    "Bimetallic Thermometer",
    "Liquid-in-Glass Thermometer",
    "Orifice Meter",
    "Electromagnetic Flow Meter",
    "Vortex Flow Meter",
    "Coriolis Mass Flow Meter"
]

dropdown = ttk.Combobox(root, textvariable=selected,
                        values=instrument_list, state="readonly")
dropdown.pack(pady=10)
dropdown.current(0)

run_btn = tk.Button(root, text="Run Simulation",
                    command=run_simulation,
                    font=("Arial", 12))
run_btn.pack(pady=20)

root.mainloop()
