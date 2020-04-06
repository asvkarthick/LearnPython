#!/usr/bin/python3
# Author: Karthick Kumaran <asvkarthick@gmail.com>
# Simple GUI Program with just a window and a label

import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()

# Set the title for the window
win.title("Python GUI with a label")

# Add a label
ttk.Label(win, text = "Label in GUI").grid(column = 0, row = 0)

# Start the GUI
win.mainloop()
