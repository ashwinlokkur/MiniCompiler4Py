import ply.lex as lex
import re
#import ply.yacc as yacc

tokens = ['NAME','VAR','NUMBER','ID','PLUS','MINUS','MULTIPLY','DIVIDE','COMMA','COLON','PARANOPEN','PARANCLOSE','FLOWEROPEN','FLOWERCLOSE','EQUAL','GREATER','LESSER','GREATEREQ','LESSEREQ','EQEQ','NOTEQ','AND','OR']
reserved = {'if':'IF','in':'IN','for':'FOR','range':'RANGE','xrange':'XRANGE','print':'PRINT'}

tokens = tokens + list(reserved.values())

t_ignore=' '
t_ignore_COMMENT=r'[#].* | \'\'\'.*\'\'\''
t_PLUS=r'\+'
t_MINUS=r'\-'
t_MULTIPLY=r'\*'
t_DIVIDE=r'/'
t_EQUAL=r'='
t_COMMA=r','
t_COLON=r':'
t_PARANOPEN=r'\('
t_PARANCLOSE=r'\)'
t_FLOWEROPEN=r'{'
t_FLOWERCLOSE=r'}'
t_GREATER=r'>'
t_LESSER=r'<'
t_GREATEREQ=r'>='
t_LESSEREQ=r'<='
t_EQEQ=r'=='
t_NOTEQ=r'!='
t_AND=r'&&'
t_OR=r'\|\|'

def t_error(t):
    #print "ERROR"
    t.lexer.skip(1)

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type=reserved[t.value]
    else:
        t.type="VAR"
    return t       
'''
def t_COMMENT(t):
    r'[#].*'
    t.lexer.skip(1)
'''
lexer = lex.lex()

'''
f = open('inputFile.py')
data = f.read()

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok) '''
