from Token_exp import TokenType
from Token_exp import Token

class Parser:

    def __init__(self, inputStr):
        self.inputStr = inputStr
        self.syntacticErros = []
        self.indice = 0
        #print(self.inputStr.values)
        if(self.inputStr != []):
            self.inputStr.append(Token(TokenType.DESCONOCIDO, "#", 0,0))
            self.preAnalysis = self.inputStr[self.indice]
            self.Expression()
        else:
            print("No hay nada que analizar")

    def Expression(self):
        if self.preAnalysis.getTokenType() == "PARENTESIS_ABRE" or self.preAnalysis.getTokenType() == "NUMERO" or self.preAnalysis.getTokenType() == "IDENTIFICADORES": 
            self.E()
            if self.preAnalysis.getLexeme() == "#" and self.indice == len(self.inputStr) - 1:
                print("Analisis Finalizado")
            else: 
                self.syntacticErros.append(self.preAnalysis)
                print("Error syntactico")
                return
        else: 
            self.syntacticErros.append(self.preAnalysis)
            print("Error syntactico")
            return

    def E(self):
        self.T()
        self.EP()

    def EP(self):
        if(self.preAnalysis.getLexeme() == '+'):
            self.Parea(TokenType.SIG_MAS, '+')
            self.T()
            self.EP()
        elif(self.preAnalysis.getLexeme() == '-'):
            self.Parea(TokenType.SIG_MENOS, '-')
            self.T()
            self.EP()
        else: 
            return

    def T(self):
        self.F()
        self.TP()

    def TP(self):
        if(self.preAnalysis.getLexeme() == '*'):
            self.Parea(TokenType.SIG_MULTIPLICACION, '*')
            self.F()
            self.TP()
        elif(self.preAnalysis.getLexeme() == '/'):
            self.Parea(TokenType.SIG_DIVIDIDO, '/')
            self.F()
            self.TP()
        else: 
            return

    def F(self):
        if(self.preAnalysis.getLexeme() == '('):
            self.Parea(TokenType.PARENTESIS_ABRE, '(')
            self.E()
            self.Parea(TokenType.PARENTESIS_CIERRA, ')')
        elif(self.preAnalysis.getTokenType() == "NUMERO"):
            self.Parea(TokenType.NUMERO, self.preAnalysis.getLexeme())
        elif(self.preAnalysis.getTokenType() == "IDENTIFICADORES"):
            self.Parea(TokenType.IDENTIFICADORES, self.preAnalysis.getLexeme())
        else:
            self.syntacticErros.append(self.preAnalysis)
            print("Error syntactico")
            return

    def Parea (self, TokenType, Lexeme):
        if TokenType.name == self.preAnalysis.getTokenType() and Lexeme == self.preAnalysis.getLexeme():
                self.indice += 1
                if self.indice < len(self.inputStr): 
                    self.preAnalysis = self.inputStr[self.indice]
                else: 
                    print("Analisis Finalizado")
        else:
            self.syntacticErros.append(self.preAnalysis)
            print("Error syntactico")
            return
            

    def imprimirsyntacticErros (self):
        for tokens in self.syntacticErros:
            print(f"Errorsyntactico: Token: {tokens.getTokenType()} Lexeme: {tokens.getLexeme()}")