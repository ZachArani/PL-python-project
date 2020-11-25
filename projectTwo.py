import sys

import ply.yacc as yacc
import ply.lex as lex
from projectTwoLexer import tokens
import fileinput

def p_program(p):
    '''program : stmt_list ';' '''


def p_stmt_list(p):
    '''stmt_list : stmt_list ';' stmt
                 | stmt'''



def p_stmt(p):
    '''stmt : assignment
            | read
            | write
            | while
            | repeat
            | block
            | foreach
            | if_stmt'''



def p_block(p):
    '''block : T_BEGIN stmt_list T_END'''


def p_foreach(p):
    '''foreach : T_FOREACH varref T_IN '(' a_fact ':' a_fact ')' stmt
           |   T_FOREACH varref T_IN '(' a_fact ':' a_fact ')' T_BEGIN stmt_list T_END '''


def p_while(p):
    '''while : T_WHILE l_expr T_BEGIN stmt_list T_END'''

def p_repeat(p):
    '''repeat : T_REPEAT stmt_list T_UNTIL l_expr'''


def p_if_stmt(p):
    '''if_stmt : T_IF l_expr T_THEN stmt
                | T_IF l_expr T_THEN stmt else_stmt'''


def p_else_stmt(p):
    '''else_stmt : T_ELSE stmt'''


def p_assignment(p):
    '''assignment : varref T_ASSIGN l_expr'''


def p_a_expr(p):
    '''a_expr : a_expr T_ADD a_term
              | a_expr T_SUB a_term
              | a_term'''


def p_a_term(p):
    '''a_term : a_term T_MUL a_fact
              | a_term T_DIV a_fact
              | a_fact'''


def p_a_fact(p):
    '''a_fact : varref
              | T_NUM
              | T_LITERAL_STR
              | T_SUB a_fact
              | '(' a_expr ')' '''


def p_varref(p):
    '''varref : varref '[' a_expr ']'
              | T_ID'''


def p_l_expr(p):
    '''l_expr : l_expr T_AND l_term
              | l_term'''


def p_l_term(p):
    '''l_term : l_term T_OR l_fact
              | l_fact'''


def p_l_fact(p):
    '''l_fact : l_fact oprel a_expr
              | a_expr
              | '(' l_expr ')' '''

def p_oprel(p):
    '''oprel : T_LT
             | T_GT
             | T_LEQ
             | T_GEQ
             | T_EQ
             | T_NEQ'''


def p_read(p):
    '''read : T_READ varlist'''

def p_write(p):
    '''write : T_WRITE expr_list'''


def p_varlist(p):
    '''varlist : varref ',' varlist
               | varref'''


def p_expr_list(p):
    '''expr_list : a_expr ',' expr_list
                 | a_expr'''

def p_error(p):
    raise SyntaxError


parser = yacc.yacc(debug=True)

try:
    s = ''
    #for line in fileinput.input(sys.argv[1]):
    #    s += line
    for line in sys.stdin:
        s += line
except EOFError:
    print("File Read error!")
try:
    result = parser.parse(s)
    print("PASS")
except SyntaxError:
    print("FAIL")
