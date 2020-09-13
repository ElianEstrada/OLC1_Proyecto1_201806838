from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog
from Sacanner_js import Scanner


a = '''


'''

analizadroJS = Scanner()

analizadroJS.scannerJs(a)
print(analizadroJS.showTokens())
analizadroJS.showErrors()

#contador = 0

#def contar(): 
 #   global contador
 #   contador += 1
  #  lblCount2.config(text= contador)

