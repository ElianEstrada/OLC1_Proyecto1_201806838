from enum import Enum

class TokenType(Enum):
    PALABRA_RESERVADA = 0
    IDENTIFICADORES = 1
    NUMERO = 2
    CADENA_TEXTO = 3
    COMENTARIO_MULTILINEA = 4
    OP_UNIVERSAL = 5
    SIG_MENOS = 6
    SIG_PUNTO_COMA = 7
    LLAVES_ABRE = 8
    LLAVES_CIERRA = 9
    PARENTESIS_ABRE = 10
    PARENTESIS_CIERRA = 11
    SIG_COMA = 12
    SIG_PUNTO = 13
    SIG_COMILLAS_DOBLES = 14
    SIG_DOS_PUTNOS = 15
    SIG_PORCENTAJE = 16
    SIG_NUMERAL = 17
    DESCONOCIDO = 18

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
           TokenType.NUMERO: "NÚMERO",
           TokenType.CADENA_TEXTO: "CADENA_TEXTO",
           TokenType.COMENTARIO_MULTILINEA: "COMENTARIO_MULTILINEA",
           TokenType.SIG_PUNTO_COMA: "PUNTO_Y_COMA",
           TokenType.LLAVES_ABRE: "LLAVES_ABRE",
           TokenType.LLAVES_CIERRA: "LLAVES_CIERRA",
           TokenType.PARENTESIS_ABRE: "PARENTESIS_ABRE",
           TokenType.PARENTESIS_CIERRA: "PARENTESIS_CIERRA",
           TokenType.SIG_COMA: "COMA", 
           TokenType.SIG_PUNTO: "PUNTO",
           TokenType.SIG_COMILLAS_DOBLES: "COMILLAS_DOBLES",
           TokenType.SIG_DOS_PUTNOS: "SIG_DOS_PUNTOS",
           TokenType.SIG_PORCENTAJE: "PORCENTAJE", 
           TokenType.SIG_NUMERAL: "NUMERAL",
           TokenType.OP_UNIVERSAL: "SIG_UNIVERSAL",
           TokenType.DESCONOCIDO: "DESCONOCIDO"
        }.get(self.tokenType) 