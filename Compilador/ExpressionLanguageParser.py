import ply.yacc as yacc
import ply.lex as lex
from lexico import tokens

def p_exp_soma(p):
    '''exp : exp SOMA exp1
    | exp1'''

def p_exp1_vezes(p):
    '''exp1 : exp1 VEZES exp2
    | exp2'''

def p_exp2_exponencial(p):
    '''exp2 : exp3 POT exp2
    | exp3'''

def p_exp3(p):
    '''exp3 : call | assign | NUMBER | ID'''

def p_call(p):
    '''call : ID LPAREN params RPAREN
        | ID LPAREN RPAREN'''

def p_params(p):
    '''params : ID COMMA params
    | ID'''

def p_assign(p):
    '''assign : ID IGUAL exp'''

parser = yacc.yacc()

result = parser.parse(debug=True)