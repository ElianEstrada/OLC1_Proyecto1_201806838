from tkinter import Tk, Menu, messagebox, filedialog, ttk, Label, scrolledtext, INSERT, END, Button, Scrollbar, RIGHT, Y, Frame, Canvas, HORIZONTAL, VERTICAL, simpledialog
#from tkinter import Tk
from Sacanner_js import Scanner as js
from Scanner_css import Scanner as css


a = '''

    html,body{
 ¬      margin:0;
        padding:0
    }
    /*
            Entrada archivo css
    */
    body{font: 76% ari*al,sans-serif; 
        background-image: url("/home/documents/picture.png");
        background: 0 0 0 0.20rem
    }
    p{ margin:0 10px 10px}
    a{
        display:block;
        color: #981793; $
        padding:10px;
    }
    div#header h1{
        height:80px;
        line-height:80px;
        12margin:0;
        padding-left:10px;
        background: #EEE;
        color: #79B30B;
    }


    div#content p{line-height:1.4}
    div#navigation{background:#B9CAFF}
    div#ex?tra{background:#FF8539}
    div#footer{
        background: #333;
        color: #FFF
    }
    div=footer p{
        margin:0;padding:5px 10px
    }

    div#wrapper{        float:left;width:100%       }
    div#content{margin: 0 25%}
    div#navigation{
        float:left;
        width:25%;
        margin-left:-100%
    }
    div#extra{
        float:left;/* :) */width:25%;
        margin-left:-25%
    }
    div#footer{
        clear:left;
        width:100%;
    }                   
    /*
    Errores lexicos en las lineas: 2,8,15,21,30,35,57,59,61
    */
    div>footer{
        clear:left;
        width:100% * 180 / 190.5px + 5;
    }
°
/* y acá :'(

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

