#!/usr/bin/python3
# Author: Karthick Kumaran <asvkarthick@gmail.com>
# Simple GUI Program with Label, Button & TextBox

import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()

# Set the title for the window
win.title("Python GUI with a label")

# Add a label
label = ttk.Label(win, text = "Enter name:")
label.grid(column = 0, row = 0)

def click_button():
    button.configure(text = "Clicked")
    label.configure(text = "Hello " + text.get())

button = ttk.Button(win, text = "Click Here", command = click_button)
button.grid(column = 1, row = 1)

text = tk.StringVar()
textbox = ttk.Entry(win, width = 12, textvariable = text)
textbox.grid(column = 0, row = 1)

# Start the GUI
win.mainloop()
