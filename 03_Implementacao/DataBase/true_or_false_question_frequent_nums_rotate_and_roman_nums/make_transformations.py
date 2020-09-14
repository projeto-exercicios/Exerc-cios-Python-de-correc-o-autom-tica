
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
add_changeable('k')      # index where to rotate list
add_changeable('n')      # the loop variable. this was added after an
                         # error ocurred. see ERROR below
add_changeable('13')     # the list length
add_changeable('33')      # min num value
add_changeable('66')      # max num value

# answers list name
add_changeable(r'\verb+a+')
add_changeable(r'\verb+k+')
add_changeable(r'\verb+k_val+')
add_changeable(r'\verb+dist+')

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
list_distance = None
wtc = None




def make_transformations():

    ''
    global a
    global _1
    global _2
    global _3
    global _4
    global _5
    global list_distance
    global wtc
    
    # question
    _135 = str(randint(1000000, 2000000))
    [a, n, k] = sample(string.ascii_lowercase, 3)
    _13 = randint(19000, 20000)
    _33  = randint(1, 500)
    _66  = randint(500, 1000)
    
    change_all_occurrences('135', _135)
    change_token_all_occurrences('a', a)
    change_token_all_occurrences('n', n)
    change_token_all_occurrences('k', k)

    change_all_occurrences('13', str(_13))
    change_all_occurrences('33', str(_33))
    change_all_occurrences('66', str(_66))

    list_distance = choice((3, 4, 5, 6, 7))
    _5 = choice(range(_13 - list_distance))
    wtc = choice(range(list_distance))
    if wtc == 0:
        wtc += choice((1,2))
    if wtc == list_distance:
        wtc -= choice((1,2))
    
    # answers
    change_all_occurrences(r'\verb+a+', r'\verb+' + a + '+')
    
    # indexes with no repetitions
    [_1, _4, _5] = sample(range(_13), 3)
    
    change_all_occurrences(r'\verb+1+', r'\verb+' + str(_1) + '+')
    change_all_occurrences(r'\verb+4+', r'\verb+' + str(_4) + '+')
    change_all_occurrences(r'\verb+5+', r'\verb+' + str(_5) + '+')

    #alinea 5
    change_all_occurrences(r'\verb+k+', r'\verb+' + k + '+')
    change_all_occurrences(r'\verb+dist+', r'\verb+' + str(list_distance) + '+')
    change_all_occurrences(r'\verb+k_val+', r'\verb+' + str(wtc) + '+')

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
    global list_distance
    global wtc

    the_list = program.get_global(a)
    mst_freq = program.get_global("mst_freq")
    lst_freq = program.get_global("lst_freq")
    nums = the_list[_5: _5 + list_distance]

    answer_1_true = the_list[_1]
    answer_2_true = mst_freq
    answer_3_true = lst_freq
    answer_4_true = int_to_roman(the_list[_4])
    answer_5_true = nums[wtc:] + nums[:wtc]

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
    answer_3_false = answer_3_true + increment3
    answer_4_false = int_to_roman(the_list[_4 + increment2])
    answer_5_false = change_random_num(list_distance, nums[wtc:] + nums[:wtc])

    change_all_occurrences(r'\verb+111+', str(answer_1_false))
    change_all_occurrences(r'\verb+222+', str(answer_2_false))
    change_all_occurrences(r'\verb+333+', str(answer_3_false))
    change_all_occurrences(r'\verb+444+', str(answer_4_false))
    change_all_occurrences(r'\verb+555+', str(answer_5_false))



def change_random_num(list_dist, nums):
    idx = choice(range(list_dist))
    nums[idx] = nums[idx] + choice((-1, 1))
    return nums


def int_to_roman(num):
    num = abs(num)
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    idx = 0
    while  num > 0:
        for _ in range(num // val[idx]):
            roman_num += syb[idx]
            num -= val[idx]
        idx += 1
    return roman_num
