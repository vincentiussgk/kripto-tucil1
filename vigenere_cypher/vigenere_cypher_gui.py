from tkinter import *
import tkinter.filedialog as filedialog

from vigenere_cypher.vigenere_cypher import *

root = Tk()
root.title("Kriptografi, Tucil 1")
root.geometry("600x600")

def returnHome():
    root.destroy()
    import main 

vigenereBackButton = Button(
    text="Back",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = returnHome
)
vigenereBackButton.pack()

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
    vigenereInputTextbox.delete(0, END)
    vigenereInputTextbox.insert(END, cypherData)

vigenereLoadButton = Button(
    text="Load",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = loadResultFromFile
)
vigenereLoadButton.pack()

# Viginere Row

# Vigenere - Text
vigenereLabel = Label(
    text="Enter Text"
)
vigenereLabel.pack()

vigenereInputTextbox = Entry()
vigenereInputTextbox.pack()

# Vigenere Key 

vigenereKeyLabel = Label(
    text="Enter Key"
)
vigenereKeyLabel.pack()

vigenereKeyTextbox = Entry()
vigenereKeyTextbox.pack()

def vigenereEncyrpt():
    vigenereInput = vigenereInputTextbox.get()
    vigenereKey = vigenereKeyTextbox.get()
    encryptResult, encryptResultSpaced = vigenere_encrypt(vigenereInput, vigenereKey)

    vigenereResultTextbox.delete(0, END)
    vigenereResultTextbox.insert(END, encryptResult)

    vigenereResultSpacedTextbox.delete(0, END)
    vigenereResultSpacedTextbox.insert(END, encryptResultSpaced)

vigenereEncryptButton = Button(
    text="Encrypt",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = vigenereEncyrpt
)
vigenereEncryptButton.pack()

# Decryption
def vigenereDecyrpt():
    vigenereEncrypted = vigenereInputTextbox.get()
    vigenereKey = vigenereKeyTextbox.get()
    decryptResult, decryptResultSpaced = vigenere_decrypt(vigenereEncrypted, vigenereKey)
    
    vigenereResultTextbox.delete(0, END)
    vigenereResultTextbox.insert(END, decryptResult)

    vigenereResultSpacedTextbox.delete(0, END)
    vigenereResultSpacedTextbox.insert(END, decryptResultSpaced)

vigenereDecyrptButton = Button(
    text="Decrypt",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = vigenereDecyrpt
)
vigenereDecyrptButton.pack()

# Result
vigenereResult = Label(
    text="Result"
)
vigenereResult.pack()

vigenereResultTextbox = Entry()
vigenereResultTextbox.pack()

virgenereResultSpaced = Label(
    text="Result (5-Character Spaced)"
)
virgenereResultSpaced.pack()

vigenereResultSpacedTextbox = Entry()
vigenereResultSpacedTextbox.pack()

# Write to file
def saveResultToFile():
    f = open("cypher_result.txt", "w")
    f.write(vigenereResultTextbox.get())
    f.close()

vigenereSaveButton = Button(
    text="Save",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = saveResultToFile
)
vigenereSaveButton.pack()

# Start the app
root.mainloop()