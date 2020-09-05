from enum import Enum

class TokenType(Enum):
    PALABRA_RESERVADA = 0
    IDENTIFICADORES = 1
    NUMEROS = 2
    CADENA_TEXTO = 3
    COMENTARIO_UNLINE = 4
    COMENTARIO_MULTILINEA = 5
    SIG_IGUAL = 6
    SIG_MULTIPLICACION = 7
    SIG_MAS = 8
    SIG_MENOS = 9
    SIG_DIVIDIDO = 10
    SIG_PUNTO_COMA = 11
    SIG_MAYOR_QUE = 12
    SIG_MENOR_QUE = 13
    SIG_NEGACION = 14
    LLAVES_ABRE = 15
    LLAVES_CIERRA = 16
    PARENTESIS_ABRE = 17
    PARENTESIS_CIERRA = 18
    SIG_AMPERSAN = 19
    SIG_PLECA = 20
    SIG_COMA = 21
    SIG_PUNTO = 22
    SIG_COMILLAS_DOBLES = 23
    SIG_COMILLAS_SIMPLES = 24
    SIG_DOS_PUTNOS = 25
    SIG_ACENTO_GRAVE = 26
    DESCONOCIDO = 27

class Token:

    def __init__(self, tokenType, lexeme, row, colum):
        self.tokenType = tokenType
        self.lexeme = lexeme
        self.row = row
        self.colum = colum

    def getLexeme(self):
        return self.lexeme

    def getTokenType(self):
        return  {
           TokenType.PALABRA_RESERVADA: "PALABRA_RESERVADA",
           TokenType.IDENTIFICADORES: "IDENTIFICADORES",
           TokenType.NUMEROS: "NÚMEROS",
           TokenType.CADENA_TEXTO: "CADENA_TEXTO",
           TokenType.COMENTARIO_UNLINE: "COMENTARIO_UNLINE",
           TokenType.COMENTARIO_MULTILINEA: "COMENTARIO_MULTILINEA",
           TokenType.SIG_IGUAL: "SIG_IGUAL",
           TokenType.SIG_MULTIPLICACION: "SIG_MULTIPLICACION",
           TokenType.SIG_MAS: "SIG_MAS",
           TokenType.SIG_MENOR_QUE: "SIG_MENOS",
           TokenType.SIG_DIVIDIDO: "SIG_DIVIDIDO",
           TokenType.SIG_PUNTO_COMA: "SIG_PUNTO_Y_COMA",
           TokenType.SIG_MAYOR_QUE: "SIG_MAYOR_QUE",
           TokenType.SIG_MENOR_QUE: "SIG_MENOR_QUE",
           TokenType.SIG_NEGACION: "SIG_NEGACION",
           TokenType.LLAVES_ABRE: "LLAVES_ABRE",
           TokenType.LLAVES_CIERRA: "LLAVES_CIERRA",
           TokenType.PARENTESIS_ABRE: "PARENTESIS_ABRE",
           TokenType.PARENTESIS_CIERRA: "PARENTESIS_CIERRA",
           TokenType.SIG_AMPERSAN: "SIG_AMPERSAN",
           TokenType.SIG_PLECA: "SIG_PLECA",
           TokenType.SIG_COMA: "SIG_COMA", 
           TokenType.SIG_PUNTO: "SIG_PUNTO",
           TokenType.SIG_COMILLAS_DOBLES: "SIG_COMILLAS_DOBLES",
           TokenType.SIG_COMILLAS_SIMPLES: "SIG_COMILLAS_SIMPLES",
           TokenType.SIG_DOS_PUTNOS: "SIG_DOS_PUNTOS",
           TokenType.SIG_ACENTO_GRAVE: "SIG_ACENTO_GRAVE",
           TokenType.DESCONOCIDO: "DESCONOCIDO"
        }.get(self.tokenType) 

            


