from Token_html import Token
from Token_html import TokenType
import re
from subprocess import call


class Scanner: 

    def __init__(self):
        self.output = []
        self.state = 0
        self.auxLex = ""
        self.row = 1
        self.column = 1
        self.flag = True
        self.reservrdWords = [
            "html", 
            "head",
            "body", 
            "title", 
            "h1", 
            "h2", 
            "h3", 
            "h4", 
            "h5", 
            "h6",
            "p",
            "img", 
            "src",
            "br", 
            "a", 
            "href",
            "ul",
            "li", 
            "ol", 
            "style", 
            "table", 
            "border", 
            "caption", 
            "tr"
            "th",
            "td", 
            "colgroup", 
            "col", 
            "thead", 
            "tbody",
            "tfoot" 
        ]
        self.reports = ""

    def scannerHtml(self, inputStr):
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
            4: self.state_4,
            5: self.state_5, 
            6: self.state_6,
            7: self.state_7, 
            8: self.state_8,
            9: self.state_9, 
            11: self.state_11,
            12: self.state_12
        }.get(state)

    #########-----------------STATE 0-------------------##########
    #Recibe el caracter en la posición i
    def state_0(self, inputStr):
        if(inputStr == '/'): 
            self.addToken(TokenType.SIG_DIVISION, inputStr, self.row, self.column)
        elif(inputStr == '='):
            self.addToken(TokenType.SIG_IGUAL , inputStr, self.row, self.column)
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
        elif(inputStr == '<'):
            self.auxLex += inputStr
            self.state = 4
        elif(inputStr == '>'): 
            self.auxLex += inputStr
            self.state = 11
        elif(inputStr == '"'):
            self.auxLex += inputStr
            self.state = 2
        elif(re.match("[A-Za-zñ]", inputStr)):
            self.auxLex += inputStr
            self.state = 1
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
        if(not re.match("[A-Za-z0-9ñ]", inputStr)):
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
        self.auxLex += inputStr

    #########-----------------STATE 2 and 3-------------------#########
    def state_2(self, inputStr): 
        if inputStr == '"': 
            self.auxLex += inputStr
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
            self.auxLex += inputStr

    #########-----------------STATE 4-------------------#########
    def state_4(self, inputStr): 
        if inputStr == "!": 
            self.auxLex += inputStr
            self.state = 5
        else: 
            self.addToken(TokenType.SIG_MENOR_QUE, self.auxLex, self.row, self. column -1)
            self.state = 0
            self.auxLex = ""
            self.i -= 1
            self.column -= 1

    #########-----------------STATE 5-------------------#########
    def state_5(self, inputStr): 
        if inputStr == "-": 
            self.auxLex += inputStr
            self.state = 6
        else: 
            self.addToken(TokenType.DESCONOCIDO, self.auxLex, self.row, self. column -1)
            self.state = 0
            self.auxLex = ""
            self.i -= 1
            self.column -= 1
    
    #########-----------------STATE 6-------------------#########
    def state_6(self, inputStr): 
        if inputStr == "-": 
            self.auxLex += inputStr
            self.state = 7
        else: 
            self.addToken(TokenType.DESCONOCIDO, self.auxLex, self.row, self. column -1)
            self.state = 0
            self.auxLex = ""
            self.i -= 1
            self.column -= 1

    #########-----------------STATE 7-------------------#########
    def state_7(self, inputStr):
        if inputStr != "-":
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
        else: 
            self.auxLex += inputStr
            self.state = 8
    
    #########-----------------STATE 8-------------------#########
    def state_8(self, inputStr): 
        if inputStr != "-": 
            self.state = 7
            self.i -= 1
            self.column -= 1
        else: 
            self.auxLex += inputStr
            self.state = 9

    #########-----------------STATE 9 and 10-------------------#########
    def state_9(self, inputStr): 
        if inputStr != ">": 
            self.state = 7
            self.i -= 2
            self.column -= 2
        else: 
            self.auxLex += inputStr
            self.addToken(TokenType.COMENTARIO_MULTILINEA, self.auxLex, self.row, self.column - 1)
            self.auxLex = ""
            self.state = 0

    #########-----------------STATE 11 and 13-------------------#########
    def state_11(self, inputStr):
        if inputStr == '<': 
            self.addToken(TokenType.TEXTO, self.auxLex, self.row, self.column -1)
            self.state = 0
            self.auxLex = ""
            self.i -= 1
            self.column -= 1
        elif inputStr == "\n": 
            self.row += 1
            self.column = 1
            self.auxLex += inputStr
        else: 
            self.auxLex += inputStr
            self.state = 12

    #########-----------------STATE 12 and 13-------------------#########
    def state_12(self, inputStr):
        if inputStr == '<': 
            self.addToken(TokenType.TEXTO, self.auxLex, self.row, self.column -1)
            self.state = 0
            self.auxLex = ""
            self.i -= 1
            self.column -= 1
        elif inputStr == "\n": 
            self.row += 1
            self.column = 1
            self.auxLex += inputStr
        else: 
            self.auxLex += inputStr

    ###Método para agregar los tokens a la lista
    def addToken(self, tokenType, lexeme, row, column):
        self.output.append(Token(tokenType, lexeme, row, column))

    ###Método para mostrar la lista de tokens
    def showTokens(self):
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
                print(f"Lexeme: {tokens.getLexeme()}; TokenType: {tokens.getTokenType()}; row: {tokens.getRow()}; column: {tokens.getColumn()}")

        return cadena

    ###Método para mostrar los errores lexicos
    def showErrors(self): 
        count = 0
        for tokens in self.output:
            if(tokens == "\n" or tokens == "\t" or tokens == " "):
                continue
            elif(tokens.getTokenType() == "DESCONOCIDO"):
                count += 1
                print(f"Lexeme: {tokens.getLexeme()}; TokenType: {tokens.getTokenType()}; row: {tokens.getRow()}; column: {tokens.getColumn()}")

        if(count == 0): 
            print("there are not lexical erros") 