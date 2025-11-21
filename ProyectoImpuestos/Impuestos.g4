// El nombre de la gramática DEBE coincidir con el nombre del archivo (Impuestos.g4)
grammar Impuestos;


// Regla inicial del programa: 1..n sentencias y luego fin de archivo

program
   : (statement)+ EOF          // Un programa es una o más sentencias seguidas del fin de archivo
    ;


// Conjunto de sentencias soportadas por el lenguaje

statement
    : assignment                // Asignación de una variable
    | ifStatement               // Estructura condicional 'si ... : ...;'
    | printStatement            // Instrucción de impresión 'print(...)'
    ;


// Sentencias específicas


// Ejemplo: ingreso = 120000;
assignment
    : ID '=' expr ';'           // Identificador, signo '=', expresión y ';'
    ;

// Ejemplo: si ingreso > 100000: impuesto = ingreso * 0.2;
ifStatement
    : 'si' condition ':' statement   // Palabra clave 'si', condición, ':', y una sentencia anidada
    ;

// Ejemplo: print(impuesto);
printStatement
    : 'print' '(' ID ')' ';'    // print( ID );
    ;


// Reglas para condiciones y expresiones


// Ejemplo: ingreso > 100000
condition
    : ID comparator expr        // ID comp expr (p.ej., x > 10, x <= y+1)
    ;

// Ejemplo: ingreso * 0.2 + bono
expr
    : term (op term)*           // Expresión: uno o más términos combinados con operadores
    ;

// Un término puede ser un identificador o un número
term
    : ID                        // Variable/identificador
    | NUMBER                    // Literal numérico (entero o decimal)
    ;

// ------------------------------------------------------------
// Operadores aritméticos válidos
// ------------------------------------------------------------
op
    : '+' | '-' | '*' | '/'     // Suma, resta, multiplicación, división
    ;

// ------------------------------------------------------------
// Operadores relacionales válidos en condiciones
// ------------------------------------------------------------
comparator
    : '<' | '>' | '<=' | '>=' | '==' | '!='   // Menor, mayor, etc.
    ;

// ------------------------------------------------------------
// Definiciones léxicas (tokens)
// ------------------------------------------------------------

// Identificador: empieza con letra o '_' y puede contener dígitos
ID
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

// Número: entero o decimal con punto
NUMBER
    : [0-9]+ ('.' [0-9]+)?
    ;

// Espacios/tabulaciones/saltos de línea: ignorados por el lexer
WS
    : [ \t\r\n]+ -> skip
    ;
