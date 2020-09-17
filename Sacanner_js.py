from Token_js import Token
from Token_js import TokenType
import re
import os
import platform 
from subprocess import call

pathFile = ""

class Scanner: 

    def __init__(self):
        self.output = []
        self.state = 0
        self.auxLex = ""
        self.row = 1
        self.column = 1
        self.flag = True
        self.flagId = True
        self.flagIdL = True
        self.flagIdD = True
        self.flagId_ = True
        self.flagDigit = True
        self.flagDigitD1 = True
        self.flagDigitD2 = True
        self.flagString = True
        self.flagStringC = True
        self.reservrdWords = [
            "var",
            "if",
            "else",
            "console", 
            "log",
            "for", 
            "while",
            "do", 
            "continue", 
            "return",
            "break", 
            "function",
            "constructor", 
            "this",
            "class",
            "math", 
            "pow"
        ]
        self.reports = "digraph G{\nrankdir = LR\nnode[shape = circle]\nS0\n"

    def scannerJs(self, inputStr):
        self.inputStr2 = inputStr
        inputStr += "#"
        self.output = []
        self.state = 0
        self.auxLex = ""
        self.row = 1
        self.column = 1
        self.i = 0

        while(self.i < len(inputStr)):
            
            c = inputStr[self.i]

            self.switch(self.state)(c)

            self.column += 1
            self.i += 1

    #simula un switch utilizando diccionarios
    def switch(self, state):
        return {
            0: self.state_0,
            1: self.state_1,
            2: self.state_2,
            3: self.state_3,
            5: self.state_5, 
            7: self.state_7, 
            9: self.state_9, 
            10: self.state_10,
            11: self.state_11, 
            12: self.state_12, 
            14: self.state_14, 
            16: self.state_16
        }.get(state)

    #########-----------------STATE 0-------------------##########
    #Recibe el caracter en la posición i
    def state_0(self, inputStr):
        if(inputStr == '('): 
            self.addToken(TokenType.PARENTESIS_ABRE, inputStr, self.row, self.column)
        elif(inputStr == ')'):
            self.addToken(TokenType.PARENTESIS_CIERRA, inputStr, self.row, self.column)
        elif(inputStr == '{'): 
            self.addToken(TokenType.LLAVES_ABRE, inputStr, self.row, self.column)
        elif(inputStr == '}'):
            self.addToken(TokenType.LLAVES_CIERRA, inputStr, self.row, self.column)
        elif(inputStr == '+'): 
            self.addToken(TokenType.SIG_MAS, inputStr, self.row, self.column)
        elif(inputStr == '-'): 
            self.addToken(TokenType.SIG_MENOS, inputStr, self.row, self.column)
        elif(inputStr == '*'): 
            self.addToken(TokenType.SIG_MULTIPLICACION, inputStr, self.row, self.column)
        elif(inputStr == '='): 
            self.addToken(TokenType.SIG_IGUAL, inputStr, self.row, self.column)
        elif(inputStr == '>'):
            self.addToken(TokenType.SIG_MAYOR_QUE, inputStr, self.row, self.column)
        elif(inputStr == '<'):
            self.addToken(TokenType.SIG_MENOR_QUE, inputStr, self.row, self.column)
        elif(inputStr == '!'): 
            self.addToken(TokenType.SIG_NEGACION, inputStr, self.row, self.column)
        elif(inputStr == '&'): 
            self.auxLex += inputStr
            self.state = 14
        elif(inputStr == '|'): 
            self.auxLex += inputStr
            self.state = 16
        elif(inputStr == ';'): 
            self.addToken(TokenType.SIG_PUNTO_COMA, inputStr, self.row, self.column)
        elif(inputStr == ':'):
            self.addToken(TokenType.SIG_DOS_PUTNOS , inputStr, self.row, self.column)
        elif(inputStr == ','):
            self.addToken(TokenType.SIG_COMA, inputStr, self.row, self.column)
        elif(inputStr == '.'):
            self.addToken(TokenType.SIG_PUNTO, inputStr, self.row, self.column)
        elif(inputStr == '`'): 
            self.addToken(TokenType.SIG_ACENTO_GRAVE, inputStr, self.row, self.column)
        elif(inputStr == '\n'): 
            self.row += 1
            self.column = 1
            self.output.append("\n")
        elif(inputStr == '\t'): 
            self.column += 8
            self.output.append("\t")
        elif(inputStr == ' '):
            #self.column += 1
            self.output.append(" ")
        elif(inputStr == '/'):
            self.auxLex += inputStr
            self.state = 9
        elif(inputStr == '"'):
            self.auxLex += inputStr
            self.state = 5
            if self.flagString: 
                self.reports += "S0->S5 [label = \"\\\"\"]\n"
        elif(inputStr == '\''):
            self.auxLex += inputStr 
            self.state = 7
        elif(re.match("[A-Za-z_ñ]", inputStr)):
            self.auxLex += inputStr
            self.state = 1
            if self.flagId: 
                self.reports += "node[shape = doublecircle]\nS1\nS0->S1[label = L]\n"
        elif(inputStr.isdigit()):
            self.flag = True
            self.auxLex += inputStr
            self.state = 2
            if self.flagDigit: 
                self.reports += "node[shape = doublecircle]\nS2\nS0->S2[label = D]\n"
        else: 
            if(inputStr == '#' and self.i == len(self.inputStr2)): 
                print("Analysis Finished")
            else: 
                self.addToken(TokenType.DESCONOCIDO, inputStr, self.row, self.column)
                self.auxLex = ""

    #########-----------------STATE 1-------------------#########
    def state_1(self, inputStr):
        flag = True
        if(not re.match("[A-Za-z_0-9ñ]", inputStr)):
            for words in self.reservrdWords:
                if self.auxLex.lower() == words: 
                    self.addToken(TokenType.PALABRA_RESERVADA, self.auxLex, self.row, self.column - 1)
                    flag = False
                    break 
            
            if flag: 
                self.addToken(TokenType.IDENTIFICADORES, self.auxLex, self.row, self.column - 1)
            self.auxLex = ""
            self.state = 0
            self.i -= 1
            self.column -= 1
            if self.flagId: 
                self.reports += "}"
                print(self.reports)
                path = ""
                system = platform.system()
                print(system)
                if system == "Linux": 
                    path = self.output[2].getLexeme().split(':')
                elif system == "Windows": 
                    path = self.output[0].getLexeme().split(':')
                global pathFile 

                splitPath = path[1].lower().split("output")
                pathFile = "/output" + splitPath[1]
                os.makedirs(f"..{pathFile}", exist_ok = True)
                with open(f"..{pathFile}/ERID.dot", 'w+') as report:
                    report.write(self.reports)
                #self.reports.Dot().write_png("graph.png", prog = "dot")
                call(["dot", "-Tpdf", f"..{pathFile}/ERID.dot", "-o", f"..{pathFile}/ERID.pdf"])
            self.flagId = False
            self.reports = "digraph G{\nrankdir = LR\nnode[shape = circle]\nS0\n"
            return
        
        if re.match("[A-Za-z]", inputStr) and self.flagIdL: 
            self.reports += "S1->S1 [label = L]\n"
            self.flagIdL = False
        elif re.match("[0-9]", inputStr) and self.flagIdD:
            self.reports += "S1->S1 [label = D]\n"
            self.flagIdD = False
        elif re.match("_", inputStr) and self.flagId_: 
            self.reports += "S1->S1 [label = _]\n"
            self.flagId_ = False
        self.auxLex += inputStr

    #########-----------------STATE 2 and 4-------------------#########
    def state_2(self, inputStr): 
        if(inputStr == '.' and self.flag):
            self.state = 3
            self.auxLex += inputStr
            if self.flagDigit:  
                self.reports += "node[shape = circle]\nS3\nS2->S3 [label = \".\"]\n"
        elif(inputStr.isdigit()):
            self.auxLex += inputStr
            if self.flagDigitD1 and self.flag:  
                self.reports += "S2->S2 [label = D]\n"
                self.flagDigitD1 = False
            elif self.flagDigitD2: 
                self.reports += "S4->S4 [label = D]\n"
                self.flagDigitD2 = False

        else: 
            global pathFile
            self.addToken(TokenType.NUMERO, self.auxLex, self.row, self.column - 1)
            self.auxLex = ""
            self.state = 0
            self.i -= 1
            self.column -= 1
            self.flag = False
            if self.flagDigit:
                self.reports += "}" 

                if pathFile == "": 
                    path = ""
                    system = platform.system()
                    print(system)
                    if system == "Linux": 
                        path = self.output[2].getLexeme().split(':')
                    elif system == "Windows": 
                        path = self.output[0].getLexeme().split(':')
                

                    splitPath = path[1].lower().split("output")
                    pathFile = "/output" + splitPath[1]
                    os.makedirs(f"..{pathFile}", exist_ok = True)

                with open(f"..{pathFile}/ERNum.dot", 'w+') as report:
                    report.write(self.reports)
                #self.reports.Dot().write_png("graph.png", prog = "dot")
                call(["dot", "-Tpdf", f"..{pathFile}/ERNum.dot", "-o", f"..{pathFile}/ERNum.pdf"])
            self.flagDigit = False
            self.reports = "digraph G{\nrankdir = LR\nnode[shape = circle]\nS0\n"


    #########-----------------STATE 3-------------------#########
    def state_3(self, inputStr): 
        if(inputStr.isdigit()): 
            self.state = 2
            self.flag = False
            self.i -= 1
            self.column -= 1
            if self.flagDigit: 
                self.reports += "node[shape = doublecircle]\nS4\nS3->S4 [label = D]"
        else: 
            self.addToken(TokenType.DESCONOCIDO, self.auxLex, self.row, self.column - 1)
            self.auxLex = ""
            self.state = 0
            self.i -= 1
            self.column -= 1
            self.reports = "digraph G{\nrankdir = LR\nnode[shape = circle]\nS0\n"

    #########-----------------STATE 5 and 6-------------------#########
    def state_5(self, inputStr): 
        if inputStr == '"': 
            self.auxLex += inputStr
            self.addToken(TokenType.CADENA_TEXTO, self.auxLex, self.row, self.column -1)
            self.state = 0
            self.auxLex = ""
            global pathFile
            if self.flagString:
                self.reports += "node[shape = doublecircle]\nS6\nS5->S6 [label = \"\\\"\"]\n}"

                if pathFile == "": 
                    path = ""
                    system = platform.system()
                    print(system)
                    if system == "Linux": 
                        path = self.output[2].getLexeme().split(':')
                    elif system == "Windows": 
                        path = self.output[0].getLexeme().split(':')
                

                    splitPath = path[1].lower().split("output")
                    pathFile = "/output" + splitPath[1]
                    os.makedirs(f"..{pathFile}", exist_ok = True)

                with open(f"..{pathFile}/ERText.dot", 'w+') as report:
                    report.write(self.reports)
                #self.reports.Dot().write_png("graph.png", prog = "dot")
                call(["dot", "-Tpdf", f"..{pathFile}/ERText.dot", "-o", f"..{pathFile}/ERText.pdf"])
            self.flagString = False
            self.reports = "digraph G{\nrankdir = LR\nnode[shape = circle]\nS0\n"

        elif inputStr == "\n": 
            self.addToken(TokenType.DESCONOCIDO, self.auxLex, self.row, self.column -1)
            self.state = 0
            self.auxLex = ""
            self.i -= 1
            self.column -= 1
            self.reports = "digraph G{\nrankdir = LR\nnode[shape = circle]\nS0\n"

        else: 
            self.auxLex += inputStr
            if self.flagStringC: 
                self.reports += "S5->S5 [label = \"L|D|S\"]\n"
                self.flagStringC = False

    #########-----------------STATE 7 and 8-------------------#########
    def state_7(self, inputStr):
        if inputStr == '\'': 
            self.auxLex += inputStr
            self.addToken(TokenType.CADENA_TEXTO, self.auxLex, self.row, self.column-1)
            self.auxLex = ""
            self.state = 0
        elif inputStr == "\n": 
            self.addToken(TokenType.DESCONOCIDO, self.auxLex, self.row, self.column-1)
            self.state = 0
            self.auxLex = ""
            self.i -= 1
            self.column -= 1
        else: 
            self.auxLex += inputStr

    #########-----------------STATE 9-------------------#########
    def state_9(self, inputStr): 
        if inputStr == "/": 
            self.auxLex += inputStr
            self.state = 10
        elif inputStr == "*": 
            self.auxLex += inputStr
            self.state = 11
        else: 
            self.addToken(TokenType.SIG_DIVIDIDO, self.auxLex, self.row, self. column -1)
            self.state = 0
            self.auxLex = ""
            self.i -= 1
            self.column -= 1
    
    #########-----------------STATE 10-------------------#########
    def state_10(self, inputStr): 
        if inputStr == "\n": 
            self.addToken(TokenType.COMENTARIO_UNLINE, self.auxLex, self.row, self.column - 1)
            self.auxLex = ""
            self.state = 0
            self.i -= 1
            self.column -= 1
        else: 
            self.auxLex += inputStr

    #########-----------------STATE 11-------------------#########
    def state_11(self, inputStr):
        if inputStr != "*":
            if inputStr == "\n": 
                self.row += 1
                self.column = 1
            self.auxLex += inputStr

        else: 
            self.auxLex += inputStr
            self.state = 12
    
    #########-----------------STATE 12 and 13-------------------#########
    def state_12(self, inputStr): 
        if inputStr != "/": 
            self.state = 11
            self.i -= 1
            self.column -= 1
        else: 
            self.auxLex += inputStr
            self.addToken(TokenType.COMENTARIO_MULTILINEA, self.auxLex, self.row, self.column - 1)
            self.auxLex = ""
            self.state = 0

    #########-----------------STATE 14 and 15-------------------#########
    def state_14(self, inputStr):
        if inputStr != "&": 
            self.addToken(TokenType.DESCONOCIDO, self.auxLex, self.row, self.column - 1)
            self.auxLex = ""
            self.state = 0
            self.i -= 1
            self.column -= 1
        else: 
            self.auxLex += inputStr
            self.addToken(TokenType.SIG_AND, self.auxLex, self.row, self.column - 1)
            self.state = 0
            self.auxLex = ""

    #########-----------------STATE 16 and 17-------------------#########
    def state_16(self, inputStr): 
        if inputStr != "|": 
            self.addToken(TokenType.DESCONOCIDO, self.auxLex, self.row, self.column - 1)
            self.auxLex = ""
            self.state = 0
            self.i -= 1
            self.column -= 1
        else: 
            self.auxLex += inputStr
            self.addToken(TokenType.SIG_OR, self.auxLex, self.row, self.column - 1)
            self.state = 0
            self.auxLex = ""

    ###Método para agregar los tokens a la lista
    def addToken(self, tokenType, lexeme, row, column):
        self.output.append(Token(tokenType, lexeme, row, column))

    ###Método para mostrar la lista de tokens
    def showTokens(self, fileName):
        cadena = ""
        for tokens in self.output:
            if(tokens == "\n"): 
                cadena += "\n"
            elif(tokens == "\t"): 
                cadena += "\t"
            elif(tokens == " "):
                    cadena += " "
            elif not tokens.getTokenType() == "DESCONOCIDO":          
                cadena += tokens.getLexeme()
                global pathFile

                with open(f"..{pathFile}/{fileName}.js", "w") as clearFile: 
                    clearFile.write(cadena)

                print(f"Lexeme: {tokens.getLexeme()}; TokenType: {tokens.getTokenType()}; row: {tokens.getRow()}; column: {tokens.getColumn()}")

        return pathFile

    ###Método para mostrar los errores lexicos
    def showErrors(self): 
        count = 0
        outErrors = ""
        htmlReport = "<html>\n\t<head>\n\t<title> Errors Lexicos de Js </title>\n\t"
        htmlReport += "<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css\">"
        htmlReport += "</head>\n<body bgcolor = \"#202020\" text = \"white\" class = \"container\">\n <h1> <center> Errores Lexicos </center> </h1>\n <div class = \"card z-depth-5\"><table border = \"1\" class = \"striped grey darken-4\">\n <tr>\n<th> No </th>\n"
        htmlReport += "<th> Fila </th>\n <th> Columna </th>\n<th> Lexema </th>\n<th> Tipo de Token </th>\n</tr>\n"
        for tokens in self.output:
            if(tokens == "\n" or tokens == "\t" or tokens == " "):
                continue
            elif(tokens.getTokenType() == "DESCONOCIDO"):
                count += 1
                htmlReport += f"<tr>\n<td> {count} </td>\n<td> {tokens.getRow()} </td>\n<td> {tokens.getColumn()} </td>\n<td> {tokens.getLexeme()} </td>\n<td> {tokens.getTokenType()} </td>\n</tr>\n"
                outErrors +=  f"Lexeme: {tokens.getLexeme()}; TokenType: {tokens.getTokenType()}; row: {tokens.getRow()}; column: {tokens.getColumn()}\n"
        htmlReport += "</div></table>\n</body>\n</html>"

        global pathFile

        with open(f"..{pathFile}/ErroresLexicosJs.html", "w+") as clearFile: 
            clearFile.write(htmlReport)

        if outErrors == "": 
            return "there are not lexical erros" 
        else: 
            return outErrors
                    