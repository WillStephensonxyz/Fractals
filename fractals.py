import tkinter as tk 
from tkinter import ttk 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 

root = tk.Tk()

def fullscreen(event): 
    state = not root.attributes("-fullscreen") 
    root.attributes('-fullscreen', state)

def killwindow(event):
    root.destroy() 

root.bind("<Control-q>", killwindow) 
root.bind("<Control-f>", fullscreen) 

#Define geometry and disable menu tearoff 
root.geometry("800x500")
root.option_add('*tearOff', False) 

#Define frame 
frame = ttk.Frame(root, padding=10) 
frame.grid()

#Create dropdown menu and define hotkeys
menubar = tk.Menu(root) 
options = tk.Menu(menubar, tearoff=False) 

options.add_cascade(label="Fullscreen       Ctrl+F") 
options.add_cascade(label="Exit             Ctrl+Q") 
options.add_cascade(label="Pause            Ctrl+P") 
options.add_cascade(label="Generate Pattern Ctrl+N")

menubar.add_cascade(label="Options", menu=options) 

# Creating frame widget for animation 

root.config(menu=menubar) 
root.mainloop() 
