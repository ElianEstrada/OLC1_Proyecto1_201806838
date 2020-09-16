from Token_exp import Token
from Token_exp import TokenType
import re
import os
from subprocess import call


class ScannerExp: 

    def __init__(self):
        self.output = []
        self.state = 0
        self.auxLex = ""
        self.row = 1
        self.column = 1
        self.flag = True

    def scannerExp(self, inputStr):
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
        return self.output

    #simula un switch utilizando diccionarios
    def switch(self, state):
        return {
            0: self.state_0,
            1: self.state_1,
            2: self.state_2,
            3: self.state_3,
        }.get(state)

    #########-----------------STATE 0-------------------##########
    #Recibe el caracter en la posición i
    def state_0(self, inputStr):
        if(inputStr == '('): 
            self.addToken(TokenType.PARENTESIS_ABRE, inputStr, self.row, self.column)
        elif(inputStr == ')'):
            self.addToken(TokenType.PARENTESIS_CIERRA, inputStr, self.row, self.column)
        elif(inputStr == '+'): 
            self.addToken(TokenType.SIG_MAS, inputStr, self.row, self.column)
        elif(inputStr == '-'): 
            self.addToken(TokenType.SIG_MENOS, inputStr, self.row, self.column)
        elif(inputStr == '*'): 
            self.addToken(TokenType.SIG_MULTIPLICACION, inputStr, self.row, self.column)
        elif(inputStr == '/'): 
            self.addToken(TokenType.SIG_DIVIDIDO, inputStr, self.row, self.column)
        elif(inputStr == '\n'): 
            self.row += 1
            self.column = 1
        elif(inputStr == '\t'): 
            self.column += 8
        elif(inputStr == ' '):
            self.state = 0
        elif(re.match("[A-Za-z_ñ]", inputStr)):
            self.auxLex += inputStr
            self.state = 1
        elif(inputStr.isdigit()):
            self.flag = True
            self.auxLex += inputStr
            self.state = 2
        else: 
            if(inputStr == '#' and self.i == len(self.inputStr2)): 
                print("Analysis Finished")
            else: 
                self.addToken(TokenType.DESCONOCIDO, inputStr, self.row, self.column)
                self.auxLex = ""

    #########-----------------STATE 1-------------------#########
    def state_1(self, inputStr):
        if(not re.match("[A-Za-z_0-9ñ]", inputStr)):
            self.addToken(TokenType.IDENTIFICADORES, self.auxLex, self.row, self.column - 1)
            self.auxLex = ""
            self.state = 0
            self.i -= 1
            self.column -= 1
            return
        self.auxLex += inputStr

    #########-----------------STATE 2 and 4-------------------#########
    def state_2(self, inputStr): 
        if(inputStr == '.' and self.flag):
            self.state = 3
            self.auxLex += inputStr
        elif(inputStr.isdigit()):
            self.auxLex += inputStr
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
            self.flag = False
            self.i -= 1
            self.column -= 1
        else: 
            self.addToken(TokenType.DESCONOCIDO, self.auxLex, self.row, self.column - 1)
            self.auxLex = ""
            self.state = 0
            self.i -= 1
            self.column -= 1

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