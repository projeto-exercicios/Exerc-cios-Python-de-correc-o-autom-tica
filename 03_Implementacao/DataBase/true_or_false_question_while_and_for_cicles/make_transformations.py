
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
add_changeable('7')      # counter number
add_changeable('15')     # range in for_cicle function


# answers list name
add_changeable(r'\verb+a+')
add_changeable(r'\verb+c+')
add_changeable(r'\verb+d+')

# answers (indexes)
add_changeable(r'\verb+1_idx+')
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
_7 = None





def make_transformations():
    ''
    global counter
    global d
    global _1
    global _2
    global _3
    global _4
    global _5
    global _7
    

    _135 = str(randint(1000000, 2000000))

    [a, counter, c, d] = sample(string.ascii_lowercase, 4)
    _1 = randint(10, 80)
    _5 = randint(50, 100)
    _7 = randint(19000, 20000)
    _15 = randint(200, 500)
    

    
    change_all_occurrences('135', _135)
    change_token_all_occurrences('a', a)
    change_token_all_occurrences('counter', counter)
    change_token_all_occurrences('c', c)
    change_token_all_occurrences('d', d)
    change_token_all_occurrences('3', str(_1))
    change_all_occurrences('5', str(_5))
    change_all_occurrences('7', str(_7))
    change_all_occurrences('15', str(_15))

    change_all_occurrences(r'\verb+1_idx+', r'\verb+' + str(_1) + '+')

    
    change_all_occurrences(r'\verb+a+', r'\verb+' + a + '+')
    change_all_occurrences(r'\verb+c+', r'\verb+' + c + '+')
    change_all_occurrences(r'\verb+d+', r'\verb+' + d + '+')
    
    _2, decision1 = decision_function()
    _3, decision2 = decision_function_2()
    change_all_occurrences(r'\verb+2+', r'\verb+' + decision1 + '+')
    change_all_occurrences(r'\verb+3+', r'\verb+' + decision2 + '+')
    change_all_occurrences(r'\verb+5+', r'\verb+' + counter + '+')

    

    



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
    change_all_occurrences(r'\verb+11+', str(answer_1_true))
    change_all_occurrences(r'\verb+22+', str(answer_2_true))
    change_all_occurrences(r'\verb+33+', str(answer_3_true))
    change_all_occurrences(r'\verb+55+', str(answer_5_true))

    # wrong answers
    increment1 = choice([1, -1])
    increment5 = choice([1, -1])

    answer_1_false = _7
    answer_2_false = the_list[-3:] if _2 == 3 else the_list[:3]
    answer_3_false = answer_3_true + 1
    answer_5_false = 0

    change_all_occurrences(r'\verb+111+', str(answer_1_false))
    change_all_occurrences(r'\verb+222+', str(answer_2_false))
    change_all_occurrences(r'\verb+333+', str(answer_3_false))
    change_all_occurrences(r'\verb+555+', str(answer_5_false))
    

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
