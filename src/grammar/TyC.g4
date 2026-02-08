grammar TyC;

options { language=Python3; }

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    # Logic to satisfy "String Token Processing" requirements
    if tk == self.STRINGLIT:
        # Strip the enclosing double quotes for valid strings
        self.text = self.text[1:-1]
        return super().emit()
    elif tk == self.UNCLOSE_STRING:
        # Remove opening quote, keep content for error message
        self.text = self.text[1:]
        result = super().emit()
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        # Remove opening quote, keep content for error message
        self.text = self.text[1:]
        result = super().emit()
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        result = super().emit()
        raise ErrorToken(result.text) 
    else:
        return super().emit()
}
/* =======================
   PARSER RULES
======================= */

program
    : decl+ EOF
    ;

decl
    : varDecl
    | mainDecl
    | funcDecl
    | structDecl
    ;

structDecl
    : STRUCT ID LBRACE structVar* RBRACE SEMI
    ;
structVar
    : type ID SEMI;

/* ---- Variable ---- */

varDecl
    : type ID (ASSIGN expr)? SEMI        // explicit type
    | AUTO ID (ASSIGN expr)? SEMI           // auto MUST have init
    ;

/* ---- Function ---- */
mainDecl
    : VOID MAIN LPAREN RPAREN block
    ;

funcDecl
    : returnType? ID LPAREN paramList? RPAREN block
    ;
returnType
    : type
    | VOID
    ;


paramList
    : param (COMMA param)*
    ;

param
    : type ID
    ;

type
    : INT
    | FLOAT
    | STRING
    | ID
    ;

/* ---- Block & Statements ---- */

block
    : LBRACE (varDecl | stmt)* RBRACE
    ;


stmt
    // : assignStmt
    : ifStmt
    | whileStmt
    | forStmt
    | switchStmt
    | breakStmt
    | continueStmt
    | returnStmt
    | exprStmt
    | block
    ;

// assignStmt
//     : lhs ASSIGN expr SEMI
//     ;

lhs
    : ID (memberAccess)*
    | postfixExpr memberAccess+
    ;

ifStmt
    : IF LPAREN expr RPAREN stmt (ELSE stmt)?
    ;

whileStmt
    : WHILE LPAREN expr RPAREN stmt
    ;

forStmt
    : FOR LPAREN forInit? SEMI expr? SEMI forUpdate? RPAREN stmt
    ;

forInit
    : type ID ASSIGN expr
    | AUTO ID ASSIGN expr
    | lhs ASSIGN expr
    ;

forUpdate
    : lhs ASSIGN expr
    | unaryExpr
    | postfixExpr
    ;

switchStmt
    : SWITCH LPAREN expr RPAREN 
      LBRACE switchCase* defaultCase? switchCase* RBRACE
    ;


switchCase
    : CASE expr COLON (stmt | varDecl)*
    ;

defaultCase
    : DEFAULT COLON (stmt | varDecl)*
    ;

breakStmt
    : BREAK SEMI
    ;

continueStmt
    : CONTINUE SEMI
    ;

returnStmt
    : RETURN expr? SEMI
    ;
returnVoidStmt
    : RETURN SEMI
    ;
exprStmt
    : expr SEMI
    ;

/* =======================
   EXPRESSIONS
======================= */

expr
    : assignExpr
    ;

assignExpr
    : lhs ASSIGN assignExpr
    | logicalOrExpr
    ;

logicalOrExpr
    : logicalAndExpr (OR logicalAndExpr)*
    ;

logicalAndExpr
    : equalityExpr (AND equalityExpr)*
    ;

equalityExpr
    : relationalExpr ((EQ | NEQ) relationalExpr)*
    ;

relationalExpr
    : additiveExpr ((LT | GT | LE | GE) additiveExpr)*
    ;

additiveExpr
    : multiplicativeExpr ((PLUS | MINUS) multiplicativeExpr)*
    ;

multiplicativeExpr
    : unaryExpr ((MUL | DIV | MOD) unaryExpr)*
    ;

unaryExpr
    : (NOT | PLUS | MINUS | INC | DEC) unaryExpr
    | postfixExpr
    ;

postfixExpr
    : primaryExpr postfixPart*
    ;

postfixPart
    : memberAccess
    | funcCall
    | INC
    | DEC
    ;

funcCall
    : LPAREN argList? RPAREN
    ;

argList
    : expr (COMMA expr)*
    ;

memberAccess
    : DOT ID
    ;

primaryExpr
    : ID
    | INTLIT
    | FLOATLIT
    | STRINGLIT
    | LPAREN expr RPAREN
    ;

/* =======================
   LEXER RULES
======================= */

/* ---- Separators ---- */

SEMI   : ';' ;
COMMA  : ',' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
COLON  : ':' ;

/* ---- Keywords ---- */

INT      : 'int';
FLOAT    : 'float';
STRING   : 'string';
AUTO     : 'auto';
VOID     : 'void';

MAIN     : 'main';
BREAK    : 'break';
CASE     : 'case';
CONTINUE : 'continue';
DEFAULT  : 'default';
ELSE     : 'else';
FOR      : 'for';
IF       : 'if';
RETURN   : 'return';
STRUCT   : 'struct';
SWITCH   : 'switch';
WHILE    : 'while';

/* ---- Operators ---- */

EQ     : '==';
NEQ    : '!=';
LE     : '<=';
GE     : '>=';
OR     : '||';
AND    : '&&';
INC    : '++';
DEC    : '--';

ASSIGN : '=';
LT     : '<';
GT     : '>';
PLUS   : '+';
MINUS  : '-';
MUL    : '*';
DIV    : '/';
MOD    : '%';
NOT    : '!';
DOT    : '.';

/* ---- Literals ---- */


FLOATLIT
    : [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)?
    | '.' [0-9]+ ([eE] [+-]? [0-9]+)?
    | [0-9]+ [eE] [+-]? [0-9]+
    ;
INTLIT :  [0-9]+ ;

/* ---- String ---- */

ILLEGAL_ESCAPE
    : '"' ( ~["\\\r\n] | ESC_SEQ )* '\\' ~[btnfr"\\\r\n]
    ;

UNCLOSE_STRING
    : '"' ( ~["\\\r\n] | ESC_SEQ )*
      ( '\\' EOF
      | [\r\n]
      | EOF
      )
    ;

STRINGLIT
    : '"' ( ~["\\\r\n] | ESC_SEQ )* '"'
    ;

fragment ESC_SEQ
    : '\\' [btnfr"\\]
    ;

/* ---- Identifier ---- */

ID : [a-zA-Z_][a-zA-Z_0-9]* ;

/* ---- Comments & WS ---- */

LINE_COMMENT  : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
WS : [ \t\f\r\n]+ -> skip ;

ERROR_CHAR : . ;