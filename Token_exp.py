from enum import Enum

class TokenType(Enum):
    IDENTIFICADORES = 1
    NUMERO = 2
    SIG_MULTIPLICACION = 3
    SIG_MAS = 4
    SIG_MENOS = 5
    SIG_DIVIDIDO = 6
    PARENTESIS_ABRE = 7
    PARENTESIS_CIERRA = 8
    DESCONOCIDO = 9

class Token:

    def __init__(self, tokenType, lexeme, row, column):
        self.tokenType = tokenType
        self.lexeme = lexeme
        self.row = row
        self.column = column

    def getLexeme(self):
        return self.lexeme
    
    def getRow(self):
        return self.row
    
    def getColumn(self):
        return self.column

    def getTokenType(self):
        return  {
           TokenType.IDENTIFICADORES: "IDENTIFICADORES",
           TokenType.NUMERO: "NUMERO",
           TokenType.SIG_MULTIPLICACION: "SIG_MULTIPLICACION",
           TokenType.SIG_MAS: "SIG_MAS",
           TokenType.SIG_MENOS: "SIG_MENOS",
           TokenType.SIG_DIVIDIDO: "SIG_DIVIDIDO",
           TokenType.PARENTESIS_ABRE: "PARENTESIS_ABRE",
           TokenType.PARENTESIS_CIERRA: "PARENTESIS_CIERRA",
           TokenType.DESCONOCIDO: "DESCONOCIDO"
        }.get(self.tokenType) 