import ply.yacc as yacc
import ply.lex as lex
from lexico import tokens
import SintaxeAbstrata as abstract

def p_exp_soma(p):
    '''exp : exp SOMA exp1
    | exp1'''
    if (len(p) == 2):   # Primeira Regra
        p[0] = p[1]
    else:
        p[0] = abstract.SomaExp(p[1], p[3])

def p_exp1_vezes(p):
    '''exp1 : exp1 VEZES exp2
    | exp2'''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = abstract.MulExp(p[1], p[3])

def p_exp2_exponencial(p):
    '''exp2 : exp3 POT exp2
    | exp3'''
    if(len(p) == 2):
        p[0] = p[1]
    else:
        p[0] = abstract.PotExp(p[1],p[3])
    
def p_exp3(p):
    '''exp3 : call 
        | assign 
        | NUMBER 
        | ID'''
    if (isinstance(p[1], abstract.Call)):
        p[0] = abstract.CallExp(p[1])
    elif(isinstance(p[1], abstract.Assign)):
        p[0] = abstract.AssignExp(p[1])
    elif('NUMBER'):
        p[0] = abstract.NumExp(p[1])
    elif('ID'):
        p[0] = abstract.IDExp(p[1])


def p_call(p):
    '''call : ID LPAREN params RPAREN
        | ID LPAREN RPAREN'''
    if(p[3] == 'RPAREN'):
        p[0] = abstract.SimpleCall(p[1])
    else:
        p[0] = abstract.ParamsCall(p[1], p[3])

def p_params(p):
    '''params : ID COMMA params
    | ID'''
    if(len(p) == 2):
        p[0] = abstract.IDExp(p[1])
    else:
        p[0] = abstract.CompoundParams(p[1], p[3])

def p_assign(p):
    '''assign : ID IGUAL exp'''
    p[0] = abstract.AssignExp(p[1], p[3])

parser = yacc.yacc()

result = parser.parse(debug=True)

visit = abstract.Visitor.Visitor()

result.accept(visit)