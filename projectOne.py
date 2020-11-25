import sys

import ply.lex as lex

tokens = (
    'K_FOREACH',
    'K_PRINT',
    'K_WHILE',
    'K_REPEAT',
    'K_UNTIL',
    'K_BEGIN',
    'K_END',
    'K_DECLARE',
    'K_IF',
    'K_THEN',
    'K_MAIN',
    'K_INTEGER',
    'K_FLOAT',
    'OP_ASSIGN',
    'OP_ADD',
    'OP_SUB',
    'OP_MUL',
    'OP_DIV',
    'OP_LT',
    'OP_GT',
    'OP_LEQ',
    'OP_GEQ',
    'OP_EQ',
    'OP_DIFF',
    'CAR_A',
    'CAR_B',
    'CAR_C',
    'CAR_AB',
    'T_ID',
    'L_INTEGER',
    'L_FLOAT',
    'L_SEMICOLON',
    # based on what I've read on PLY, including semicolon as a token makes things a lot easier compare to in C.
    'T_EOF'
)

tokenNum = {
    'K_FOREACH': 200,
    'K_PRINT': 201,
    'K_WHILE': 202,
    'K_REPEAT': 203,
    'K_UNTIL': 204,
    'K_BEGIN': 205,
    'K_END': 206,
    'K_DECLARE': 209,
    'K_IF': 210,
    'K_THEN': 211,
    'K_MAIN': 212,
    'K_INTEGER': 213,
    'K_FLOAT': 214,
    'OP_ASSIGN': 220,
    'OP_ADD': 221,
    'OP_SUB': 222,
    'OP_MUL': 223,
    'OP_DIV': 224,
    'OP_LT': 225,
    'OP_GT': 226,
    'OP_LEQ': 227,
    'OP_GEQ': 228,
    'OP_EQ': 229,
    'OP_DIFF': 230,
    'CAR_A': 400,
    'CAR_B': 401,
    'CAR_C': 402,
    'CAR_AB': 403,
    'T_ID': 240,
    'L_INTEGER': 241,
    'L_FLOAT': 242,
    'T_EOF': 280,

}

t_L_SEMICOLON = r';'
t_OP_ADD = r'\+'
t_OP_SUB = r'-'
t_OP_MUL = r'\*'
t_OP_DIV = r'/'
t_OP_LEQ = r'<='
t_OP_GEQ = r'>='
t_OP_EQ = r'=='
t_OP_DIFF = r'!='
t_OP_LT = r'<'
t_OP_GT = r'>'
t_K_MAIN = r'main'
t_K_INTEGER = r'integer'
t_K_FLOAT = r'float'
t_K_FOREACH = r'foreach'
t_K_BEGIN = r'begin'
t_K_END = r'end'
t_K_REPEAT = r'repeat'
t_K_UNTIL = r'until'
t_K_WHILE = r'while'
t_K_DECLARE = r'declare'
t_K_IF = r'if'
t_K_THEN = r'then'
t_K_PRINT = r'print'
t_L_INTEGER = r'\d+'
t_T_ID = r'(_|[a-z])(_|[a-z]|[0-9])(_|[a-z]|[0-9])+'
t_L_FLOAT = r'(\+|-)*[0-9]+\.[0-9]+'
t_T_EOF = r'<<EOF>>'

t_OP_ASSIGN = r'='


def t_error(t):
    t.lexer.skip(1)


lexer = lex.lex()
for line in sys.stdin:
    lexer.input(line)
    tok = lexer.token()
    while tok:
        if not tok:
            break
        print('token = %d' % tokenNum[tok.type])
        tok = lexer.token()

