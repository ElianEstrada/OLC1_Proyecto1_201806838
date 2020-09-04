from Token_js import Token
from Token_js import TokenType

class Scanner: 

    def __init__(self):
        self.output = []
        self.state = 0
        self.auxLex = ""
        self.row = 0
        self.colum = 0

    def scannerJs(self, inputStr):
        inputStr += "#"
        self.output = []
        self.state = 0
        self.auxLex = ""
        self.i = 0

        while(self.i < len(inputStr)):
            
            c = inputStr[self.i]

            self.switch(self.state, c)(c)

            self.i += 1

    #simula un switch utilizando diccionarios
    def switch(self, state, c):
        return {
            0: self.state_0,
            1: self.state_1,
            2: self.state_2 
        }.get(state)

    ##va a recibir el caracter que tengamos en la posición i de nuestra cadena de entrada
    def state_0(self, inputStr):
        if(inputStr == '('): 
            self.addToken(TokenType.PARENTESIS_ABRE, inputStr, self.row, self.colum)
        elif(inputStr == ')'):
            self.addToken(TokenType.PARENTESIS_CIERRA, inputStr, self.row, self.colum)
        elif(inputStr.isdigit()):
            self.state = 1
            self.i -= 1

    def state_1(self, inputStr):
        return 

    def state_2(self, inputStr): 
        return 

    def addToken(self, tokenType, lexeme, row, colum):
        self.output.append(Token(tokenType, lexeme, row, colum))

    def showTokens(self):
        for tokens in self.output:
            print(tokens.getTokenType())

