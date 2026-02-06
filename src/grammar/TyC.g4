grammar TyC;

options { language=Python3; }

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

/* =======================
   PARSER RULES
======================= */

program
    : decl+ EOF
    ;

decl
    : varDecl
    | funcDecl
    | structDecl
    ;

structDecl
    : STRUCT ID '{' varDecl* '}' ';'
    ;

varDecl
    : (type | AUTO) ID ('=' expr)? ';'
    ;

funcDecl
    : (returnType)? ID '(' paramList? ')' block
    ;

returnType
    : type
    | VOID
    | AUTO
    ;

paramList
    : param (',' param)*
    ;

param
    : type ID
    ;

type
    : INT
    | FLOAT
    | STRING
    | ID          // Struct type names
    ;

block
    : '{' (varDecl | stmt)* '}'
    ;

stmt
    : assignStmt
    | ifStmt
    | whileStmt
    | forStmt
    | switchStmt
    | breakStmt
    | continueStmt
    | returnStmt
    | exprStmt
    | block
    ;

assignStmt
    : lhs ASSIGN expr ';'
    ;

lhs
    : ID (DOT ID)*
    ;

ifStmt
    : IF '(' expr ')' stmt (ELSE stmt)?
    ;

whileStmt
    : WHILE '(' expr ')' stmt
    ;

forStmt
    : FOR '(' forInit? ';' expr? ';' forUpdate? ')' stmt
    ;

forInit
    : (type | AUTO) ID '=' expr 
    | lhs ASSIGN expr
    ;

forUpdate
    : lhs ASSIGN expr
    | unaryExpr
    | postfixExpr
    ;

switchStmt
    : SWITCH '(' expr ')' '{' (switchCase | defaultCase)* '}'
    ;

switchCase
    : CASE (unaryExpr | INTLIT | ID) ':' (stmt | varDecl)*
    ;

defaultCase
    : DEFAULT ':' (stmt | varDecl)*
    ;

breakStmt
    : BREAK ';'
    ;

continueStmt
    : CONTINUE ';'
    ;

returnStmt
    : RETURN expr? ';'
    ;

exprStmt
    : expr ';'
    ;

/* =======================
   EXPRESSIONS
======================= */

expr
    : assignExpr
    ;

assignExpr
    : logicalOrExpr (ASSIGN assignExpr)?
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
    : primaryExpr (INC | DEC | memberAccess | funcCall)*
    ;

funcCall
    : '(' argList? ')'
    ;

argList
    : expr (',' expr)*
    ;

memberAccess
    : DOT ID
    ;

primaryExpr
    : ID
    | INTLIT
    | FLOATLIT
    | STRINGLIT
    | '(' expr ')'
    | '{' argList? '}' // Struct initialization
    ;

/* =======================
   LEXER RULES
======================= */

INT      : 'int';
FLOAT    : 'float';
STRING   : 'string';
AUTO     : 'auto';
VOID     : 'void';
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

INTLIT : [0-9]+;

FLOATLIT
    : [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)?
    | '.' [0-9]+ ([eE] [+-]? [0-9]+)?
    | [0-9]+ [eE] [+-]? [0-9]+
    ;

/* String rules defined in order of detection priority */

ILLEGAL_ESCAPE
    : '"' ( ~["\\\r\n] | ESC_SEQ )* '\\' ~[btnfr"\\\r\n]
    ;

UNCLOSE_STRING
    : '"' ( ~["\\\r\n] | ESC_SEQ )* ([\r\n] | EOF)
    ;

STRINGLIT
    : '"' ( ~["\\\r\n] | ESC_SEQ )* '"'
    ;

fragment ESC_SEQ
    : '\\' [btnfr"\\]
    ;

ID : [a-zA-Z_][a-zA-Z_0-9]*;

LINE_COMMENT  : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;
WS : [ \t\f\r\n]+ -> skip;
ERROR_CHAR : .;