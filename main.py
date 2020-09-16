from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, CENTER, SE, NW, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog, WORD
#from tkinter import Tk
from Sacanner_js import Scanner as js
from Scanner_css import Scanner as css
from Scanner_exp import ScannerExp
from Scanner_html import Scanner as html
from Parser_exp import Parser

#########------------Functions for GUI---------------##########

fileInput = ""

def new(): 
    txtInput.delete(1.0, END)

def open(): 
    global fileInput
    fileInput = filedialog.askopenfile(title = "Abrir Archivo")
    print(fileInput)


#########------------GUI---------------##########

##-------root of windows------##
root = Tk()
root.title("LABORATORIO")

##-------Bottom Frame------##
myFrame = Frame()
myFrame.pack(side = "bottom", fill = "x")
myFrame.config(bg = "#0079cc", width = "920", height = "20")

##-------Label for row------##
lblRow = Label(myFrame, text = "Row: ", fg = "white", bg = "#0079cc")
lblRow.grid(row = 0, column = 0)

lblRow2 = Label(myFrame, text= "0", fg="white", bg= "#0079cc")
lblRow2.grid(row = 0, column = 1)

##-------Label for column------##
lblColumn = Label(myFrame, text = "Column: ", fg = "white", bg = "#0079cc")
lblColumn.grid(row = 0, column = 3)

lblColumn2 = Label(myFrame, text= "0", fg="white", bg= "#0079cc")
lblColumn2.grid(row = 0, column = 4)

##-------Main Frame------##
myFrame2 = Frame()
myFrame2.pack(fill = "both", expand = "yes")
myFrame2.config(bg = "#202020", width = "920", height = "550")

##-------Label for Title------##
lblTitle = Label(myFrame2, text = "ML WEB EDITOR", fg = "white", bg = "#202020")
lblTitle.config(font = ("Arial", 24))
lblTitle.grid(row = 0, column = 1)
#lblTitle.pack(anchor = CENTER)

##-------Label of Input------##
lblInput = Label(myFrame2, text = "ENTRADA", fg = "white", bg = "#202020")
lblInput.config(font = ("Arial", 14))
lblInput.grid(row = 1, column = 0)

##-------Label of Output------##
lblOutput = Label(myFrame2, text = "SALIDA", fg = "white", bg= "#202020")
lblOutput.config(font = ("Arial", 14))
lblOutput.grid(row = 1, column = 2)

##-------Button for Analizer------##
btnAnalizer = Button(myFrame2, text = "Analizar", fg = "white", bg = "#0079cc", width = "15", height = "1")
btnAnalizer.config(font = ("Arial", 16))
btnAnalizer.grid(row = 2, column = 1)

##-------Bar Menú------##
barMenu = Menu(root)

##-------File Menu------##
fileMenu = Menu(barMenu, tearoff = 0)
fileMenu.add_command(label = "Nuevo", command = new)
fileMenu.add_command(label = "Abrir", command = open)
fileMenu.add_separator()
fileMenu.add_command(label = "Salir", command = root.quit)
barMenu.add_cascade(label = "Archivos", menu= fileMenu)

##-------Reports Menu------##
reportMenu = Menu(barMenu, tearoff = 0)
reportMenu.add_separator()
barMenu.add_cascade(label =  "Reportes", menu = reportMenu)

##-------Text Area for Input--------##
txtInput = scrolledtext.ScrolledText(myFrame2, wrap = WORD, width = 50, height = 30)
txtInput.focus()
txtInput.grid(row = 2, column = 0)
##-------Text Area for Output--------##
txtOutput = scrolledtext.ScrolledText(myFrame2, wrap = WORD, width = 50, height = 30, state= "disabled")
txtOutput.grid(row = 2, column = 2)

root.config(menu = barMenu)

root.mainloop()