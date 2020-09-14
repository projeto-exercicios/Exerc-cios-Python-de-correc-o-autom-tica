
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
add_changeable('135') # seed
add_changeable('a')      # the list
add_changeable('b')      # the filtered list
add_changeable('c')      # the list of merge result of filtered list
add_changeable('d')      # the list of merge result
add_changeable('e')      # the list of c intervals
add_changeable('i')      # the loop variable. this was added after an
                         # error ocurred. see ERROR below
add_changeable('13')     # the list length
add_changeable('3')      # the list length
add_changeable('9')      # the list length
add_changeable('18')     # the list length

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
a  = None
b = None
c = None
d = None
e = None
_5 = None





def make_transformations():

    ''
    global a
    global b
    global c
    global d
    global e
    global _5
    
    # question
    _135 = str(randint(1000000, 2000000))
    [a, b, c, d, e, i] = sample(string.ascii_lowercase, 6)
    _13 = randint(19000, 20000)
    _3  = randint(1, 500)
    _9  = randint(500, 1000)
    _18 = _9 * 2
    
    change_all_occurrences('135', _135)
    change_token_all_occurrences('a', a)
    change_token_all_occurrences('b', b)
    change_token_all_occurrences('c', c)
    change_token_all_occurrences('d', d)
    change_token_all_occurrences('e', e)
    change_token_all_occurrences('i', i)
    change_all_occurrences('13', str(_13))
    change_all_occurrences('3', str(_3))
    change_all_occurrences('9', str(_9))
    change_all_occurrences('18', str(_18))

    # answers
    change_all_occurrences(r'\verb+a+', r'\verb+' + a + '+')
    change_all_occurrences(r'\verb+c+', r'\verb+' + c + '+')
    change_all_occurrences(r'\verb+d+', r'\verb+' + d + '+')
    
    # indexes with no repetitions
    [_5] = sample(range(_13), 1)

    change_all_occurrences(r'\verb+5+', r'\verb+' + str(_5) + '+')

    



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global a
    global b
    global c
    global d
    global e
    global _5


    the_list_a = program.get_global(a)
    the_list_b = program.get_global(b)
    the_list_c = program.get_global(c)
    the_list_d = program.get_global(d)
    the_list_e = program.get_global(e)

    answer_1_true = len(the_list_c)
    answer_2_true = round(len(the_list_a) / len(the_list_d),2)
    answer_3_true = max(the_list_e)
    answer_4_true = the_list_c[the_list_e.index(max(the_list_e))]
    answer_5_true = the_list_a[_5]
    choosen_index = choose_other(the_list_e.index(max(the_list_e)), the_list_e)
    # true answers
    change_all_occurrences(r'\verb+11+', str(answer_1_true))
    change_all_occurrences(r'\verb+22+', str(answer_2_true))
    change_all_occurrences(r'\verb+33+', str(answer_3_true))
    change_all_occurrences(r'\verb+44+', str(answer_4_true))
    change_all_occurrences(r'\verb+55+', str(answer_5_true))

    # wrong answers
    increment1 = choice([1, -1])
    increment2 = choice([1, -1])
    increment3 = choice([1, -1])
    increment4 = choice([1, -1])
    increment5 = choice([1, -1])

    answer_1_false = answer_1_true + increment1
    answer_2_false = answer_2_true + increment2
    answer_3_false = the_list_e[choosen_index]
    answer_4_false = the_list_c[choosen_index]
    answer_5_false = the_list_a[_5 + increment5]

    change_all_occurrences(r'\verb+111+', str(answer_1_false))
    change_all_occurrences(r'\verb+222+', str(answer_2_false))
    change_all_occurrences(r'\verb+333+', str(answer_3_false))
    change_all_occurrences(r'\verb+444+', str(answer_4_false))
    change_all_occurrences(r'\verb+555+', str(answer_5_false))
    
def choose_other(the_list_idx, the_list):
    nums = []
    for i in range(len(the_list)):
        if i != the_list_idx:
            nums.append(i)
    return choice(nums)
