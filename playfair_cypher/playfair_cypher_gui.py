from tkinter import *
import tkinter.filedialog as filedialog

from playfair_cypher.playfair_cypher import *

root = Tk()
root.title("Kriptografi, Tucil 1")
root.geometry("600x600")

playfairTitle = Label(
    text="Playfair Cypher"
)
playfairTitle.pack()

def returnHome():
    root.destroy()
    import main 

playfairBackButton = Button(
    text="Back",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = returnHome
)
playfairBackButton.pack()


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
    playfairInputTextbox.delete(0, END)
    playfairInputTextbox.insert(END, cypherData)

playfairLoadButton = Button(
    text="Load",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = loadResultFromFile
)
playfairLoadButton.pack()

# Viginere Row

# playfair - Text
playfairLabel = Label(
    text="Enter Text"
)
playfairLabel.pack()

playfairInputTextbox = Entry()
playfairInputTextbox.pack()

# playfair Key 

playfairKeyLabel = Label(
    text="Enter Key"
)
playfairKeyLabel.pack()

playfairKeyTextbox = Entry()
playfairKeyTextbox.pack()

def playfairEncyrpt():
    playfairInput = playfairInputTextbox.get()
    playfairKey = playfairKeyTextbox.get()
    encryptResult, encryptResultSpaced = playfair_encrypt(playfairInput, playfairKey)

    playfairResultTextbox.delete(0, END)
    playfairResultTextbox.insert(END, encryptResult)

    playfairResultSpacedTextbox.delete(0, END)
    playfairResultSpacedTextbox.insert(END, encryptResultSpaced)

playfairEncryptButton = Button(
    text="Encrypt",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = playfairEncyrpt
)
playfairEncryptButton.pack()

# Decryption
def playfairDecyrpt():
    playfairEncrypted = playfairInputTextbox.get()
    playfairKey = playfairKeyTextbox.get()
    decryptResult, decryptResultSpaced = playfair_decrypt(playfairEncrypted, playfairKey)
    
    playfairResultTextbox.delete(0, END)
    playfairResultTextbox.insert(END, decryptResult)

    playfairResultSpacedTextbox.delete(0, END)
    playfairResultSpacedTextbox.insert(END, decryptResultSpaced)

playfairDecyrptButton = Button(
    text="Decrypt",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = playfairDecyrpt
)
playfairDecyrptButton.pack()

# Result
playfairResult = Label(
    text="Result"
)
playfairResult.pack()

playfairResultTextbox = Entry()
playfairResultTextbox.pack()

virgenereResultSpaced = Label(
    text="Result (5-Character Spaced)"
)
virgenereResultSpaced.pack()

playfairResultSpacedTextbox = Entry()
playfairResultSpacedTextbox.pack()

# Write to file
def saveResultToFile():
    f = open("cypher_result.txt", "w")
    f.write(playfairResultTextbox.get())
    f.close()

playfairSaveButton = Button(
    text="Save",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
    command = saveResultToFile
)
playfairSaveButton.pack()