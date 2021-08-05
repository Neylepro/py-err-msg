## Py Error Gui Manager by Neylepro
import tkinter as tk  
from tkinter import ttk  
from tkinter import Menu  
from tkinter import messagebox as mbox  
errgui = tk.Tk()
errgui.title("Error")
ttk.Label(errgui, text="An Error was detected")


def StartErrorGui(error, appname):
  errgui.showwarning("Error :" + error)
  errgui.mainLoop()
