import ply.yacc as yacc
import plyLex
import compiler

tokens=plyLex.tokens

noOfStmt=1

def p_error(p):
    print "Something went wrong"
    print "Error at "+str(p.lineno)+" "+str(p.lexpos)

def p_start(p):
    '''start : assign start
            | fLoop start
            | assign
            | fLoop stmt'''    
    global noOfStmt
    print str(noOfStmt)+" Statements parsed"
    noOfStmt=noOfStmt+1

def p_stmt(p):  #RE-THINK
    '''stmt : PRINT VAR'''

def p_assign(p):
    '''assign : VAR EQUAL expr '''
    p[0]=p[3]
def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term '''
    if len(p)==3:
        p[0]=p[1]+p[3]
    else:
        p[0]=p[1]

def p_term(p):
    '''term : term MULTIPLY factor
            | term DIVIDE factor
            | factor '''
    if len(p)==3:
        p[0]=p[1]+p[3]
    else:
        p[0]=p[1]

def p_factor(p):
    '''factor : VAR
              | NUMBER '''
    p[0]=p[1]
def p_fLoop(p):
    '''fLoop : FOR inner'''
    p[0]=p[2]
def p_inner(p):
    '''inner : PARANOPEN VAR IN rangeSpec PARANCLOSE COLON
             | VAR IN rangeSpec COLON '''
    if len(p)==6:
        p[0]=p[4]
    else:
        p[0]=p[3]
def p_rangeSpec(p):
    '''rangeSpec : RANGE PARANOPEN expr COMMA expr PARANCLOSE
                 | XRANGE PARANOPEN expr PARANCLOSE '''
    if len(p)==6:
        p[0]=p[3]+p[5]
    else:
        p[0]=[3]


parser = yacc.yacc()

f = open('inputFile.py')
data = f.read()

res = yacc.parse(data)
print res
