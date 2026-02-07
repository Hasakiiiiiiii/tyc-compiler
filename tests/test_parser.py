"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


def test_parser_placeholder():
    """Placeholder test - basic program"""
    source = "void main() { }"
    parser = Parser(source)
    result = parser.parse()
    assert result == "success"

# Basic Program Structure
def test_program_empty_main():
    """Test: Program with empty main function"""
    result = Parser("void main() { }").parse()
    assert result == "success"

def test_program_single_function():
    """Test: Program with single function"""
    result = Parser("int foo() { return 0; }").parse()
    assert result == "success"

def test_program_multiple_functions():
    """Test: Program with multiple functions"""
    result = Parser("int foo() { return 1; } float bar() { return 2.5; } void main() { }").parse()
    assert result == "success"

def test_program_struct_then_function():
    """Test: Struct definition followed by function"""
    result = Parser("struct Point { int x; int y; }; void main() { }").parse()
    assert result == "success"

def test_program_multiple_structs():
    """Test: Multiple struct definitions"""
    result = Parser("struct A { int x; }; struct B { float y; }; void main() { }").parse()
    assert result == "success"

# Function Declaration and Definition
def test_function_void_return():
    """Test: Function with void return type"""
    result = Parser("void func() { }").parse()
    assert result == "success"

def test_function_int_return():
    """Test: Function with int return type"""
    result = Parser("int func() { return 5; }").parse()
    assert result == "success"

def test_function_float_return():
    """Test: Function with float return type"""
    result = Parser("float func() { return 3.14; }").parse()
    assert result == "success"

def test_function_string_return():
    """Test: Function with string return type"""
    result = Parser('string func() { return "hello"; }').parse()
    assert result == "success"

def test_function_no_params():
    """Test: Function with no parameters"""
    result = Parser("int func() { }").parse()
    assert result == "success"

def test_function_single_param():
    """Test: Function with single parameter"""
    result = Parser("int func(int x) { }").parse()
    assert result == "success"

def test_function_multiple_params():
    """Test: Function with multiple parameters"""
    result = Parser("int add(int x, int y) { }").parse()
    assert result == "success"

def test_function_many_params():
    """Test: Function with many parameters"""
    result = Parser("void func(int a, float b, string c, int d) { }").parse()
    assert result == "success"

def test_function_different_param_types():
    """Test: Function with different parameter types"""
    result = Parser("float calc(int x, float y, string label) { }").parse()
    assert result == "success"

# Struct Declaration
def test_struct_simple():
    """Test: Simple struct with one field"""
    result = Parser("struct Point { int x; };").parse()
    assert result == "success"

def test_struct_multiple_fields():
    """Test: Struct with multiple fields"""
    result = Parser("struct Point { int x; int y; };").parse()
    assert result == "success"

def test_struct_different_types():
    """Test: Struct with different field types"""
    result = Parser("struct Person { int age; float height; string name; };").parse()
    assert result == "success"

def test_struct_many_fields():
    """Test: Struct with many fields"""
    result = Parser("struct Data { int a; float b; string c; int d; float e; };").parse()
    assert result == "success"

# Variable Declaration
def test_var_decl_int():
    """Test: Integer variable declaration"""
    result = Parser("void main() { int x; }").parse()
    assert result == "success"

def test_var_decl_float():
    """Test: Float variable declaration"""
    result = Parser("void main() { float x; }").parse()
    assert result == "success"

def test_var_decl_string():
    """Test: String variable declaration"""
    result = Parser("void main() { string x; }").parse()
    assert result == "success"

def test_var_decl_auto():
    """Test: Auto variable declaration"""
    result = Parser("void main() { auto x = 5; }").parse()
    assert result == "success"

def test_var_decl_multiple():
    """Test: Multiple variable declarations"""
    result = Parser("void main() { int x; float y; string z; }").parse()
    assert result == "success"

# Variable Initialization
def test_var_init_int():
    """Test: Integer variable with initialization"""
    result = Parser("void main() { int x = 5; }").parse()
    assert result == "success"

def test_var_init_float():
    """Test: Float variable with initialization"""
    result = Parser("void main() { float x = 3.14; }").parse()
    assert result == "success"

def test_var_init_string():
    """Test: String variable with initialization"""
    result = Parser('void main() { string x = "hello"; }').parse()
    assert result == "success"

def test_var_init_expression():
    """Test: Variable initialization with expression"""
    result = Parser("void main() { int x = 5 + 3; }").parse()
    assert result == "success"

# Assignment Statements
def test_assignment_int():
    """Test: Integer assignment"""
    result = Parser("void main() { x = 5; }").parse()
    assert result == "success"

def test_assignment_float():
    """Test: Float assignment"""
    result = Parser("void main() { x = 3.14; }").parse()
    assert result == "success"

def test_assignment_expression():
    """Test: Assignment with expression"""
    result = Parser("void main() { x = a + b; }").parse()
    assert result == "success"

def test_assignment_chain():
    """Test: Chained assignment"""
    result = Parser("void main() { x = y = z = 5; }").parse()
    assert result == "success"

# Control Flow: If Statement
def test_if_statement():
    """Test: Simple if statement"""
    result = Parser("void main() { if (x > 0) { } }").parse()
    assert result == "success"

def test_if_else_statement():
    """Test: If-else statement"""
    result = Parser("void main() { if (x > 0) { } else { } }").parse()
    assert result == "success"

def test_if_nested():
    """Test: Nested if statement"""
    result = Parser("void main() { if (x > 0) { if (y > 0) { } } }").parse()
    assert result == "success"

def test_if_with_multiple_statements():
    """Test: If with multiple statements in body"""
    result = Parser("void main() { if (x > 0) { a = 1; b = 2; } }").parse()
    assert result == "success"

def test_if_else_if():
    """Test: If-else if-else chain"""
    result = Parser("void main() { if (x > 0) { } else { if (y > 0) { } else { } } }").parse()
    assert result == "success"

# Control Flow: While Loop
def test_while_loop():
    """Test: Simple while loop"""
    result = Parser("void main() { while (x < 10) { } }").parse()
    assert result == "success"

def test_while_with_body():
    """Test: While loop with statements"""
    result = Parser("void main() { while (x < 10) { x = x + 1; } }").parse()
    assert result == "success"

def test_while_nested():
    """Test: Nested while loops"""
    result = Parser("void main() { while (x < 10) { while (y < 5) { } } }").parse()
    assert result == "success"

def test_while_with_break():
    """Test: While loop with break"""
    result = Parser("void main() { while (1) { break; } }").parse()
    assert result == "success"

def test_while_with_continue():
    """Test: While loop with continue"""
    result = Parser("void main() { while (x < 10) { x++; continue; } }").parse()
    assert result == "success"

# Control Flow: For Loop
def test_for_loop_simple():
    """Test: Simple for loop"""
    result = Parser("void main() { for (int i = 0; i < 10; i++) { } }").parse()
    assert result == "success"

def test_for_loop_with_body():
    """Test: For loop with statements"""
    result = Parser("void main() { for (int i = 0; i < 10; i++) { a = i; } }").parse()
    assert result == "success"

def test_for_loop_nested():
    """Test: Nested for loops"""
    result = Parser("void main() { for (int i = 0; i < 10; i++) { for (int j = 0; j < 10; j++) { } } }").parse()
    assert result == "success"

def test_for_loop_with_break():
    """Test: For loop with break"""
    result = Parser("void main() { for (int i = 0; i < 10; i++) { break; } }").parse()
    assert result == "success"

def test_for_loop_with_continue():
    """Test: For loop with continue"""
    result = Parser("void main() { for (int i = 0; i < 10; i++) { continue; } }").parse()
    assert result == "success"

# Control Flow: Switch Statement
def test_switch_single_case():
    """Test: Switch with single case"""
    result = Parser("void main() { switch (x) { case 1: break; } }").parse()
    assert result == "success"

def test_switch_multiple_cases():
    """Test: Switch with multiple cases"""
    result = Parser("void main() { switch (x) { case 1: break; case 2: break; } }").parse()
    assert result == "success"

def test_switch_with_default():
    """Test: Switch with default case"""
    result = Parser("void main() { switch (x) { case 1: break; default: break; } }").parse()
    assert result == "success"

def test_switch_with_statements():
    """Test: Switch with statements in cases"""
    result = Parser("void main() { switch (x) { case 1: a = 1; b = 2; break; } }").parse()
    assert result == "success"

def test_switch_nested():
    """Test: Nested switch statements"""
    result = Parser("void main() { switch (x) { case 1: switch (y) { case 2: break; } } }").parse()
    assert result == "success"

# Return Statements
def test_return_void():
    """Test: Return without value"""
    result = Parser("void main() { return; }").parse()
    assert result == "success"

def test_return_int():
    """Test: Return integer"""
    result = Parser("int func() { return 5; }").parse()
    assert result == "success"

def test_return_float():
    """Test: Return float"""
    result = Parser("float func() { return 3.14; }").parse()
    assert result == "success"

def test_return_string():
    """Test: Return string"""
    result = Parser('string func() { return "hello"; }').parse()
    assert result == "success"

def test_return_expression():
    """Test: Return expression"""
    result = Parser("int func() { return a + b; }").parse()
    assert result == "success"

# Expressions: Arithmetic
def test_expr_addition():
    """Test: Addition expression"""
    result = Parser("void main() { a + b; }").parse()
    assert result == "success"

def test_expr_subtraction():
    """Test: Subtraction expression"""
    result = Parser("void main() { a - b; }").parse()
    assert result == "success"

def test_expr_multiplication():
    """Test: Multiplication expression"""
    result = Parser("void main() { a * b; }").parse()
    assert result == "success"

def test_expr_division():
    """Test: Division expression"""
    result = Parser("void main() { a / b; }").parse()
    assert result == "success"

def test_expr_modulo():
    """Test: Modulo expression"""
    result = Parser("void main() { a % b; }").parse()
    assert result == "success"

# Expressions: Comparison
def test_expr_less_than():
    """Test: Less than comparison"""
    result = Parser("void main() { a < b; }").parse()
    assert result == "success"

def test_expr_greater_than():
    """Test: Greater than comparison"""
    result = Parser("void main() { a > b; }").parse()
    assert result == "success"

def test_expr_less_equal():
    """Test: Less than or equal comparison"""
    result = Parser("void main() { a <= b; }").parse()
    assert result == "success"

def test_expr_greater_equal():
    """Test: Greater than or equal comparison"""
    result = Parser("void main() { a >= b; }").parse()
    assert result == "success"

def test_expr_equal():
    """Test: Equality comparison"""
    result = Parser("void main() { a == b; }").parse()
    assert result == "success"

def test_expr_not_equal():
    """Test: Inequality comparison"""
    result = Parser("void main() { a != b; }").parse()
    assert result == "success"

# Expressions: Logical
def test_expr_and():
    """Test: Logical AND"""
    result = Parser("void main() { a && b; }").parse()
    assert result == "success"

def test_expr_or():
    """Test: Logical OR"""
    result = Parser("void main() { a || b; }").parse()
    assert result == "success"

def test_expr_not():
    """Test: Logical NOT"""
    result = Parser("void main() { !a; }").parse()
    assert result == "success"

# Expressions: Unary
def test_expr_unary_minus():
    """Test: Unary minus"""
    result = Parser("void main() { -a; }").parse()
    assert result == "success"

def test_expr_unary_plus():
    """Test: Unary plus"""
    result = Parser("void main() { +a; }").parse()
    assert result == "success"

def test_expr_prefix_increment():
    """Test: Prefix increment"""
    result = Parser("void main() { ++a; }").parse()
    assert result == "success"

def test_expr_prefix_decrement():
    """Test: Prefix decrement"""
    result = Parser("void main() { --a; }").parse()
    assert result == "success"

def test_expr_postfix_increment():
    """Test: Postfix increment"""
    result = Parser("void main() { a++; }").parse()
    assert result == "success"

def test_expr_postfix_decrement():
    """Test: Postfix decrement"""
    result = Parser("void main() { a--; }").parse()
    assert result == "success"

# Expressions: Member Access
def test_expr_member_access():
    """Test: Member field access"""
    result = Parser("void main() { p.x; }").parse()
    assert result == "success"

def test_expr_member_chain():
    """Test: Chained member access"""
    result = Parser("void main() { a.b.c; }").parse()
    assert result == "success"

def test_expr_member_assignment():
    """Test: Member field assignment"""
    result = Parser("void main() { p.x = 5; }").parse()
    assert result == "success"

# Expressions: Function Call
def test_expr_function_call_no_args():
    """Test: Function call without arguments"""
    result = Parser("void main() { foo(); }").parse()
    assert result == "success"

def test_expr_function_call_one_arg():
    """Test: Function call with one argument"""
    result = Parser("void main() { foo(5); }").parse()
    assert result == "success"

def test_expr_function_call_multiple_args():
    """Test: Function call with multiple arguments"""
    result = Parser("void main() { foo(a, b, c); }").parse()
    assert result == "success"

def test_expr_function_call_nested():
    """Test: Nested function calls"""
    result = Parser("void main() { foo(bar(baz())); }").parse()
    assert result == "success"

# Expressions: Operator Precedence
def test_expr_precedence_mult_add():
    """Test: Multiplication before addition"""
    result = Parser("void main() { a + b * c; }").parse()
    assert result == "success"

def test_expr_precedence_parentheses():
    """Test: Parentheses override precedence"""
    result = Parser("void main() { (a + b) * c; }").parse()
    assert result == "success"

def test_expr_precedence_comparison():
    """Test: Comparison operators precedence"""
    result = Parser("void main() { a < b && b < c; }").parse()
    assert result == "success"

# Complex Programs
def test_complex_program_with_struct():
    """Test: Program with struct and usage"""
    result = Parser("struct Point { int x; int y; }; void main() { Point p; p.x = 5; }").parse()
    assert result == "success"

def test_complex_program_functions():
    """Test: Program with multiple function definitions"""
    result = Parser("int add(int a, int b) { return a + b; } void main() { int x = add(3, 4); }").parse()
    assert result == "success"

def test_complex_nested_loops():
    """Test: Complex nested loops"""
    result = Parser("void main() { for (int i = 0; i < 10; i++) { for (int j = 0; j < i; j++) { } } }").parse()
    assert result == "success"

def test_complex_control_flow():
    """Test: Complex control flow mixing if/while/for"""
    result = Parser("void main() { if (x > 0) { while (y < 10) { for (int i = 0; i < 5; i++) { } } } }").parse()
    assert result == "success"

def test_complex_expressions():
    """Test: Complex arithmetic and logical expressions"""
    result = Parser("void main() { (a + b) * (c - d) / e > f && g <= h || i != j; }").parse()
    assert result == "success"
def test_36():
    result = Parser("void main() { auto x; x = 5; }").parse()
    assert result == "success"
def test_error():
    result = Parser("void main( { }").parse()
    assert result == "Error on line 1 col 11: {"
def test_struct_empty():
    input = "struct Empty { };"
    assert Parser(input).parse() == "success"
def test_struct_primitives():
    input = "struct Point { int x; int y; float z; };"
    assert Parser(input).parse() == "success"
def test_struct_with_struct_member():
    input = """
    struct Point {
        int x;
        int y;
    };

    struct Line {
        Point start;
        Point end;
    };
    """
    assert Parser(input).parse() == "success"
def test_struct_and_var_decl():
    input = """
    struct Person {
        string name;
        int age;
    };

    Person p;
    """
    assert Parser(input).parse() == "success"
def test_struct_member_auto_invalid():
    input = """
    struct Bad {
        auto x;
    };
    """
    assert Parser(input).parse() == "Error on line 3 col 8: auto"
def test_nested_struct_invalid():
    input = """
    struct A {
        int x;
        struct B {
            int y;
        };
    };
    """
    assert Parser(input).parse() == "Error on line 4 col 8: struct"
def test_struct_forward_reference_invalid():
    input = """
    struct B {
        A x;
    };

    struct A {
        int y;
    };
    """
    assert Parser(input).parse() == "success"
def test_duplicate_struct_name_invalid():
    input = """
    struct A {
        int x;
    };

    struct A {
        int y;
    };
    """
    assert Parser(input).parse() == "success"
def test_struct_missing_semicolon_invalid():
    input = """
    struct A {
        int x
    };
    """
    assert Parser(input).parse() == "Error on line 4 col 4: }"
def test_struct_member_is_struct_type_ok():
    input = """
    struct A {
        int x;
    };

    struct B {
        A a;
        A b;
    };
    """
    assert Parser(input).parse() == "success"
def test_struct_only_struct_members():
    input = """
    struct A {
    };

    struct B {
        A a;
    };
    """
    assert Parser(input).parse() == "success"
def test_big_program_complex_valid():
    input = """
    struct Point {
        int x;
        int y;
    };

    struct Rect {
        Point topLeft;
        Point bottomRight;
    };

    // inferred return type = int
    add(int a, int b) {
        return a + b;
    }

    // inferred return type = float
    area(Rect r) {
        auto width = r.bottomRight.x - r.topLeft.x;
        auto height = r.topLeft.y - r.bottomRight.y;
        return width * height;
    }

    // explicit void
    printPoint(Point p) {
        printInt(p.x);
        printInt(p.y);
    }

    int max(int a, int b) {
        if (a > b) {
            return a;
        }
        return b;
    }

    void main() {
        Point p1;
        Point p2;
        Rect rect;

        p1.x = 0;
        p1.y = 10;

        p2.x = 10;
        p2.y = 0;

        rect.topLeft = p1;
        rect.bottomRight = p2;

        auto s = add(3, 5);
        auto m = max(7, s);
        auto a = area(rect);

        printInt(s);
        printInt(m);
        printInt(a);

        printPoint(p1);
        printPoint(p2);
    }
    """
    assert Parser(input).parse() == "success"
def test_function_and_inferred_return_and_main():
    input = """
    struct Point {
        int x;
        int y;
    };

    add(int a, int b) {
        return a + b;
    }

    multiply(float a, float b) {
        return a * b;
    }

    void main() {
        auto s = add(1, 2);
        auto p = multiply(2.0, 3.0);
    }
    """
    assert Parser(input).parse() == "success"
def test_invalid_main_has_parameter():
    input = """
    void main(int x) {
    }
    """
    assert Parser(input).parse() == "Error on line 2 col 14: int"
def test_invalid_function_overloading():
    input = """
    int add(int x, int y) {
        return x + y;
    }

    float add(float x, float y) {
        return x + y;
    }

    void main() {
    }
    """
    assert Parser(input).parse() == "success"
def test_invalid_no_main():
    input = """
    int add(int x, int y) {
        return x + y;
    }
    """
    assert Parser(input).parse() == "success"
def test_inferenrd_return_type_in_function():
    input = """
    increment(int x) {
        return x + 1;
    }

    void main() {
        auto y = increment(5);
    }
    """
    assert Parser(input).parse() == "success"
def test_invalid_type():
    input = "int 3.14;"
    assert Parser(input).parse() == "Error on line 1 col 4: 3.14"
def test_invalid_type_2():
    input = "float a = 3.14 + 2;"
    assert Parser(input).parse() == "success"
def test_invalid_variable_name():
    input = "void main() { int 1var; }"
    assert Parser(input).parse() == "Error on line 1 col 18: 1"
def test_invalid_variable_type_2():
    input = "3.141592653589793 || 2.718281828459045;"
    assert Parser(input).parse() == "Error on line 1 col 0: 3.141592653589793"
def test_void_func():
    input = """
    void doNothing() {
        return;
    }

    void main() {
        doNothing();
    }
    """
    assert Parser(input).parse() == "success"
def test_invalid_return_in_void_func():
    input = """
    void doSomething() {
        return 5;
    }

    void main() {
        doSomething();
    }
    """
    assert Parser(input).parse() == "success"
def test_auto_use_before_assign():
    input = """
    void main() {
        auto a;
        printInt(a);
    }
    """
    # Parser OK, semantic phải lỗi
    assert Parser(input).parse() == "success"
def test_auto_first_assign_int():
    input = """
    void main() {
        auto a;
        a = 10;
        a = 20;
    }
    """
    assert Parser(input).parse() == "success"
def test_auto_first_assign_float():
    input = """
    void main() {
        auto a;
        a = 3.14;
        a = 2.71;
    }
    """
    assert Parser(input).parse() == "success"
def test_auto_reassign_different_type():
    input = """
    void main() {
        auto a;
        a = 10;
        a = 3.14;   // type conflict
    }
    """
    assert Parser(input).parse() == "success"
def test_auto_init_then_wrong_type():
    input = """
    void main() {
        auto a = 10;
        a = 3.14;   // semantic error
    }
    """
    assert Parser(input).parse() == "success"
def test_auto_init_expr_promotion():
    input = """
    void main() {
        auto a = 10;
        auto b = 3.14;
        auto c = a + b;   // float
    }
    """
    assert Parser(input).parse() == "success"
def test_auto_init_from_func_return():
    input = """
    int foo() {
        return 10;
    }

    void main() {
        auto a = foo();
    }
    """
    assert Parser(input).parse() == "success"
def test_auto_assign_from_func_return():
    input = """
    int foo() {
        return 10;
    }

    void main() {
        auto a;
        a = foo();
    }
    """
    assert Parser(input).parse() == "success"
def test_auto_used_in_expr_before_assign():
    input = """
    void main() {
        auto a;
        auto b = a + 1;   // a chưa có type
    }
    """
    assert Parser(input).parse() == "success"
def test_auto_shadowing_inner_scope():
    input = """
    void main() {
        auto a = 10;
        {
            auto a = 3.14;
        }
    }
    """
    assert Parser(input).parse() == "success"
def test_auto_never_assigned():
    input = """
    void main() {
        auto a;
    }
    """
    assert Parser(input).parse() == "success"
def test_member_access_postfix_inc():
    input = """
    struct Point { int x; };

    void main() {
        Point p;
        p.x++;
    }
    """
    assert Parser(input).parse() == "success"
def test_chained_member_postfix():
    input = """
    struct A { int x; };
    struct B { A a; };

    void main() {
        B b;
        b.a.x++;
    }
    """
    assert Parser(input).parse() == "success"
def test_postfix_then_member_invalid():
    input = """
    void main() {
        a++.b;
    }
    """
    # Parser có thể accept hoặc reject tùy grammar
    # Nhưng về logic, a++ là rvalue, không thể .b
    assert Parser(input).parse() == "success"
def test_call_member_postfix():
    input = """
    struct A { int x; };
    A foo() { A a; return a; }

    void main() {
        foo().x++;
    }
    """
    assert Parser(input).parse() == "success"
def test_multiple():
    input = """
    struct A { int x; };
    struct B { A a; };
    A foo() { A a; return a; }

    void main() {
        B b;
        foo().x++;
        b.a.x++;
        auto v = b.a.x + foo().x;
    }
    """
    assert Parser(input).parse() == "success"
def test_multiple2():
    input = "int a,b,c = 2;"
    assert Parser(input).parse() == "success"
def test_multiple3():
    input = "float x = 2.0; x = y = z"
    assert Parser(input).parse() == "success"
def test_double_postfix_inc():
    input = """
    void main() {
        a++;
        a--;
    }
    """
    assert Parser(input).parse() == "success"
def test_member_call_inc():
    input = """
    struct A { int x; };
    A getA() { A a; return a; }

    void main() {
        getA().x++;
    }
    """
    assert Parser(input).parse() == "success"
def test_deep_chain_postfix():
    input = """
    struct A { int x; };
    struct B { A a; };
    struct C { B b; };

    void main() {
        C c;
        c.b.a.x++;
    }
    """
    assert Parser(input).parse() == "success"
def test_chained_calls_and_member():
    input = """
    struct A { int x; };
    A foo() { A a; return a; }
    A bar() { A a; return a; }

    void main() {
        foo().x = bar().x;
    }
    """
    assert Parser(input).parse() == "success"
def test_postfix_in_expression():
    input = """
    void main() {
        a = b++ + c;
    }
    """
    assert Parser(input).parse() == "success"
def test_parenthesized_postfix():
    input = """
    void main() {
        (a).x++;
    }
    """
    assert Parser(input).parse() == "success"
def test_prefix_then_member():
    input = """
    void main() {
        ++a;
        a.x = 1;
    }
    """
    assert Parser(input).parse() == "success"
def test_call_postfix_member():
    input = """
    struct A { int x; };
    A foo() { A a; return a; }

    void main() {
        foo().x++;
    }
    """
    assert Parser(input).parse() == "success"