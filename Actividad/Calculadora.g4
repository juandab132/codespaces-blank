grammar Calculadora;

// Regla inicial
prog:   stat+ ;

// Reglas de sentencias
stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   funcionDef NEWLINE          # functionDefinition
    |   NEWLINE                     # blank
    ;

// Expresiones
expr:   expr ('*'|'/') expr         # MulDiv
    |   expr ('+'|'-') expr         # AddSub
    |   INT                         # int
    |   ID                          # id
    |   ID '(' args? ')'            # functionCall
    |   '(' expr ')'                # parens
    ;

// Definición de función
funcionDef
    :   'func' ID '(' params? ')' '{' stat+ '}'
    ;

// Argumentos y parámetros
args:   expr (',' expr)* ;
params: ID (',' ID)* ;

// Tokens
ID  :   [a-zA-Z]+ ;
INT :   [0-9]+ ;
NEWLINE:'\r'? '\n' ;
WS  :   [ \t]+ -> skip ;
