
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
add_changeable('a')      # the list
add_changeable('n')      # the loop variable
add_changeable('i')      # the loop variable
add_changeable('__var')  # class's global variable
add_changeable('P')      # class name
add_changeable('p')      # class variable
add_changeable('13')     # the list length
add_changeable('33')     # the list length
add_changeable('3')      # the list length

# answers class name
add_changeable(r'\verb+classP+')
add_changeable(r'\verb+classp+')

# answers list name
add_changeable(r'\verb+a+')

# answers (indexes)
add_changeable(r'\verb+1+')
add_changeable(r'\verb+2_1+')
add_changeable(r'\verb+2_2+')
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
a  = None
_1 = None
_2_1 = None
_2_2 = None
__var = None
var = None
P = None
p = None






def make_transformations():

    ''
    global a
    global _1
    global _2_1
    global _2_2
    global __var
    global var
    global P
    global p
    
    # question
    _135 = str(randint(1000000, 2000000))
    [a, n, p, P, var, i] = sample(string.ascii_lowercase, 6)
    _13 = randint(19000, 20000)
    _3 = randint(-50, 5)
    _33 = randint(5, 1500)
    __var = '__' + var
    P = P.upper()
    
    change_all_occurrences('135', _135)
    change_token_all_occurrences('a', a)
    change_token_all_occurrences('P', P)
    change_token_all_occurrences('__var', __var)
    change_token_all_occurrences('p', p)
    change_token_all_occurrences('i', i)
    change_token_all_occurrences('n', n)
    change_all_occurrences('13', str(_13))
    change_all_occurrences('3', str(_3))
    change_all_occurrences('33', str(_33))

    # answers
    change_all_occurrences(r'\verb+a+', r'\verb+' + a + '+')
    change_all_occurrences(r'\verb+classp+', r'\verb+' + p + '+')
    change_all_occurrences(r'\verb+classP+', r'\verb+' + P + '+')
    
    # indexes with no repetitions
    [_1, _2_1, _2_2] = sample(range(_13), 3)

    change_all_occurrences(r'\verb+1+', r'\verb+' + str(_1) + '+')
    change_all_occurrences(r'\verb+2_1+', r'\verb+' + str(_2_1) + '+')
    change_all_occurrences(r'\verb+2_2+', r'\verb+' + str(_2_2) + '+')
    change_all_occurrences(r'\verb+3+', r'\verb+' + __var + '+')
    

    



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global a
    global _1
    global _2_1
    global _2_2
    global __var
    global var
    global P
    global p
    

    the_list = program.get_global(a)
    #correct index for question 5
    _5 = choose_correct_idx_5(the_list)
    change_all_occurrences(r'\verb+5+', r'\verb+' + str(_5) + '+')
    

    answer_1_true = 1
    p1 = the_list[_2_1].num
    p2 = the_list[_2_2].num
    if p2 == 0 or ( (p1 / p2) % 2 == 0 ):
        answer_2_true = 3
    else:
        answer_2_true = 4
    answer_3_true = p + '.\_' + P + '\_\_' + var
    answer_4_true = 0
    answer_5_true = factorial(the_list[_5].num)

    # true answers
    change_all_occurrences(r'\verb+11+', str(answer_1_true))
    change_all_occurrences(r'\verb+22+', str(answer_2_true))
    change_all_occurrences(r'\verb+33+', answer_3_true)
    change_all_occurrences(r'\verb+44+', str(answer_4_true))
    change_all_occurrences(r'\verb+55+', str(answer_5_true))

    # wrong answers
    increment2 = choice([1, -1])
    increment3 = choice([1, -1])
    increment4 = choice([1, -1])
    increment5 = choice([1, -1])

    answer_1_false = _1
    if p2 == 0 or ( (p1 / p2) % 2 == 0 ):
        answer_2_false = 4
    else:
        answer_2_false = 3
    wrong_answer_3 = choice((p + '.' + '\_\_' + var,
                             P + '.' + '\_\_' + var,
                             p + '.\_' + P + '\_' + var,
                             P + '.' + var , p + '.' + var))
    answer_3_false = wrong_answer_3
    wrong_answer_4 = choice(('Undifined', 'None', 'Null'))
    answer_4_false = wrong_answer_4
    answer_5_false = answer_5_true + increment5

    change_all_occurrences(r'\verb+111+', str(answer_1_false))
    change_all_occurrences(r'\verb+222+', str(answer_2_false))
    change_all_occurrences(r'\verb+333+', answer_3_false)
    change_all_occurrences(r'\verb+444+', answer_4_false)
    change_all_occurrences(r'\verb+555+', str(answer_5_false))


def choose_correct_idx_5(the_list):
    for i in range(len(the_list)):
        num = the_list[i].num
        if num > 1 and num < 11:
            return i
    return 0

def factorial(num):
    if num == 1: return 1
    else: return num * factorial(num - 1)
