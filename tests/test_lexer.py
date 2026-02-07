"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


def test1():
    """Test: auto x = 5 + 3 * 2;"""
    source = "auto x = 5 + 3 * 2;"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == "AUTO,auto,ID,x,ASSIGN,=,INTLIT,5,PLUS,+,INTLIT,3,MUL,*,INTLIT,2,SEMI,;,EOF"

def test2():
    """Test: int add(int x, int y) { return x + y; }"""
    source = "int add(int x, int y) { return x + y; }"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == "INT,int,ID,add,LPAREN,(,INT,int,ID,x,COMMA,,,INT,int,ID,y,RPAREN,),LBRACE,{,RETURN,return,ID,x,PLUS,+,ID,y,SEMI,;,RBRACE,},EOF"

def test3():
    """Test: int x = 10; float y = 3.14; string s = "hello";"""
    source = 'int x = 10; float y = 3.14; string s = "hello";'
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == 'INT,int,ID,x,ASSIGN,=,INTLIT,10,SEMI,;,FLOAT,float,ID,y,ASSIGN,=,FLOATLIT,3.14,SEMI,;,STRING,string,ID,s,ASSIGN,=,STRINGLIT,hello,SEMI,;,EOF'

def test4():
    """Test: struct Point { int x; int y; };"""
    source = "struct Point { int x; int y; };"
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == "STRUCT,struct,ID,Point,LBRACE,{,INT,int,ID,x,SEMI,;,INT,int,ID,y,SEMI,;,RBRACE,},SEMI,;,EOF"

def test5():
    """Test: Simple program with multiple statements"""
    source = "int x = 5; x = x + 1;"
    tokenizer = Tokenizer(source)
    result = tokenizer.get_tokens_as_string()
    assert "INT,int" in result and "ID,x" in result

# Keyword tests
def test_keyword_int():
    assert Tokenizer("int").get_tokens_as_string() == "INT,int,EOF"

def test_keyword_float():
    assert Tokenizer("float").get_tokens_as_string() == "FLOAT,float,EOF"

def test_keyword_string():
    assert Tokenizer("string").get_tokens_as_string() == "STRING,string,EOF"

def test_keyword_auto():
    assert Tokenizer("auto").get_tokens_as_string() == "AUTO,auto,EOF"

def test_keyword_void():
    assert Tokenizer("void").get_tokens_as_string() == "VOID,void,EOF"

def test_keyword_break():
    assert Tokenizer("break").get_tokens_as_string() == "BREAK,break,EOF"

def test_keyword_case():
    assert Tokenizer("case").get_tokens_as_string() == "CASE,case,EOF"

def test_keyword_continue():
    assert Tokenizer("continue").get_tokens_as_string() == "CONTINUE,continue,EOF"

def test_keyword_default():
    assert Tokenizer("default").get_tokens_as_string() == "DEFAULT,default,EOF"

def test_keyword_else():
    assert Tokenizer("else").get_tokens_as_string() == "ELSE,else,EOF"

def test_keyword_for():
    assert Tokenizer("for").get_tokens_as_string() == "FOR,for,EOF"

def test_keyword_if():
    assert Tokenizer("if").get_tokens_as_string() == "IF,if,EOF"

def test_keyword_return():
    assert Tokenizer("return").get_tokens_as_string() == "RETURN,return,EOF"

def test_keyword_struct():
    assert Tokenizer("struct").get_tokens_as_string() == "STRUCT,struct,EOF"

def test_keyword_switch():
    assert Tokenizer("switch").get_tokens_as_string() == "SWITCH,switch,EOF"

def test_keyword_while():
    assert Tokenizer("while").get_tokens_as_string() == "WHILE,while,EOF"

# Operator tests
def test_operator_equal():
    assert Tokenizer("==").get_tokens_as_string() == "EQ,==,EOF"

def test_operator_not_equal():
    assert Tokenizer("!=").get_tokens_as_string() == "NEQ,!=,EOF"

def test_operator_less_equal():
    assert Tokenizer("<=").get_tokens_as_string() == "LE,<=,EOF"

def test_operator_greater_equal():
    assert Tokenizer(">=").get_tokens_as_string() == "GE,>=,EOF"

def test_operator_or():
    assert Tokenizer("||").get_tokens_as_string() == "OR,||,EOF"

def test_operator_and():
    assert Tokenizer("&&").get_tokens_as_string() == "AND,&&,EOF"

def test_operator_increment():
    assert Tokenizer("++").get_tokens_as_string() == "INC,++,EOF"

def test_operator_decrement():
    assert Tokenizer("--").get_tokens_as_string() == "DEC,--,EOF"

def test_operator_assign():
    assert Tokenizer("=").get_tokens_as_string() == "ASSIGN,=,EOF"

def test_operator_less():
    assert Tokenizer("<").get_tokens_as_string() == "LT,<,EOF"

def test_operator_greater():
    assert Tokenizer(">").get_tokens_as_string() == "GT,>,EOF"

def test_operator_plus():
    assert Tokenizer("+").get_tokens_as_string() == "PLUS,+,EOF"

def test_operator_minus():
    assert Tokenizer("-").get_tokens_as_string() == "MINUS,-,EOF"

def test_operator_multiply():
    assert Tokenizer("*").get_tokens_as_string() == "MUL,*,EOF"

def test_operator_divide():
    assert Tokenizer("/").get_tokens_as_string() == "DIV,/,EOF"

def test_operator_modulo():
    assert Tokenizer("%").get_tokens_as_string() == "MOD,%,EOF"

def test_operator_not():
    assert Tokenizer("!").get_tokens_as_string() == "NOT,!,EOF"

def test_operator_dot():
    assert Tokenizer(".").get_tokens_as_string() == "DOT,.,EOF"

# Integer literal tests
def test_integer_zero():
    assert Tokenizer("0").get_tokens_as_string() == "INTLIT,0,EOF"

def test_integer_five():
    assert Tokenizer("5").get_tokens_as_string() == "INTLIT,5,EOF"

def test_integer_multi_digit():
    assert Tokenizer("12345").get_tokens_as_string() == "INTLIT,12345,EOF"

def test_integer_large():
    assert Tokenizer("999999999").get_tokens_as_string() == "INTLIT,999999999,EOF"

def test_integer_leading_zeros():
    assert Tokenizer("00123").get_tokens_as_string() == "INTLIT,00123,EOF"

def test_integer_multiple():
    assert Tokenizer("10 20 30").get_tokens_as_string() == "INTLIT,10,INTLIT,20,INTLIT,30,EOF"

# Float literal tests
def test_float_simple():
    assert Tokenizer("3.14").get_tokens_as_string() == "FLOATLIT,3.14,EOF"

def test_float_leading_zero():
    assert Tokenizer("0.5").get_tokens_as_string() == "FLOATLIT,0.5,EOF"

def test_float_no_leading():
    assert Tokenizer(".5").get_tokens_as_string() == "FLOATLIT,.5,EOF"

def test_float_no_trailing():
    assert Tokenizer("5.").get_tokens_as_string() == "FLOATLIT,5.,EOF"

def test_float_scientific_e():
    assert Tokenizer("1.23e4").get_tokens_as_string() == "FLOATLIT,1.23e4,EOF"

def test_float_scientific_E():
    assert Tokenizer("5.67E-2").get_tokens_as_string() == "FLOATLIT,5.67E-2,EOF"

def test_float_scientific_no_decimal():
    assert Tokenizer("42e10").get_tokens_as_string() == "FLOATLIT,42e10,EOF"

# String literal tests
def test_string_hello():
    assert Tokenizer('"hello"').get_tokens_as_string() == 'STRINGLIT,hello,EOF'

def test_string_with_spaces():
    assert Tokenizer('"hello world"').get_tokens_as_string() == 'STRINGLIT,hello world,EOF'

def test_string_escape_newline():
    result = Tokenizer('"hello\\nworld"').get_tokens_as_string()
    assert 'STRINGLIT,hello\\nworld' in result

def test_string_escape_tab():
    result = Tokenizer('"hello\\tworld"').get_tokens_as_string()
    assert 'STRINGLIT,hello\\tworld' in result
def test_string_multiple():
    result = Tokenizer('"a" "b" "c"').get_tokens_as_string()
    assert 'STRINGLIT,a' in result and 'STRINGLIT,b' in result and 'STRINGLIT,c' in result

def test_string_quote_escape():
    """Test: String with escaped quote"""
    result = Tokenizer('"hello\\"world"').get_tokens_as_string()
    assert 'STRINGLIT,hello\\"world' in result

def test_string_backslash_escape():
    """Test: String with escaped backslash"""
    result = Tokenizer('"path\\\\file"').get_tokens_as_string()
    assert 'STRINGLIT,path\\\\file' in result

# Identifier tests
def test_identifier_simple():
    assert Tokenizer("variable").get_tokens_as_string() == "ID,variable,EOF"

def test_identifier_underscore():
    assert Tokenizer("_var").get_tokens_as_string() == "ID,_var,EOF"

def test_identifier_with_digits():
    assert Tokenizer("var123").get_tokens_as_string() == "ID,var123,EOF"

def test_identifier_camelcase():
    assert Tokenizer("myVariable").get_tokens_as_string() == "ID,myVariable,EOF"

def test_identifier_uppercase():
    assert Tokenizer("MAX_VALUE").get_tokens_as_string() == "ID,MAX_VALUE,EOF"

def test_identifier_single_letter():
    assert Tokenizer("x").get_tokens_as_string() == "ID,x,EOF"

def test_identifier_multiple():
    result = Tokenizer("a b c").get_tokens_as_string()
    assert result == "ID,a,ID,b,ID,c,EOF"

# Comment tests
def test_line_comment():
    result = Tokenizer("// comment\nint x;").get_tokens_as_string()
    assert "INT,int" in result and "ID,x" in result

def test_block_comment():
    result = Tokenizer("/* comment */int x;").get_tokens_as_string()
    assert "INT,int" in result and "ID,x" in result

def test_block_comment_multiline():
    result = Tokenizer("/* line1\nline2 */int x;").get_tokens_as_string()
    assert "INT,int" in result

# Whitespace tests
def test_leading_whitespace():
    result = Tokenizer("   int x").get_tokens_as_string()
    assert "INT,int" in result and "ID,x" in result

def test_trailing_whitespace():
    result = Tokenizer("int x   ").get_tokens_as_string()
    assert "INT,int" in result and "ID,x" in result

def test_tab_whitespace():
    result = Tokenizer("int\tx\t5").get_tokens_as_string()
    assert "INT,int" in result and "ID,x" in result

def test_newline_whitespace():
    result = Tokenizer("int\nx\n5").get_tokens_as_string()
    assert "INT,int" in result and "ID,x" in result

# Complex expressions
def test_arithmetic():
    result = Tokenizer("x + y * z").get_tokens_as_string()
    assert "ID,x" in result and "PLUS,+" in result and "ID,y" in result

def test_comparison():
    result = Tokenizer("a < b").get_tokens_as_string()
    assert "ID,a" in result and "LT,<" in result and "ID,b" in result

def test_logical_and():
    result = Tokenizer("a && b").get_tokens_as_string()
    assert "ID,a" in result and "AND,&&" in result and "ID,b" in result

def test_logical_or():
    result = Tokenizer("a || b").get_tokens_as_string()
    assert "ID,a" in result and "OR,||" in result and "ID,b" in result

def test_member_access():
    result = Tokenizer("p.x").get_tokens_as_string()
    assert "ID,p" in result and "DOT,." in result and "ID,x" in result

def test_function_call():
    result = Tokenizer("func(a, b)").get_tokens_as_string()
    assert "ID,func" in result and "ID,a" in result and "ID,b" in result

def test_increment():
    result = Tokenizer("x++").get_tokens_as_string()
    assert "ID,x" in result and "INC,++" in result

def test_decrement():
    result = Tokenizer("x--").get_tokens_as_string()
    assert "ID,x" in result and "DEC,--" in result

# Edge cases
def test_empty_input():
    assert Tokenizer("").get_tokens_as_string() == "EOF"

def test_only_whitespace():
    assert Tokenizer("   \t  \n").get_tokens_as_string() == "EOF"

def test_consecutive_operators():
    result = Tokenizer("x++ + y").get_tokens_as_string()
    assert "INC,++" in result and "PLUS,+" in result

def test_complex_struct():
    result = Tokenizer("struct Point { int x; int y; }").get_tokens_as_string()
    assert "STRUCT,struct" in result and "ID,Point" in result
# Additional lexer tests for coverage
def test_separators_parentheses():
    """Test: Parentheses tokens"""
    result = Tokenizer("()").get_tokens_as_string()
    assert "LPAREN,(" in result and "RPAREN,)" in result

def test_separators_braces():
    """Test: Braces tokens"""
    result = Tokenizer("{}").get_tokens_as_string()
    assert "LBRACE,{" in result and "RBRACE,}" in result

def test_separator_semicolon():
    """Test: Semicolon token"""
    result = Tokenizer(";").get_tokens_as_string()
    assert "SEMI,;" in result

def test_separator_comma():
    """Test: Comma token"""
    result = Tokenizer(",").get_tokens_as_string()
    assert "COMMA,," in result

def test_mixed_operators():
    """Test: Multiple operators in one expression"""
    result = Tokenizer("a + b * c / d % e").get_tokens_as_string()
    assert "PLUS,+" in result and "MUL,*" in result and "DIV,/" in result and "MOD,%" in result

def test_all_comparison_operators():
    """Test: All comparison operators"""
    result = Tokenizer("a < b <= c > d >= e == f != g").get_tokens_as_string()
    assert "LT,<" in result and "LE,<=" in result and "GT,>" in result and "GE,>=" in result and "EQ,==" in result and "NEQ,!=" in result

def test_integer_zero_with_ops():
    """Test: Zero integer with operators"""
    result = Tokenizer("0 + 0 * 0").get_tokens_as_string()
    assert result == "INTLIT,0,PLUS,+,INTLIT,0,MUL,*,INTLIT,0,EOF"

def test_float_with_plus():
    """Test: Float number in expression"""
    result = Tokenizer("3.14 + 2.71").get_tokens_as_string()
    assert "FLOATLIT,3.14" in result and "PLUS,+" in result and "FLOATLIT,2.71" in result

def test_keywords_in_sequence():
    """Test: Multiple keywords in sequence"""
    result = Tokenizer("if while for switch").get_tokens_as_string()
    assert "IF,if" in result and "WHILE,while" in result and "FOR,for" in result and "SWITCH,switch" in result

def test_return_with_expr():
    """Test: Return statement with expression"""
    result = Tokenizer("return x + 5;").get_tokens_as_string()
    assert "RETURN,return" in result and "ID,x" in result and "PLUS,+" in result and "INTLIT,5" in result

def test_struct_keyword():
    """Test: Struct definition"""
    result = Tokenizer("struct Node").get_tokens_as_string()
    assert "STRUCT,struct" in result and "ID,Node" in result

def test_auto_declaration():
    """Test: Auto keyword for type inference"""
    result = Tokenizer("auto var = 42;").get_tokens_as_string()
    assert "AUTO,auto" in result and "ID,var" in result and "ASSIGN,=" in result and "INTLIT,42" in result

def test_void_function():
    """Test: Void return type"""
    result = Tokenizer("void func()").get_tokens_as_string()
    assert "VOID,void" in result and "ID,func" in result and "LPAREN,(" in result and "RPAREN,)" in result

def test_break_statement():
    """Test: Break keyword"""
    result = Tokenizer("break;").get_tokens_as_string()
    assert "BREAK,break" in result and "SEMI,;" in result

def test_continue_statement():
    """Test: Continue keyword"""
    result = Tokenizer("continue;").get_tokens_as_string()
    assert "CONTINUE,continue" in result and "SEMI,;" in result

def test_case_default():
    """Test: Case and default keywords"""
    result = Tokenizer("case default").get_tokens_as_string()
    assert "CASE,case" in result and "DEFAULT,default" in result

def test_else_statement():
    """Test: Else keyword"""
    result = Tokenizer("else").get_tokens_as_string()
    assert "ELSE,else" in result

def test_unary_operators():
    """Test: Unary operators"""
    result = Tokenizer("!x -y ++z --w").get_tokens_as_string()
    assert "NOT,!" in result and "MINUS,-" in result and "INC,++" in result and "DEC,--" in result

def test_logical_operators():
    """Test: Logical AND and OR"""
    result = Tokenizer("a && b || c").get_tokens_as_string()
    assert "AND,&&" in result and "OR,||" in result

def test_assignment_operators():
    """Test: Assignment operator"""
    result = Tokenizer("x = y").get_tokens_as_string()
    assert "ID,x" in result and "ASSIGN,=" in result and "ID,y" in result

def test_identifier_with_underscore_start():
    """Test: Identifier starting with underscore"""
    result = Tokenizer("_private").get_tokens_as_string()
    assert "ID,_private" in result

def test_identifier_mixed_case():
    """Test: Mixed case identifier"""
    result = Tokenizer("MyClass").get_tokens_as_string()
    assert "ID,MyClass" in result

def test_identifier_with_numbers():
    """Test: Identifier with numbers"""
    result = Tokenizer("var1 var2 var123").get_tokens_as_string()
    assert "ID,var1" in result and "ID,var2" in result and "ID,var123" in result

def test_string_empty():
    """Test: Empty string"""
    result = Tokenizer('""').get_tokens_as_string()
    assert 'STRINGLIT,' in result

def test_string_with_number():
    """Test: String containing numbers"""
    result = Tokenizer('"test123"').get_tokens_as_string()
    assert 'STRINGLIT,test123' in result

def test_string_with_special_chars():
    """Test: String with special characters"""
    result = Tokenizer('"hello-world_123"').get_tokens_as_string()
    assert 'STRINGLIT,hello-world_123' in result

def test_float_exponential_plus():
    """Test: Scientific notation with positive exponent"""
    result = Tokenizer("1.5e+10").get_tokens_as_string()
    assert "FLOATLIT,1.5e+10" in result

def test_float_exponential_negative():
    """Test: Scientific notation with negative exponent"""
    result = Tokenizer("2.5e-5").get_tokens_as_string()
    assert "FLOATLIT,2.5e-5" in result

def test_integer_then_float():
    """Test: Integer followed by float"""
    result = Tokenizer("10 3.14").get_tokens_as_string()
    assert "INTLIT,10" in result and "FLOATLIT,3.14" in result

def test_complex_expression_full():
    """Test: Complex arithmetic expression"""
    result = Tokenizer("(a + b) * (c - d) / e").get_tokens_as_string()
    assert "LPAREN,(" in result and "RPAREN,)" in result and "PLUS,+" in result and "MINUS,-" in result and "MUL,*" in result and "DIV,/" in result

def test_member_field_access():
    """Test: Accessing struct field"""
    result = Tokenizer("point.x").get_tokens_as_string()
    assert "ID,point" in result and "DOT,." in result and "ID,x" in result

def test_function_call_simple():
    """Test: Simple function call"""
    result = Tokenizer("foo()").get_tokens_as_string()
    assert "ID,foo" in result and "LPAREN,(" in result and "RPAREN,)" in result

def test_function_call_args():
    """Test: Function call with arguments"""
    result = Tokenizer("foo(a, b)").get_tokens_as_string()
    assert "ID,foo" in result and "ID,a" in result and "COMMA,," in result and "ID,b" in result

def test_increment_variants():
    """Test: Pre and post increment"""
    result = Tokenizer("++x x++").get_tokens_as_string()
    assert "INC,++" in result

def test_decrement_variants():
    """Test: Pre and post decrement"""
    result = Tokenizer("--y y--").get_tokens_as_string()
    assert "DEC,--" in result

def test_mixed_int_float():
    """Test: Mix of integer and float in expression"""
    result = Tokenizer("10 + 3.5 * 2").get_tokens_as_string()
    assert "INTLIT,10" in result and "FLOATLIT,3.5" in result and "INTLIT,2" in result

def test_keywords_all_types():
    """Test: All type keywords"""
    result = Tokenizer("int float string auto").get_tokens_as_string()
    assert "INT,int" in result and "FLOAT,float" in result and "STRING,string" in result and "AUTO,auto" in result

def test_keywords_all_control():
    """Test: All control flow keywords"""
    result = Tokenizer("if else for while switch case break continue default").get_tokens_as_string()
    assert "IF,if" in result and "ELSE,else" in result and "FOR,for" in result and "WHILE,while" in result and "SWITCH,switch" in result
def test_36_0():
    source = '-123'
    tokenize = Tokenizer(source)
    assert tokenize.get_tokens_as_string() == 'MINUS,-,INTLIT,123,EOF'
def test_36_1():
    source = '-0'
    tokenize = Tokenizer(source)
    assert tokenize.get_tokens_as_string() == 'MINUS,-,INTLIT,0,EOF'
def test_36_2():
    source = '--45'
    tokenize = Tokenizer(source)
    assert tokenize.get_tokens_as_string() == 'DEC,--,INTLIT,45,EOF'
def test_36_3():
    source = '-3.14'
    tokenize = Tokenizer(source)
    assert tokenize.get_tokens_as_string() == 'MINUS,-,FLOATLIT,3.14,EOF'
def test_36():
    source = '"raumania\\n\\b\\t\\r"'
    tokenize = Tokenizer(source)
    assert tokenize.get_tokens_as_string() == 'STRINGLIT,raumania\\n\\b\\t\\r,EOF'
def test_comment():
    source = '/**/*//**///***//*/*/**/'
    tokenize = Tokenizer(source)
    assert tokenize.get_tokens_as_string() == 'MUL,*,EOF'
def test_special_char():
    source = '"!@#$%^&*()_+-=[]{}|;:\',.<>/?`~"'
    tokenize = Tokenizer(source)
    assert tokenize.get_tokens_as_string() == 'STRINGLIT,!@#$%^&*()_+-=[]{}|;:\',.<>/?`~,EOF'
def test_special_char2():
    source = '"á ở bé ối ba sáu bê sô thịt kho tàu"'
    tokenize = Tokenizer(source)
    assert tokenize.get_tokens_as_string() == 'STRINGLIT,á ở bé ối ba sáu bê sô thịt kho tàu,EOF'
def test_special_char3():
    source = '"汉字漢字"'
    tokenize = Tokenizer(source)
    assert tokenize.get_tokens_as_string() == 'STRINGLIT,汉字漢字,EOF'
def test_special_char4():
    source = '"😀😃😄😁😆😅😂🤣😊😇"'
    tokenize = Tokenizer(source)
    assert tokenize.get_tokens_as_string() == 'STRINGLIT,😀😃😄😁😆😅😂🤣😊😇,EOF'
def test_leading_zeros():
    source = '000123 000.456 0.007890000'
    tokenize = Tokenizer(source)
    assert tokenize.get_tokens_as_string() == 'INTLIT,000123,FLOATLIT,000.456,FLOATLIT,0.007890000,EOF'
def test_mixed_comments():
    source = 'int x; /* block comment */ // line comment\n x = 5;'
    tokenize = Tokenizer(source)
    assert tokenize.get_tokens_as_string() == 'INT,int,ID,x,SEMI,;,ID,x,ASSIGN,=,INTLIT,5,SEMI,;,EOF'
def test_error():
    source = '"Unclosed string literal'
    tokenize = Tokenizer(source)
    assert tokenize.get_tokens_as_string() == 'lexererr.UncloseString: Unclosed String: Unclosed string literal'
