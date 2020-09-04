from enum import Enum

class TokenType(Enum):
    PALABRA_RESERVADA = 0
    IDENTIFICADORES = 1
    NUMEROS = 2
    CADENA_TEXTO = 3
    COMENTARIO_UNLINE = 4
    SIG_IGUAL = 5
    SIG_MULTIPLICACION = 6
    SIG_MAS = 7
    SIG_MENOS = 8
    SIG_DIVIDIDO = 9
    SIG_PUNTO_COMA = 10
    SIG_MAYOR_QUE = 11
    SIG_MENOR_QUE = 12
    SIG_NEGACION = 13
    LLAVES_ABRE = 14
    LLAVES_CIERRA = 15
    PARENTESIS_ABRE = 16
    PARENTESIS_CIERRA = 17
    SIG_AMPERSAN = 18
    SIG_PLECA = 19
    SIG_COMA = 20
    SIG_PUNTO = 21
    SIG_COMILLAS_DOBLES = 22
    SIG_COMILLAS_SIMPLES = 23
    SIG_DOS_PUTNOS = 24
    SIG_ACENTO_GRAVE = 25
    DESCONOCIDO = 26

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
           TokenType.PARENTESIS_ABRE: "PARENTESIS_ABRE",
           TokenType.PARENTESIS_CIERRA: "PARENTESIS_CIERRA"
        }.get(self.tokenType) 

            


