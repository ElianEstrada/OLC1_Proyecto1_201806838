from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, CENTER, SE, NW, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog, WORD
#from tkinter import Tk
from Sacanner_js import Scanner as js
from Scanner_css import Scanner as css
from Scanner_exp import ScannerExp
from Scanner_html import Scanner as html
from Parser_exp import Parser
import os

#########------------Functions for GUI---------------##########

fileInput = ""
rowCount = 1
columnCount = 1
string = ""
pathFileJs = ""

def new(): 
    txtInput.delete(1.0, END)

def openFile(): 
    global fileInput
    fileInput = filedialog.askopenfile(title = "Abrir Archivo")

    fileText = open(fileInput.name)
    text = fileText.read()

    txtInput.delete(1.0, END)
    txtInput.insert(INSERT, text)
    positionPush()
    fileText.close()

def exit():
    value = messagebox.askokcancel("Salir", "Está seguro que desea salir?")
    if value: 
        root.destroy()

def save_as(): 
    global fileInput

    save = filedialog.asksaveasfile(title = "Guardar Archivo")
    with open(save.name, "w+") as fileSave:
        fileSave.write(txtInput.get(1.0, END))
    fileInput = save.name

def save():
    global fileInput

    if fileInput == "": 
        save_as()
    else: 
        with open(fileInput.name, "w") as fileSave: 
            fileSave.write(txtInput.get(1.0, END))

def analize(): 
    global fileInput
    global string
    global pathFileJs

    pathName, fileExtension = os.path.splitext(fileInput.name)
    fileName = pathName.split("/")
    print(fileName[-1],fileExtension)
    if fileExtension == ".js": 
        print("Js")
        analizerJs = js()
        analizerJs.scannerJs(txtInput.get(1.0, END))
        pathFileJs = analizerJs.showTokens(fileName[-1])
        txtOutput.delete(1.0, END)
        txtOutput.insert(INSERT, analizerJs.showErrors())
    elif fileExtension == ".css":  
        print("css")
        analizerCss = css()
        analizerCss.scannerCss(txtInput.get(1.0, END))
        string = analizerCss.showTokens(fileName[-1])
        txtOutput.delete(1.0, END)
        txtOutput.insert(INSERT, analizerCss.showErrors())
    elif fileExtension == ".html": 
        print("html")
        analizerHtml = html()
        analizerHtml.scannerHtml(txtInput.get(1.0, END))
        print(analizerHtml.showTokens(fileName[-1]))
        txtOutput.delete(1.0, END)
        txtOutput.insert(INSERT, analizerHtml.showErrors())
    elif fileExtension == ".rmt": 
        print("rmt")
        count = 0
        row = 0
        htmlReport = "<html>\n\t<head>\n\t<title> Errors Sintácticos </title>\n\t"
        htmlReport += "<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css\">"
        htmlReport += "</head>\n<body bgcolor = \"#202020\" text = \"white\" class = \"container\">\n <h1> <center> Errores Lexicos </center> </h1>\n <div class = \"card z-depth-5\"><table border = \"1\" class = \"striped grey darken-4\">\n <tr>\n<th> No </th>\n"
        htmlReport += "<th> Fila </th>\n<th> Expresión </th>\n<th> Análisis </th>\n</tr>\n"

        analizerExp = ScannerExp()
        expresions = txtInput.get(1.0, END).split("\n")
        parser = Parser()
        for exp in expresions:
            count += 1
            result = parser.Start(analizerExp.scannerExp(exp))
            if result == []:
                row += 1
                htmlReport += f"<tr>\n<td> {count} </td>\n<td> {row} </td>\n<td> {exp} </td>\n<td> Correcto </td>\n</tr>\n"
                print("Correcto")
            elif result != None: 
                row += 1
                print("Incorrecto")
                htmlReport += f"<tr>\n<td> {count} </td>\n<td> {row} </td>\n<td> {exp} </td>\n<td> Incorrecto </td>\n</tr>\n"
            else: 
                row += 1

        htmlReport += "</div></table>\n</body>\n</html>"

        with open(f"..{pathFileJs}/AnalisisSintactico.html", "w+") as clearFile: 
            clearFile.write(htmlReport)

        print(parser)
    else: 
        messagebox.showwarning("Aclaración", "La extensión no cumple con ninguna de las definidas :'(")

def current_row(flag): 
    global rowCount
    if flag: 
        rowCount += 1
        lblRow2.config(text = rowCount)
    else: 
        rowCount -= 1
        lblRow2.config(text = rowCount)

def current_column(flag): 
    global columnCount
    if flag: 
        columnCount += 1
        lblColumn2.config(text = columnCount)
    else: 
        columnCount -= 1
        lblColumn2.config(text = columnCount)

def position(e): 
    if e.keysym == "Up": 
        current_row(False)
    elif e.keysym == "Down": 
        current_row(True)
    elif e.keysym == "Left": 
        current_column(False)
    elif e.keysym == "Right": 
        current_column(True)
    elif e.keysym == "Return": 
        current_row(True)

def positionPush(e = None): 
    global rowCount
    global columnCount
    #messagebox.showinfo("hola", e.keysym)

    positions = txtInput.index("current").split('.')
    lblRow2.config(text = positions[0])
    rowCount = int(positions[0])
    column = int(positions[1]) + 1
    columnCount = column
    lblColumn2.config(text = column)

def cssReport(): 
    txtOutput.delete(1.0, END)
    txtOutput.insert(INSERT, string)


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

lblRow2 = Label(myFrame, text= rowCount, fg="white", bg= "#0079cc")
lblRow2.grid(row = 0, column = 1)

##-------Label for column------##
lblColumn = Label(myFrame, text = "Column: ", fg = "white", bg = "#0079cc")
lblColumn.grid(row = 0, column = 3)

lblColumn2 = Label(myFrame, text= columnCount, fg="white", bg= "#0079cc")
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
btnAnalizer.config(font = ("Arial", 16), command = analize)
btnAnalizer.grid(row = 2, column = 1)

##-------Bar Menú------##
barMenu = Menu(root)

##-------File Menu------##
fileMenu = Menu(barMenu, tearoff = 0)
fileMenu.add_command(label = "Nuevo", command = new)
fileMenu.add_command(label = "Abrir", command = openFile)
fileMenu.add_command(label = "Guardar...", command = save)
fileMenu.add_command(label = "Guardar Como...", command= save_as)
fileMenu.add_separator()
fileMenu.add_command(label = "Salir", command = exit)
barMenu.add_cascade(label = "Archivos", menu= fileMenu)

##-------Reports Menu------##
reportMenu = Menu(barMenu, tearoff = 0)
reportMenu.add_command(label = "Reporte de Css", command = cssReport)
reportMenu.add_separator()
barMenu.add_cascade(label =  "Reportes", menu = reportMenu)

##-------Text Area for Input--------##
txtInput = scrolledtext.ScrolledText(myFrame2, wrap = WORD, width = 60, height = 30)
txtInput.focus()
txtInput.grid(row = 2, column = 0, pady = 24, padx= 20)
txtInput.bind("<Button>", positionPush)
txtInput.bind("<KeyRelease>", position)
##-------Text Area for Output--------##
txtOutput = scrolledtext.ScrolledText(myFrame2, wrap = WORD, width = 60, height = 30)
txtOutput.bind("<Key>", lambda a: "break")
txtOutput.grid(row = 2, column = 2, pady = 24, padx= 20)

root.config(menu = barMenu)

root.mainloop()