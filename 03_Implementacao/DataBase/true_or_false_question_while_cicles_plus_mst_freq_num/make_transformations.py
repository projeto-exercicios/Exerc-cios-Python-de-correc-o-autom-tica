
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
add_changeable('n')      # the loop variable.
add_changeable('c')      # the while loop variable.

add_changeable('13')     # the list length
add_changeable('3')      # num min value
add_changeable('33')     # num max value

# answers list name
add_changeable(r'\verb+a+')

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
a  = None
_1 = None
_2 = None
_3 = None
_4 = None
_5 = None

pt_a = "ã".encode('utf8').decode('iso-8859-1')
pt_e = "é".encode('utf8').decode('iso-8859-1')
pt_nao = 'n' + pt_a + 'o ' + pt_e
pt_impar = "í".encode('utf8').decode('iso-8859-1') + 'mpares'


def make_transformations():

    ''
    global a
    global _1
    global _2
    global _3
    global _4
    global _5
    
    # question
    _135 = str(randint(1000000, 2000000))
    [a, n, c] = sample(string.ascii_lowercase, 3)
    _13 = randint(19000, 20000)
    _3 = randint(0, 5)
    _33 = randint(_3, 500)
    
    change_all_occurrences('135', _135)
    change_token_all_occurrences('a', a)
    change_token_all_occurrences('n', n)
    change_token_all_occurrences('c', c)
    change_all_occurrences('13', str(_13))
    change_all_occurrences('3', str(_3))
    change_all_occurrences('33', str(_33))

    # answers
    change_all_occurrences(r'\verb+a+', r'\verb+' + a + '+')

    _1 = question_1()
    _2 = question_2()
    _3 = randint(_3, _33)
    _4 = choice((pt_impar, 'pares'))
    _5 = 'par' if _4 == pt_impar else pt_impar
    
   
    change_all_occurrences(r'\verb+1+', r'\verb+' + str(_1[0]) + '+')
    change_all_occurrences(r'\verb+2+', r'\verb+' + str(_2[0]) + '+')
    change_all_occurrences(r'\verb+3+', r'\verb+' + str(_3) + '+')
    change_all_occurrences(r'\verb+4+', r'\verb+' + _4 + '+')
    change_all_occurrences(r'\verb+5+', r'\verb+' + _5 + '+')

    



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global a
    global _1
    global _2
    global _3
    global _4
    global _5

    
    the_list = program.get_global(a)
##    print(the_list)
    answer_1_true = _1[1]
    answer_2_true = _2[1]
    answer_3_true = question_3(the_list, _3)
    answer_4_true = question_4(the_list, _4)
    wrong_5, correct_5 = question_5(_5)
    answer_5_true = correct_5

    # true answers
    change_all_occurrences(r'\verb+11+', answer_1_true)
    change_all_occurrences(r'\verb+22+', answer_2_true)
    change_all_occurrences(r'\verb+33+', str(answer_3_true))
    change_all_occurrences(r'\verb+44+', str(answer_4_true))
    change_all_occurrences(r'\verb+55+', str(answer_5_true))


    answer_1_false = pt_e if _1[1] == pt_nao else pt_nao
    answer_2_false = pt_e if _2[1] == pt_nao else pt_nao
    answer_3_false = answer_3_true - 1 if answer_3_true > 0 else answer_3_true + 1
    answer_4_false = question_4(the_list, 'pares') if _4 == pt_impar else question_4(the_list, pt_impar)
    answer_5_false = wrong_5

    change_all_occurrences(r'\verb+111+', answer_1_false)
    change_all_occurrences(r'\verb+222+', answer_2_false)
    change_all_occurrences(r'\verb+333+', str(answer_3_false))
    change_all_occurrences(r'\verb+444+', str(answer_4_false))
    change_all_occurrences(r'\verb+555+', str(answer_5_false))
    

def question_1():
    decision = choice(('exec', 'noexec'))
    if decision == 'exec':
        return choice(('while_1()', 'while_3()')), pt_e
    else:
        return 'while_2()', pt_nao

def question_2():
    decision = choice(('loop', 'noloop'))
    if decision == 'loop':
        return 'while_1()', pt_e
    else:
        return choice(('while_2()', 'while_3()')), pt_nao

def question_3(nums, max_num):
    nums = [x for x in nums if x < max_num]
    if len(nums) == 0:
        return "None"
    else:
        return max(set(nums), key = nums.count)


def question_4(nums, decision):
    if decision == pt_impar:
        return len([x for x in nums if x % 2 != 0 and x != 0])
    else:
        return len([x for x in nums if x % 2 == 0 and x != 0])

def question_5(decision):
    if decision == pt_impar:
        return choice(('len([x for x in nums if x \% 2 != 0])',
                       'len([x for x in nums if x \% 2 != 0 or x == 0])',
                       'len([x for x in nums if x \% 2 != 0 or x != 0])')), 'len([x for x in nums if x \% 2 != 0 and x != 0])'
    else:
        return choice(('len([x for x in nums if x \% 2 == 0 or x == 0])',
                       'len([x for x in nums if x \% 2 == 0 and x == 0])',
                       'len([x for x in nums if x \% 2 == 0 or x != 0])',
                       'len([x for x in nums if x \% 2 == 0]) ')), 'len([x for x in nums if x \% 2 == 0 and x != 0])'






    
