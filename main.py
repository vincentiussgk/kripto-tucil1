from tkinter import *
import time
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import csv
import os
from vigenere_cypher.vigenere_cypher import *

root = Tk()
root.title("Kriptografi, Tucil 1")
root.geometry("600x600")

def menu1():
    root.destroy()
    import vigenere_cypher.vigenere_cypher_gui 
def menu2():
    root.destroy()
    import playfair_cypher.playfair_cypher_gui
def menu3():
    root.destroy()
    import onetimepad.onetimepad_gui
# def menu4():
#     root.destroy()
#     import otp_gui

vigenereMenu = Button(
        text="Vigenere Cypher",
        width=15,
        height=5,
        bg="blue",
        fg="yellow",
        command = menu1
    )
vigenereMenu.pack()

playfairMenu = Button(
        text="Playfair Cypher",
        width=15,
        height=5,
        bg="blue",
        fg="yellow",
        command = menu2
    )
playfairMenu.pack()

oneTimePadMenu = Button(
        text="One Time Pad",
        width=15,
        height=5,
        bg="blue",
        fg="yellow",
        command = menu3
    )
oneTimePadMenu.pack()

# Start the app

root.mainloop()