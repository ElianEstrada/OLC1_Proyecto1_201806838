from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog
#from tkinter import Tk
from Sacanner_js import Scanner as js
from Scanner_css import Scanner as css
from Scanner_html import Scanner as html



a = '''

<!--Este es el inicio del documento-->
<html>
<!--este es el fin del documento --> 

'''

analizadorhtml = html()

analizadorhtml.scannerHtml(a)
print(analizadorhtml.showTokens())
analizadorhtml.showErrors()

#contador = 0

#def contar(): 
 #   global contador
 #   contador += 1
  #  lblCount2.config(text= contador)

