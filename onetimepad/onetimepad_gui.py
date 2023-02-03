from tkinter import *
import tkinter.filedialog as filedialog
from tkinter import messagebox

from onetimepad.onetimepad import *

root = Tk()
root.title("Kriptografi, Tucil 1")
root.geometry("600x600")

otpTitle = Label(
    text="One Time Pad"
)
otpTitle.pack()

def returnHome():
    root.destroy()
    import main 

oneTimePadBackButton = Button(
    text="Back",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = returnHome
)
oneTimePadBackButton.pack()


# Load text
def loadResultFromFile():
    textfile = filedialog.askopenfilename(initialdir = ".",
            title = "Select a File",
            filetypes = (("Text files",
                        "*.txt*"),
                        ("all files",
                        "*.*")))
    textfile = open(textfile)
    cypherData = textfile.read()
    oneTimePadInputTextbox.delete(0, END)
    oneTimePadInputTextbox.insert(END, cypherData)

oneTimePadLoadButton = Button(
    text="Load",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = loadResultFromFile
)
oneTimePadLoadButton.pack()

# Viginere Row

# oneTimePad - Text
oneTimePadLabel = Label(
    text="Enter Text"
)
oneTimePadLabel.pack()

oneTimePadInputTextbox = Entry()
oneTimePadInputTextbox.pack()

# oneTimePad Key 

oneTimePadKeyLabel = Label(
    text="Enter Key"
)
oneTimePadKeyLabel.pack()

oneTimePadKeyTextbox = Entry()
oneTimePadKeyTextbox.pack()

def oneTimePadEncyrpt():
    oneTimePadInput = oneTimePadInputTextbox.get()
    oneTimePadKey = oneTimePadKeyTextbox.get()
    encryptResult, encryptResultSpaced = onetimepad_encrypt(oneTimePadInput, oneTimePadKey)

    if (encryptResult == 0):
        messagebox.showinfo("Error!", encryptResultSpaced)

    else:
        oneTimePadResultTextbox.delete(0, END)
        oneTimePadResultTextbox.insert(END, encryptResult)

        oneTimePadResultSpacedTextbox.delete(0, END)
        oneTimePadResultSpacedTextbox.insert(END, encryptResultSpaced)

oneTimePadEncryptButton = Button(
    text="Encrypt",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = oneTimePadEncyrpt
)
oneTimePadEncryptButton.pack()

# Decryption
def oneTimePadDecyrpt():
    oneTimePadEncrypted = oneTimePadInputTextbox.get()
    oneTimePadKey = oneTimePadKeyTextbox.get()
    decryptResult, decryptResultSpaced = onetimepad_decrypt(oneTimePadEncrypted, oneTimePadKey)
    
    if (decryptResult == 0):
        messagebox.showinfo("Error!", decryptResultSpaced)

    else:
        oneTimePadResultTextbox.delete(0, END)
        oneTimePadResultTextbox.insert(END, decryptResult)

        oneTimePadResultSpacedTextbox.delete(0, END)
        oneTimePadResultSpacedTextbox.insert(END, decryptResultSpaced)

oneTimePadDecyrptButton = Button(
    text="Decrypt",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = oneTimePadDecyrpt
)
oneTimePadDecyrptButton.pack()

# Result
oneTimePadResult = Label(
    text="Result"
)
oneTimePadResult.pack()

oneTimePadResultTextbox = Entry()
oneTimePadResultTextbox.pack()

virgenereResultSpaced = Label(
    text="Result (5-Character Spaced)"
)
virgenereResultSpaced.pack()

oneTimePadResultSpacedTextbox = Entry()
oneTimePadResultSpacedTextbox.pack()

# Write to file
def saveResultToFile():
    f = open("cypher_result.txt", "w")
    f.write(oneTimePadResultTextbox.get())
    f.close()

oneTimePadSaveButton = Button(
    text="Save",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = saveResultToFile
)
oneTimePadSaveButton.pack()