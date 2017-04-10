import ply.yacc as yacc
import plyLex
import sys

class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    PURPLE = '\033[35m'

tokens=plyLex.tokens
parseTree=()
icg=[]
tempCount=1
currTemp=""
labelCount=1
labels=[]

def innerMost(x):
    f=1
    while(f==1):
        if type(x)==tuple:
            x=x[-1]
        else:
            f=0
    return x

def p_error(p):
    print bcolors.RED+"Something went wrong"+bcolors.WHITE
    print bcolors.RED+"Error at "+str(p.lineno)+bcolors.WHITE
    exit()

def p_start(p):
    '''start : assign 
             | fLoop stmt 
             | fLoop stmt start
             | assign start
             | assign fLoop start
             | stmt'''
    if len(p)==2:
        p[0]=('START',p[1])
    elif len(p)==3:
        p[0]=('START',p[1],p[2])
    else:
        p[0]=('START',p[1],p[2],p[3])      
    global parseTree
    parseTree = p[0]

def p_stmt(p): 
    '''stmt : PRINT VAR'''
    p[0]="STATEMENT "
    global icg
    global labels
    if len(labels)>1:
        icg.append("goto "+labels[-1])
        labels=labels[0:-1]
        icg.append(labels[-1]+":")
        labels=labels[0:-1]
    icg.append(" STMT ")


def p_assign(p):
    '''assign : factor EQUAL expr '''
    p[0]=('ASSIGN',p[1],"=",p[3])
    global currTemp
    if not currTemp:
        global icg
        icg.append(innerMost(p[1])+"="+str(innerMost(p[3])))
    else:
        global icg
        icg.append(str(innerMost(p[1]))+"="+str(currTemp))
    global tempCount
    currTemp="t"+str(tempCount)
    tempCount = tempCount +1 

def p_expr(p):
    '''expr : expr PLUS term
            | expr MINUS term
            | term '''
    if len(p)>2 and p[2]=="+":
        global currTemp
        if not currTemp:
            global icg
            icg.append("t"+str(tempCount)+"="+str(innerMost(p[1]))+"+"+str(innerMost(p[3])))
        else:
            if(type(innerMost(p[1]))==int):
                icg.append("t"+str(tempCount)+"="+str(innerMost(p[1]))+"+"+str(currTemp))
            else:
                icg.append("t"+str(tempCount)+"="+str(currTemp)+"+"+str(innerMost(p[3])))
        global tempCount
        currTemp="t"+str(tempCount)
        tempCount = tempCount +1
        p[0]=('ADD',p[1],p[3])
    elif len(p)>2 and p[2]=="-":
        global currTemp
        global icg
        if not currTemp:
            icg.append("t"+str(tempCount)+"="+str(innerMost(p[1]))+"-"+str(innerMost(p[3])))
        else:
            if(type(innerMost(p[1]))==int):
                icg.append("t"+str(tempCount)+"="+str(innerMost(p[1]))+"-"+str(currTemp))    
            else:
                icg.append("t"+str(tempCount)+"="+str(currTemp)+"-"+str(innerMost(p[3])))
        global tempCount
        currTemp="t"+str(tempCount)
        tempCount = tempCount +1
        p[0]=('SUB',p[1],p[3])
    else:
        p[0]=("EXPR",p[1])
    

def p_term(p):
    '''term : term MULTIPLY factor
            | term DIVIDE factor
            | factor '''
    if len(p)>2 and p[2]=="*":
        global currTemp
        global icg
        if not currTemp:
            icg.append("t"+str(tempCount)+"="+str(innerMost(p[1]))+"*"+str(innerMost(p[3])))
        else:
            if(type(innerMost(p[1]))==int):
                icg.append("t"+str(tempCount)+"="+str(innerMost(p[1]))+"*"+str(currTemp))    
            else:
                icg.append("t"+str(tempCount)+"="+str(currTemp)+"*"+str(innerMost(p[3])))
        global tempCount
        currTemp="t"+str(tempCount)
        tempCount = tempCount +1
        p[0]=('MUL',p[1],p[3])
    elif len(p)>2 and p[2]=="/":
        global currTemp
        global icg
        if not currTemp:
            icg.append("t"+str(tempCount)+"="+str(innerMost(p[1]))+"/"+str(innerMost(p[3])))
        else:
            if(type(innerMost(p[1]))==int):
                icg.append("t"+str(tempCount)+"="+str(innerMost(p[1]))+"/"+str(currTemp))    
            else:
                icg.append("t"+str(tempCount)+"="+str(currTemp)+"/"+str(innerMost(p[3])))
        global tempCount
        currTemp="t"+str(tempCount)
        tempCount = tempCount +1
        p[0]=('DIVIDE',p[1],p[3])
    else:
        p[0]=("TERM",p[1])
    
def p_factor(p):
    '''factor : VAR
              | NUMBER '''
    
    if type(p[1])==int:
        p[0]=("FACTOR","NUM",p[1])
    else:
        p[0]=("FACTOR","VAR",p[1])
                
def p_fLoop(p):
    '''fLoop : FOR inner'''
    p[0]=('FOR',p[2])
    

def p_inner(p):
    '''inner : PARANOPEN VAR IN rangeSpec PARANCLOSE COLON
             | VAR IN rangeSpec COLON '''
    if len(p)==6:
        p[0]=('INSIDE FOR',p[1],p[2],p[3],p[4],p[5],p[6])
        #global icg
        #icg.append(str(p[2]+"="+innerMost(p[4][3])))
    else:
        p[0]=('INSIDE FOR',p[1],p[2],p[3],p[4]) 
        #global icg
        #icg.append(str(p[1]+"="+str(innerMost(p[3][3]))))


def p_rangeSpec(p):
    '''rangeSpec : RANGE PARANOPEN expr COMMA expr PARANCLOSE '''
    p[0]=('RANGESPEC',p[1],p[2],p[3],p[4],p[5],p[6])
    global icg
    icg.append(str(innerMost(p[-2]))+"="+str(innerMost(p[3])))
    icg.append("L"+str(labelCount)+":")
    global labels
    global labelCount
    labelCount = labelCount + 1
    icg.append("ifFalse "+str(innerMost(p[-2]))+"<"+str(innerMost(p[5]))+" goto L"+str(labelCount))
    labels.append("L"+str(labelCount))
    labels.append("L"+str(labelCount-1))
    labelCount = labelCount + 1

def printParseTree(s):
    tabs=-1
    finalStr=""
    toBeIgnore=[',','\'']
    symbols=['=','+','-','*','/',':']
    for i in range(0,len(s)):
        if s[i]=="(":
            finalStr=finalStr+"\n"
            tabs=tabs+1
            for j in range(0, tabs):
                finalStr=finalStr+bcolors.WHITE+"---"
        elif s[i]==")":
            tabs=tabs-1
            finalStr=finalStr+"\n"
        else:
            if s[i] not in toBeIgnore:
                if s[i] in symbols:
                    for j in range(0, tabs):
                        finalStr=finalStr+bcolors.WHITE+"---"
                    finalStr=finalStr+"  "+bcolors.PURPLE+s[i]+bcolors.WHITE
                else:
                    finalStr=finalStr+bcolors.PURPLE+s[i]+bcolors.WHITE
                if s[i]=="T" and s[i-1]=="N":
                    finalStr=finalStr+"\n"
    return finalStr


parser = yacc.yacc()

f = open(sys.argv[1])
data = f.read()

res = yacc.parse(data)
print bcolors.GREEN+"PARSE TREE"+bcolors.WHITE
print parseTree
print "\n"
print printParseTree(str(parseTree))


print "\n\n"
print bcolors.GREEN+"ICG "+bcolors.WHITE
#print icg

for i in icg:
    print i
print "\n"
#parseTreeData =  str(compiler.parse(data))
#print parseTreeData 
#genParseTree.disp(parseTreeData)