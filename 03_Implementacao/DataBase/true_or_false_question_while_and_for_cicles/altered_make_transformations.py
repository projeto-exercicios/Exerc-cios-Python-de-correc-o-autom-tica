
import sys

#sys.path.append(
#    '/home/jbs/develop.old/articles/201509_python_exercises_generator')

#sys.path.append('/home/jbs/develop/201902_questions_transformer')
sys.path.append('../qom_questions_transformer')

import string
from random import sample
from random import choice
from random import randint
from random import shuffle

from text_transformer.tt_text_transformer_interface import add_changeable
#from text_transformer.tt_text_transformer_interface import change_all_occurrences
from text_transformer.tt_text_transformer_interface import change_one_occurrence

# # this import removes an import error. I don't know why (jbs
# # 2018/12/12). see pt_import_tests.py and try to correct the problem.
# import py_transformer.ast_processor

# from python_transformer.pt_python_transformer_interface import change_identifier_all_occurrences
# from python_transformer.pt_python_transformer_interface import change_all_occurrences_in_strings
from python_transformer.pt_python_transformer_interface import change_token_all_occurrences
from python_transformer.pt_python_transformer_interface import change_all_occurrences

#from sympy import latex, sympify




# in the question (program)
add_changeable('135')    # seed
add_changeable('a')      # function atribute     
add_changeable('c')
add_changeable('counter')# global variable
add_changeable('d')      # global list
add_changeable('3')
add_changeable('5')      # range in print_indexes function
add_changeable('6')      # counter number
add_changeable('15')     # range in for_cicle function


# answers list name
add_changeable(r'\verb+a+')
add_changeable(r'\verb+c+')
add_changeable(r'\verb+d+')
# answers (indexes)
add_changeable(r'\verb+1+')
add_changeable(r'\verb+2+')
add_changeable(r'\verb+3+')
add_changeable(r'\verb+4+')
add_changeable(r'\verb+5+')


# right answers values
add_changeable(r'\verb+11+')
add_changeable(r'\verb+22+')
add_changeable(r'\verb+33+')
add_changeable(r'\verb+44+')
add_changeable(r'\verb+55+')

# wrong answers values
add_changeable(r'\verb+111+')
add_changeable(r'\verb+222+')
add_changeable(r'\verb+333+')
add_changeable(r'\verb+444+')
add_changeable(r'\verb+555+')





# variáveis partilhas entre as funções make_transformations e
# make_transformations_on_results
counter = None
d = None
_1 = None
_2 = None
_3 = None
_4 = None
_5 = None





def make_transformations():
    ''
    global counter
    global d
    global _1
    global _2
    global _3
    global _4
    global _5
    

    _135 = str(randint(1000000, 2000000))

    [a, counter, c, d] = sample(string.ascii_lowercase, 4)
    _1 = randint(10, 80)
    _5 = randint(50, 100)
    _6 = randint(19000, 20000)
    _15 = randint(200, 500)
    

    
    change_all_occurrences('135',"<b><i>" +  _135+ "</b></i>")
    change_token_all_occurrences('a',"<b><i>" +  a+ "</b></i>")
    change_token_all_occurrences('counter',"<b><i>" +  counter+ "</b></i>")
    change_token_all_occurrences('c',"<b><i>" +  c+ "</b></i>")
    change_token_all_occurrences('d',"<b><i>" +  d+ "</b></i>")
    change_token_all_occurrences('3',"<b><i>" +  str(_1)+ "</b></i>")
    change_all_occurrences('5',"<b><i>" +  str(_5)+ "</b></i>")
    change_all_occurrences('6',"<b><i>" +  str(_6)+ "</b></i>")
    change_all_occurrences('15',"<b><i>" +  str(_15)+ "</b></i>")


    change_all_occurrences(r'\verb+a+',"<b><i>" +  r'\verb+' + a + '+'+ "</b></i>")
    change_all_occurrences(r'\verb+c+',"<b><i>" +  r'\verb+' + c + '+'+ "</b></i>")
    change_all_occurrences(r'\verb+d+',"<b><i>" +  r'\verb+' + d + '+'+ "</b></i>")
    
    _2, decision1 = decision_function()
    _3, decision2 = decision_function_2()
    change_all_occurrences(r'\verb+2+',"<b><i>" +  r'\verb+' + decision1 + '+'+ "</b></i>")
    change_all_occurrences(r'\verb+3+',"<b><i>" +  r'\verb+' + decision2 + '+'+ "</b></i>")
    change_all_occurrences(r'\verb+5+',"<b><i>" +  r'\verb+' + counter + '+'+ "</b></i>")

    

    



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global counter
    global d
    global _1
    global _2
    global _3
    global _4
    global _5


    the_list = program.get_global(d)
    answer_1_true = _1
    answer_2_true = the_list[:3] if _2 == 3 else the_list[-3:]
    answer_3_true = 0 if _3 == 1 else _5 - 1
    answer_5_true = program.get_global(counter)

    # true answers
    change_all_occurrences(r'\verb+11+',"<b><i>" +  str(answer_1_true)+ "</b></i>")
    change_all_occurrences(r'\verb+22+',"<b><i>" +  str(answer_2_true)+ "</b></i>")
    change_all_occurrences(r'\verb+33+',"<b><i>" +  str(answer_3_true)+ "</b></i>")
    change_all_occurrences(r'\verb+55+',"<b><i>" +  str(answer_5_true)+ "</b></i>")

    # wrong answers
    increment1 = choice([1, -1])
    increment5 = choice([1, -1])

    answer_1_false = answer_1_true + increment1
    answer_2_false = the_list[-3:] if _2 == 3 else the_list[:3]
    answer_3_false = answer_3_true + 1
    answer_5_false = 0

    change_all_occurrences(r'\verb+111+',"<b><i>" +  str(answer_1_false)+ "</b></i>")
    change_all_occurrences(r'\verb+222+',"<b><i>" +  str(answer_2_false)+ "</b></i>")
    change_all_occurrences(r'\verb+333+',"<b><i>" +  str(answer_3_false)+ "</b></i>")
    change_all_occurrences(r'\verb+555+',"<b><i>" +  str(answer_5_false)+ "</b></i>")
    

def decision_function():
    arr_indexes = choice((3, -3))
    if arr_indexes == -3:
        return arr_indexes, "ultimos"
    return arr_indexes, "primeiros"

def decision_function_2():
    arr_indexes = choice((1, -1))
    if arr_indexes == -1:
        return arr_indexes, "ultimo"
    return arr_indexes, "primeiro"

