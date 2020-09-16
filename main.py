from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog
#from tkinter import Tk
from Sacanner_js import Scanner as js
from Scanner_css import Scanner as css


a = '''

/******esto es un 
comentario multi
linea perros :v 
@ para que lo sepan :v*
******************/
'''

analizadorCss = css()

analizadorCss.scannerCss(a)
print(analizadorCss.showTokens())
analizadorCss.showErrors()

#contador = 0

#def contar(): 
 #   global contador
 #   contador += 1
  #  lblCount2.config(text= contador)

