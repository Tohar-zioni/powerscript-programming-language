import tkinter as tk
from tkinter import *

window = tk.Tk()


Token = ""
ttitle = ""
size = ""
color = ""
ltext = ""
def xtitle():
        window.title(ttitle)
def xsize():
      #ac.size "100x100"
    size = ""
    window.geometry(size)
    window.config(bg= color)
def label():
    ltext = ""
    Label(window, text=ltext)

def xwindow():
    window.title("AppCreator.ps window")
    window.geometry("800x800")
    window.mainloop()