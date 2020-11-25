import ply.lex as lex

tokens = (
    'T_ID',
    'T_NUM',
    'T_ADD',
    'T_SUB',
    'T_MUL',
    'T_DIV',
    'T_LT',
    'T_GT',
    'T_LEQ',
    'T_GEQ',
    'T_EQ',
    'T_NEQ',
    'T_AND',
    'T_OR',
    'T_READ',
    'T_WRITE',
    'T_ASSIGN',
    'T_BEGIN',
    'T_END',
    'T_FOREACH',
    'T_IN',
    'T_REPEAT',
    'T_UNTIL',
    'T_WHILE',
    'T_IF',
    'T_THEN',
    'T_ELSE',
    'T_DECLARE',
    'T_INTEGER',
    'T_FLOAT',
    'T_LITERAL_STR',
)
literals = [';', '(', ')', ':', ',', '[', ']']

t_T_LITERAL_STR = '\".+\"'
t_T_ASSIGN = ':='
t_T_ADD = '\+'
t_T_SUB = '-'
t_T_MUL = '\*'
t_T_DIV = '/'
t_T_LT = '<'
t_T_GT = '>'
t_T_GEQ = '>='
t_T_LEQ = '<='
t_T_EQ = '='
t_T_NEQ = '<>'
def t_T_AND(t): r'and'; return t #We need to declare reserved words as functions to avoid issues with PLY's order of RegEx evaluation. Otherwise all reserved words would be evalulated as IDs before they are evaluated as their own regex
def t_T_OR(t): r'or'; return t
def t_T_FOREACH(t): r'foreach'; return t
def t_T_IN(t): 'in'; return t
def t_T_WHILE(t): r'while'; return t
def t_T_BEGIN(t): r'begin'; return t
def t_T_END(t): r'end'; return t
def t_T_IF(t): r'if'; return t
def t_T_THEN(t): r'then'; return t
def t_T_ELSE(t): r'else'; return t
def t_T_WRITE(t): r'write'; return t
def t_T_READ(t): r'read'; return t
def t_T_INTEGER(t): r'int'; return t
def t_T_FLOAT(t): r'float'; return t
def t_T_REPEAT(t): r'repeat'; return t
def t_T_UNTIL(t): r'until'; return t
def t_T_DECLARE(t): r'declare'; return t
t_T_NUM = '\d+\.\d+|\d+'
t_T_ID = '([a-zA-Z]|_)([a-zA-Z]|\d|_)*'
t_ignore = ' \n \t'




def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
