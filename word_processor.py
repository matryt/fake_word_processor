from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import showerror


filename = None


def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)


def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, "w")
    f.write(t)
    f.close()


def saveAs():
    f = asksaveasfile(defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except Exception:
        showerror(title="Oh no!", message="Unable to save file...")


root = Tk()


def openFile():
    global filename
    file = askopenfile(parent=root, title="Select a File")
    filename = file.name
    t = file.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    file.close()


fname = 'second'


numlines = 0
numwords = 0
numchars = 0
numparagraph = 0


with open(fname, 'rb+') as k:
    for line in k.readlines():
        if line in ('\n', '\r\n'):
            if numlines == 0:
                numparagraph = numparagraph + 1
            numlines = numlines + 1
        else:
            numlines = 0
        words = line.split()
        numlines += 1
        numwords += len(words)
        numchars += len(line)


def printWordCount():
    print(numwords)


def printCharCount():
    print(numchars)


def printParaCount():
    print(numparagraph)


def printLineCount():
    print(numlines)


root.title("Text Editor")


root.minsize(width=800, height=600)
root.maxsize(width=1920, height=1080)

text = Text(root, width=500, height=600, bg="white", fg="black")
text.pack()

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menu.add_cascade(label="File", menu=filemenu)


toolbar = Menu(menu)
toolbar.add_command(label="Word Count", command=printWordCount)
toolbar.add_command(label="Character Count", command=printCharCount)
toolbar.add_command(label="Paragraph Count", command=printParaCount)
toolbar.add_command(label="Line Count", command=printLineCount)
menu.add_cascade(label="Tools", menu=toolbar)


root.mainloop()
