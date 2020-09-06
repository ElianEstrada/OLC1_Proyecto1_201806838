from Sacanner_js import Scanner

a = "\t _a5@\n 5 @ $)"


analizadroJS = Scanner()

analizadroJS.scannerJs(a)
print(analizadroJS.showTokens())
analizadroJS.showErrors()




