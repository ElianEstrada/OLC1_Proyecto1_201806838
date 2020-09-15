from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog
#from tkinter import Tk
from Sacanner_js import Scanner


a = '''


class_02 MiClase02 {

    this.name = "Elian";
    this.ege = 20;

    if (ege == 20){
        console.log (this.name + " tu edad es de: " + this.ege);
    }
    else {
        console.log ("no tienes la edad suficiente");
    }

    Function myFunction(a, b, c){
        console.Log("esta es mi funcion");
        flag = true
        while(flag){
            if this.ege == 10{
                flag = false
            }
        }

    }

}

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

