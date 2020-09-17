from Token_css import Token
from Token_css import TokenType
import re
import platform 
import os
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
        self.reservrdWords = [
            "color",
            "border", 
            "text-align",
            "font-weight", 
            "padding-left", 
            "padding-top", 
            "line-height", 
            "margin-top", 
            "margin-left", 
            "display", 
            "top", 
            "float", 
            "min-width", 
            "background-color", 
            "Opacity", 
            "font-family", 
            "font-size", 
            "padding-right", 
            "padding", 
            "width", 
            "margin-right", 
            "margin", 
            "position", 
            "right", 
            "clear",
            "max-height", 
            "background-image", 
            "background", 
            "font-style", 
            "font", 
            "padding-bottom", 
            "height", 
            "margin-bottom", 
            "border-style", 
            "bottom", 
            "left", 
            "max-width", 
            "min-height", 
            "px", 
            "em", 
            "relative", 
            "inline-block", 
            "rgba", 
            "url", 
            "content", 
            "inherit", 
            "solid", 
            "absolute", 
            "rem"
        ]
        self.reports = ""

    def scannerCss(self, inputStr):
        self.inputStr2 = inputStr
        inputStr += "$"
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
            8: self.state_8,
            9: self.state_9
        }.get(state)

    #########-----------------STATE 0-------------------##########
    #Recibe el caracter en la posición i
    def state_0(self, inputStr):
        if(inputStr == '('):
            self.reports += f"S0; S0; {inputStr}\n" 
            self.addToken(TokenType.PARENTESIS_ABRE, inputStr, self.row, self.column)
        elif(inputStr == ')'):
            self.reports += f"S0; S0; {inputStr}\n"
            self.addToken(TokenType.PARENTESIS_CIERRA, inputStr, self.row, self.column)
        elif(inputStr == '{'): 
            self.reports += f"S0; S0; {inputStr}\n"
            self.addToken(TokenType.LLAVES_ABRE, inputStr, self.row, self.column)
        elif(inputStr == '}'):
            self.reports += f"S0; S0; {inputStr}\n"
            self.addToken(TokenType.LLAVES_CIERRA, inputStr, self.row, self.column)
        elif(inputStr == '-'): 
            self.reports += f"S0; S0; {inputStr}\n"
            self.addToken(TokenType.SIG_MENOS, inputStr, self.row, self.column)
        elif(inputStr == '*'): 
            self.reports += f"S0; S0; {inputStr}\n"
            self.addToken(TokenType.OP_UNIVERSAL, inputStr, self.row, self.column)
        elif(inputStr == ';'): 
            self.reports += f"S0; S0; {inputStr}\n"
            self.addToken(TokenType.SIG_PUNTO_COMA, inputStr, self.row, self.column)
        elif(inputStr == ':'):
            self.reports += f"S0; S0; {inputStr}\n"
            self.addToken(TokenType.SIG_DOS_PUTNOS , inputStr, self.row, self.column)
        elif(inputStr == ','):
            self.reports += f"S0; S0; {inputStr}\n"
            self.addToken(TokenType.SIG_COMA, inputStr, self.row, self.column)
        elif(inputStr == '.'):
            self.reports += f"S0; S0; {inputStr}\n"
            self.addToken(TokenType.SIG_PUNTO, inputStr, self.row, self.column)
        elif(inputStr == "#"): 
            self.reports += f"S0; S0; {inputStr}\n"
            self.addToken(TokenType.SIG_NUMERAL, inputStr, self.row, self.column)
        elif(inputStr == "%"): 
            self.reports += f"S0; S0; {inputStr}\n"
            self.addToken(TokenType.SIG_PORCENTAJE, inputStr, self.row, self.column)
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
            self.reports += f"S0; S7; {inputStr}\n"
            self.auxLex += inputStr
            self.flag = True
            self.state = 7
        elif(inputStr == '"'):
            self.reports += f"S0; S5; {inputStr}\n"
            self.auxLex += inputStr
            self.state = 5
        elif(re.match("[A-Za-z-ñ]", inputStr)):
            self.reports += f"S0; S1; {inputStr}\n"
            self.auxLex += inputStr
            self.state = 1
        elif(inputStr.isdigit()):
            self.flag = True
            self.reports += f"S0; S2; {inputStr}\n"
            self.auxLex += inputStr
            self.state = 2
        else: 
            if(inputStr == '$' and self.i == len(self.inputStr2)): 
                print("Analysis Finished")
                print(self.reports)
            else: 
                self.addToken(TokenType.DESCONOCIDO, inputStr, self.row, self.column)
                self.auxLex = ""

    #########-----------------STATE 1-------------------#########
    def state_1(self, inputStr):
        flag = True
        if(not re.match("[A-Za-z-0-9ñ]", inputStr)):
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
            return
        self.reports += f"S1; S1; {inputStr}\n"
        self.auxLex += inputStr

    #########-----------------STATE 2 and 4-------------------#########
    def state_2(self, inputStr): 
        if(inputStr == '.' and self.flag):
            self.state = 3
            self.reports += f"S2; S3; {inputStr}\n"
            self.auxLex += inputStr
        elif(inputStr.isdigit()):
            self.auxLex += inputStr
            if self.flag: 
                self.reports += f"S2; S2; {inputStr}\n"
            else: 
                self.reports += f"S4; S4; {inputStr}\n"
        else: 
            self.addToken(TokenType.NUMERO, self.auxLex, self.row, self.column - 1)
            self.auxLex = ""
            self.state = 0
            self.i -= 1
            self.column -= 1
            self.flag = False

    #########-----------------STATE 3-------------------#########
    def state_3(self, inputStr): 
        if(inputStr.isdigit()): 
            self.state = 2
            self.reports += f"S3; S4; {inputStr}\n"
            self.auxLex += inputStr
            self.flag = False
        else: 
            self.addToken(TokenType.DESCONOCIDO, self.auxLex, self.row, self.column - 1)
            self.auxLex = ""
            self.state = 0
            self.i -= 1
            self.column -= 1

    #########-----------------STATE 5 and 6-------------------#########
    def state_5(self, inputStr): 
        if inputStr == '"': 
            self.auxLex += inputStr
            self.reports += f"S5, S6, {inputStr}\n"
            self.addToken(TokenType.CADENA_TEXTO, self.auxLex, self.row, self.column -1)
            self.state = 0
            self.auxLex = ""
        elif inputStr == "\n": 
            self.addToken(TokenType.DESCONOCIDO, self.auxLex, self.row, self.column -1)
            self.state = 0
            self.auxLex = ""
            self.i -= 1
            self.column -= 1
        else: 
            self.reports += f"S5, S5, {inputStr}\n"
            self.auxLex += inputStr

    #########-----------------STATE 7-------------------#########
    def state_7(self, inputStr): 
        if inputStr == "*": 
            self.auxLex += inputStr
            self.reports += f"S7, S8, {inputStr}\n"
            self.state = 8
        else: 
            self.addToken(TokenType.DESCONOCIDO, self.auxLex, self.row, self. column -1)
            self.state = 0
            self.auxLex = ""
            self.i -= 1
            self.column -= 1

    #########-----------------STATE 8-------------------#########
    def state_8(self, inputStr):
        if inputStr != "*":
            if inputStr == "\n": 
                self.row += 1
                self.column = 1
            if inputStr == "$" and self.i == len(self.inputStr2): 
                self.addToken(TokenType.DESCONOCIDO, self.auxLex, self.row, self. column -1)
                self.state = 0
                self.auxLex = ""
                self.i -= 1
                self.column -= 1
            self.auxLex += inputStr
            if self.flag: 
                self.reports += f"S8, S8, {inputStr}\n"
            else: 
                self.reports += f"S9, S8, {inputStr}\n"
                self.flag = True
        else: 
            self.auxLex += inputStr
            self.reports += f"S8, S9, {inputStr}\n"
            self.state = 9
    
    #########-----------------STATE 9 and 10-------------------#########
    def state_9(self, inputStr): 
        if inputStr != "/": 
            self.state = 8
            self.flag = False
            self.i -= 1
            self.column -= 1
        else: 
            self.auxLex += inputStr
            self.reports += f"S9, S10, {inputStr}\n"
            self.addToken(TokenType.COMENTARIO_MULTILINEA, self.auxLex, self.row, self.column - 1)
            self.auxLex = ""
            self.state = 0

    ###Método para agregar los tokens a la lista
    def addToken(self, tokenType, lexeme, row, column):
        self.output.append(Token(tokenType, lexeme, row, column))

    ###Método para mostrar la lista de tokens
    def showTokens(self, fileName):
        cadena = ""
        path = ""
        system = platform.system()
        print(system)
        if system == "Linux": 
            path = self.output[2].getLexeme().split(':')
        elif system == "Windows": 
            path = self.output[0].getLexeme().split(':')
        global pathFile 

        splitPath = path[1].lower().split("output")
        moreSplitPath = splitPath[1].split('*')
        pathFile = "/output" + moreSplitPath[0]
        os.makedirs(f"..{pathFile}", exist_ok = True)

        for tokens in self.output:
            if(tokens == "\n"): 
                cadena += "\n"
            elif(tokens == "\t"): 
                cadena += "\t"
            elif(tokens == " "):
                    cadena += " "
            elif not tokens.getTokenType() == "DESCONOCIDO":          
                cadena += tokens.getLexeme()
                print(f"Lexeme: {tokens.getLexeme()}; TokenType: {tokens.getTokenType()}; row: {tokens.getRow()}; column: {tokens.getColumn()}")

        with open(f"..{pathFile}/{fileName}.css", "w") as clearFile: 
            clearFile.write(cadena)

        return self.reports

    ###Método para mostrar los errores lexicos
    def showErrors(self): 
        count = 0
        outErrors = ""
        htmlReport = "<html>\n\t<head>\n\t<title> Errors Lexicos de Css </title>\n\t"
        htmlReport += "<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css\">"
        htmlReport += "</head>\n<body bgcolor = \"#202020\" text = \"white\" class = \"container\">\n <h1> <center> Errores Lexicos </center> </h1>\n <div class = \"card z-depth-5\"><table border = \"1\" class = \"striped grey darken-4\">\n <tr>\n<th> No </th>\n"
        htmlReport += "<th> Fila </th>\n <th> Columna </th>\n<th> Lexema </th>\n<th> Tipo de Token </th>\n</tr>\n"
        for tokens in self.output:
            if(tokens == "\n" or tokens == "\t" or tokens == " "):
                continue
            elif(tokens.getTokenType() == "DESCONOCIDO"):
                count += 1
                htmlReport += f"<tr>\n<td> {count} </td>\n<td> {tokens.getRow()} </td>\n<td> {tokens.getColumn()} </td>\n<td> {tokens.getLexeme()} </td>\n<td> {tokens.getTokenType()} </td>\n</tr>\n"
                outErrors += f"Lexeme: {tokens.getLexeme()}; TokenType: {tokens.getTokenType()}; row: {tokens.getRow()}; column: {tokens.getColumn()}\n"
        htmlReport += "</div></table>\n</body>\n</html>"
        with open(f"..{pathFile}/ErroresLexicosCss.html", "w+") as clearFile: 
            clearFile.write(htmlReport)

        if outErrors == "": 
            return "No hay errores lexicos"
        else: 
            return outErrors