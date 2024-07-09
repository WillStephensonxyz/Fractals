import tkinter as tk 
from tkinter import ttk 
import numpy 
# from fractals import mandelbrot_set, julia_set 

root = tk.Tk()

#Define geometry and disable menu tearoff 
root.geometry("800x500")
root.option_add('*tearOff', False) 

#Define frame 
frame = ttk.Frame(root, padding=10) 
frame.grid()

#Create dropdown menu and define hotkeys
menubar = tk.Menu(root) 
options = tk.Menu(menubar, tearoff=False) 

options.add_cascade(label="Fullscreen       Ctrl+f") 
options.add_cascade(label="Generate Pattern Ctrl+n")
options.add_cascade(label="Exit             Ctrl+k") 

menubar.add_cascade(label="Options", menu=options) 

#Frame text and button, testing purposes
ttk.Label(frame, text="Hello World!").grid(column=0, row=0) 
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0) 

root.config(menu=menubar) 
root.mainloop() 
