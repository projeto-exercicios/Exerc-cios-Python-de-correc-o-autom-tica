
import sys

#sys.path.append(
#    '/home/jbs/develop.old/articles/201509_python_exercises_generator')

#sys.path.append('/home/jbs/develop/201902_questions_transformer')
sys.path.append('../qom_questions_transformer')

import string
import re
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
add_changeable('b')      # the 2nd list
add_changeable('n')      # the loop variable
add_changeable('i')      # the loop variable
add_changeable('__var')  # class's global variable
add_changeable('P')      # class name
add_changeable('p')      # class variable
add_changeable('13')     # the list length
add_changeable('33')     # the list length
add_changeable('3')      # the list length

# answers list name
add_changeable(r'\verb+a+')
add_changeable(r'\verb+b+')

# answers (indexes)
add_changeable(r'\verb+1+')
add_changeable(r'\verb+2_1+')
add_changeable(r'\verb+2_2+')
add_changeable(r'\verb+3_1+')
add_changeable(r'\verb+3_2+')
add_changeable(r'\verb+3_1_f+')
add_changeable(r'\verb+3_2_f+')
add_changeable(r'\verb+4+')
add_changeable(r'\verb+5_1+')
add_changeable(r'\verb+5_2+')

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
b  = None
_1 = None
_2_1 = None
_2_2 = None
_3 = None
_3_1 = None
_3_2 = None
_3_1_f = None
_3_2_f = None
_4 = None
_5_1 = None
_5_2 = None
__var = None
var = None
P = None
p = None






def make_transformations():

    ''
    global a
    global b
    global _1
    global _2_1
    global _2_2
    global _3
    global _3_1
    global _3_2
    global _3_1_f
    global _3_2_f
    global _4
    global __var
    global var
    global P
    global p
    
    # question
    _135 = str(randint(1000000, 2000000))
    [a, b, n, p, P, var, i] = sample(string.ascii_lowercase, 7)
    _13 = randint(19000, 20000)
    _3 = randint(0, 3)
    _33 = randint(50, 1500)
    __var = '__' + var
    P = P.upper()

    wrong_3 = choice((p + '.' + '__' + var,
                             P + '.' + '__' + var,
                             p + '._' + P + '_' + var,
                             P + '.' + var , p + '.' + var))
    correct_answers_list = [p + '._' + P + '__' + var,
                            p + ".get_var()", P + "().get_var()"]

    _3_1, _3_2 = sample(correct_answers_list, 2)

    decision = choice((0, 1))
    correct_3 = choice((_3_1, _3_2))
    
    _3_1_f = correct_3 if decision == 0 else wrong_3
    _3_2_f = wrong_3 if decision == 0 else _3_1
    
    change_all_occurrences('135',"<b><font color=green><i>" +  _135+ "</font></i></b>")
    change_token_all_occurrences('a',"<b><font color=green><i>" +  a+ "</font></i></b>")
    change_token_all_occurrences('b',"<b><font color=green><i>" +  b+ "</font></i></b>")
    change_token_all_occurrences('P',"<b><font color=green><i>" +  P+ "</font></i></b>")
    change_token_all_occurrences('__var',"<b><font color=green><i>" +  __var+ "</font></i></b>")
    change_token_all_occurrences('p',"<b><font color=green><i>" +  p+ "</font></i></b>")
    change_token_all_occurrences('i',"<b><font color=green><i>" +  i+ "</font></i></b>")
    change_token_all_occurrences('n',"<b><font color=green><i>" +  n+ "</font></i></b>")
    change_all_occurrences('13',"<b><font color=green><i>" +  str(_13)+ "</font></i></b>")
    change_all_occurrences('3',"<b><font color=green><i>" +  str(_3)+ "</font></i></b>")
    change_all_occurrences('33',"<b><font color=green><i>" +  str(_33)+ "</font></i></b>")

    # answers
    change_all_occurrences(r'\verb+a+',"<b><font color=green><i>" +  r'\verb+' + a + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+b+',"<b><font color=green><i>" +  r'\verb+' + b + '+'+ "</font></i></b>")

    
    # indexes with no repetitions
    [_1] = sample(range(10), 1)
    _1 = str(_1)
    
    #regex parameters decision
    [_2_1, _2_2] = sample(range(10) ,2)
    _2_1 = str(_2_1)
    _2_2 = str(_2_2)
    
    decision = choice(("single", "list"))
    if decision == "single":
        [_4] = sample(range(10),1)
        _4 = str(_4) + choice(('?', '*', '+'))
    if decision == "list":
        [_4] = sample(range(10),1)
        [max_4] = sample(range(len(str(_13))),1)
        max_4 = max_4 if max_4 > 0 else max_4 + 1
        [min_4] = sample(range(max_4),1)
        _4 = str(_4) + '{' + str(min_4) + '-' + str(max_4) + '}'
    
    change_all_occurrences(r'\verb+1+',"<b><font color=green><i>" +  r'\verb+' + _1 + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+2_1+',"<b><font color=green><i>" +  r'\verb+' + _2_1 + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+2_2+',"<b><font color=green><i>" +  r'\verb+' + _2_2 + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+3_1+',"<b><font color=green><i>" +  r'\verb+' + _3_1 + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+3_2+',"<b><font color=green><i>" +  r'\verb+' + _3_2 + '+'+ "</font></i></b>")
##    change_all_occurrences(r'\verb+3_1+',"<b><font color=green><i>" +  _3_1+ "</font></i></b>")
##    change_all_occurrences(r'\verb+3_2+',"<b><font color=green><i>" +  _3_2 + "</font></i></b>")
    change_all_occurrences(r'\verb+3_1_f+',"<b><font color=green><i>" +  r'\verb+' + _3_1_f + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+3_2_f+',"<b><font color=green><i>" +  r'\verb+' + _3_2_f + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+4+',"<b><font color=green><i>" +  r'\verb+' + _4 + '+'+ "</font></i></b>")
    

    



def make_transformations_on_results(program):
    ''
    global a
    global b
    global _1
    global _2_1
    global _2_2
    global _3_1
    global _3_2
    global _3_1_f
    global _3_2_f
    global _4
    global _5_1
    global _5_2
    global __var
    global var
    global P
    global p
    

    print('»»»»»»»»»')
    the_list = program.get_global(a)
    the_list_b = program.get_global(b)
    #correct index for question 5
    _5_1, _5_2 = choose_correct_idx_5(the_list)  
    change_all_occurrences(r'\verb+5_1+',"<b><font color=green><i>" +  r'\verb+' + str(_5_1) + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+5_2+',"<b><font color=green><i>" +  r'\verb+' + str(_5_2) + '+'+ "</font></i></b>")

    answer_1_true = regular_search(_1, the_list_b)
    new_b = regular_subtitution(_2_1, _2_2, the_list_b)
    answer_2_true = round(regular_search(_2_2, new_b) /
                          regular_search(_2_2, the_list_b),2)
    answer_4_true = regular_match(_4, the_list_b)
    answer_5_true = power(the_list[_5_1].num, the_list[_5_2].num)

    # true answers
    change_all_occurrences(r'\verb+11+',"<b><font color=green><i>" +  str(answer_1_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+22+',"<b><font color=green><i>" +  str(answer_2_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+44+',"<b><font color=green><i>" +  str(answer_4_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+55+',"<b><font color=green><i>" +  str(answer_5_true)+ "</font></i></b>")

    # wrong answers
    increment2 = choice([.1, -.1])
    increment4 = choice([1, -1])
    increment5 = choice([1, -1])

    answer_1_false = _1
    answer_2_false = round(answer_2_true + increment2,2)
    answer_4_false = answer_4_true + increment4
    answer_5_false = answer_5_true + increment5

    change_all_occurrences(r'\verb+111+',"<b><font color=green><i>" +  str(answer_1_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+222+',"<b><font color=green><i>" +  str(answer_2_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+444+',"<b><font color=green><i>" +  str(answer_4_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+555+',"<b><font color=green><i>" +  str(answer_5_false)+ "</font></i></b>")


def choose_correct_idx_5(the_list):
    result_base = 0
    result_exp = 1
    for i in range(len(the_list)):
        value = the_list[i].num
        if value < 10:
            result_base = i
            break
    for i in range(len(the_list)):
        value = the_list[i].num
        if value < 8 and value != the_list[result_base].num:
            result_exp = i
            break
    return result_base, result_exp

def choose_diffrenet_answer(the_list, choosen_answer):
    while True:
        result = choice(the_list)
        if result != choosen_answer:
            return result

def power(num, exp):
    if exp == 1: return num
    else: return num * power(num, exp - 1)

def regular_search(pattern_val, the_list):
    return sum(list(map(lambda x: 1 if re.search(r"" + pattern_val, x)
                        else 0, the_list)))

def regular_subtitution(pattern_val, subtitute_val, the_list):
    return list(map(lambda x: re.sub(r"" + pattern_val, subtitute_val, x) , the_list))

def regular_match(pattern_val, the_list):
    return sum(list(map(lambda x: 1 if re.match(r"" + pattern_val, x)
                        else 0, the_list)))

