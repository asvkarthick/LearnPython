#!/usr/bin/python3
# Author: Karthick Kumaran <asvkarthick@gmail.com>
# Simple GUI Program with just a window resize disabled

import tkinter as tk

# Create instance
win = tk.Tk()

# Set the title for the window
win.title("Python GUI Hello World")

# Disable resizing
win.resizable(False, False)

# Start the GUI
win.mainloop()
