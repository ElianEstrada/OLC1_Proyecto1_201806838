from enum import Enum

class TokenType(Enum):
    PALABRA_RESERVADA = 0
    IDENTIFICADORES = 1
    CADENA_TEXTO = 2
    COMENTARIO_MULTILINEA = 3
    SIG_DIVISION = 4
    SIG_COMILLAS_DOBLES = 5
    SIG_IGUAL = 6
    SIG_MAYOR_QUE = 7
    SIG_MENOR_QUE = 8
    TEXTO = 9
    DESCONOCIDO = 10

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
           TokenType.PALABRA_RESERVADA: "PALABRA_RESERVADA",
           TokenType.IDENTIFICADORES: "IDENTIFICADORES",
           TokenType.CADENA_TEXTO: "CADENA_TEXTO",
           TokenType.COMENTARIO_MULTILINEA: "COMENTARIO_MULTILINEA",
           TokenType.SIG_DIVISION: "SIG_DIVISION",
           TokenType.SIG_COMILLAS_DOBLES: "COMILLAS_DOBLES",
           TokenType.SIG_IGUAL: "SIG_IGUAL",
           TokenType.SIG_MAYOR_QUE: "MAYOR_QUE", 
           TokenType.SIG_MENOR_QUE: "MENOR_QUE",
           TokenType.TEXTO: "TEXTO",
           TokenType.DESCONOCIDO: "DESCONOCIDO"
        }.get(self.tokenType) 