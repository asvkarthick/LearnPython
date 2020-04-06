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
label = ttk.Label(win, text = "Label in GUI")
label.grid(column = 0, row = 0)

def click_button():
    button.configure(text = "Clicked")
    label.configure(foreground = 'red')
    label.configure(text = 'Button clicked')

button = ttk.Button(win, text = "Click Here", command = click_button)
button.grid(column = 1, row = 0)

# Start the GUI
win.mainloop()
