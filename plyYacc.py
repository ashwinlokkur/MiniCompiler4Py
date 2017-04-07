import ply.yacc as yacc
import plyLex

tokens=plyLex.tokens

def p_error(p):
    print "Something went wrong"
    print p

def p_start(p):
    '''start : assign start
            | fLoop start
            | assign
            | fLoop stmt'''

def p_stmt(p):
    '''stmt : PRINT VAR'''

def p_assign(p):
    '''assign : VAR EQUAL expr '''

def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term '''

def p_term(p):
    '''term : term MULTIPLY factor
            | term DIVIDE factor
            | factor '''

def p_factor(p):
    '''factor : VAR
              | NUMBER '''

def p_fLoop(p):
    '''fLoop : FOR inner'''

def p_inner(p):
    '''inner : PARANOPEN VAR IN rangeSpec PARANCLOSE COLON
             | VAR IN rangeSpec COLON '''

def p_rangeSpec(p):
    '''rangeSpec : RANGE PARANOPEN expr COMMA expr PARANCLOSE
                 | XRANGE PARANOPEN expr PARANCLOSE '''

parser = yacc.yacc()

f = open('inputFile.py')
data = f.read()

yacc.parse(data)