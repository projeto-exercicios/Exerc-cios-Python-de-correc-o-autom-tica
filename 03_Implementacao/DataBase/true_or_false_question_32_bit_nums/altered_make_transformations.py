
import sys

#sys.path.append(
#    '/home/jbs/develop.old/articles/201509_python_exercises_generator')

#sys.path.append('/home/jbs/develop/201902_questions_transformer')
sys.path.append('../qom_questions_transformer')

import string
import numpy as np
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
add_changeable('b')      # the list a with reversed values
add_changeable('c')      # the list b with reversed values
add_changeable('r')      # reverser class 
add_changeable('i')      # the loop variable. this was added after an
                         # error ocurred. see ERROR below
add_changeable('13')     # the list length


# answers list name
add_changeable(r'\verb+a+')
add_changeable(r'\verb+b+')
add_changeable(r'\verb+c+')

# answers (indexes)
add_changeable(r'\verb+1+')
add_changeable(r'\verb+2+')
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
b  = None
c  = None
_1 = None
_2 = None
_5 = None
_13 = None





def make_transformations():

    ''
    global a
    global b
    global c
    global _1
    global _2
    global _5
    global _13
    
    # question
    _135 = str(randint(1000000, 2000000))
    [a, b, c, r, i] = sample(string.ascii_lowercase, 5)
    _13 = randint(19000, 20000)
    
    change_all_occurrences('135',"<b><font color=red><i>" +  _135+ "</font></i></b>")
    change_token_all_occurrences('a',"<b><font color=red><i>" +  a+ "</font></i></b>")
    change_token_all_occurrences('b',"<b><font color=red><i>" +  b+ "</font></i></b>")
    change_token_all_occurrences('c',"<b><font color=red><i>" +  c+ "</font></i></b>")
    change_token_all_occurrences('r',"<b><font color=red><i>" +  r+ "</font></i></b>")
    change_token_all_occurrences('i',"<b><font color=red><i>" +  i+ "</font></i></b>")
    change_all_occurrences('13',"<b><font color=red><i>" +  str(_13)+ "</font></i></b>")


    # answers
    change_all_occurrences(r'\verb+a+',"<b><font color=red><i>" +  r'\verb+' + a + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+b+',"<b><font color=red><i>" +  r'\verb+' + b + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+c+',"<b><font color=red><i>" +  r'\verb+' + c + '+'+ "</font></i></b>")
    
    # indexes with no repetitions
    [_1, _2, _5] = sample(range(_13), 3)

    change_all_occurrences(r'\verb+1+',"<b><font color=red><i>" +  r'\verb+' + str(_1) + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+2+',"<b><font color=red><i>" +  r'\verb+' + str(_2) + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+5+',"<b><font color=red><i>" +  r'\verb+' + str(_5) + '+'+ "</font></i></b>")

    



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global a
    global b
    global c
    global _1
    global _2
    global _5
    global _13


    the_list_a = program.get_global(a)
    the_list_b = program.get_global(b)
    the_list_c = program.get_global(c)
    r = Reverser()
##    print(the_list)
    answer_1_true = the_list_a[_1]
    answer_2_true = the_list_b[_2]
    answer_3_true = sum(np.array(the_list_a) != np.array(the_list_c) * 1.0)
    answer_4_true = sum(np.array(the_list_c) == 0 * 1.0)
    answer_5_true = r.reverse(binary_sum(to_bits(the_list_a[_5])
                                         ,to_bits(the_list_b[_5])))

    # true answers
    change_all_occurrences(r'\verb+11+',"<b><font color=red><i>" +  str(answer_1_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+22+',"<b><font color=red><i>" +  str(answer_2_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+33+',"<b><font color=red><i>" +  str(answer_3_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+44+',"<b><font color=red><i>" +  str(answer_4_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+55+',"<b><font color=red><i>" +  str(answer_5_true)+ "</font></i></b>")

    # wrong answers
    increment1 = choice([1, -1])
    increment2 = choice([1, -1])
    increment3 = choice([1, -1]) if answer_3_true > 0 else 1
    increment4 = choice([1, -1]) if answer_4_true > 0 else 1
    increment5 = choice([1, -1])

    answer_1_false = answer_1_true + increment1
    answer_2_false = answer_2_true + increment2
    answer_3_false = answer_3_true + increment3
    answer_4_false = answer_4_true + increment4
    if answer_5_true == 0:
        answer_5_false = r.false_reverse(binary_sum(to_bits(the_list_a[_5])
                                             ,to_bits(the_list_b[_5])))
    else:
        idx = 0
        while True:
            if idx != _5:
                reverse = r.reverse(binary_sum(to_bits(the_list_a[idx])
                                             ,to_bits(the_list_b[idx])))
                if reverse != answer_5_true:
                    answer_5_false = reverse
                    break
            idx += 1
            
    change_all_occurrences(r'\verb+111+',"<b><font color=red><i>" +  str(answer_1_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+222+',"<b><font color=red><i>" +  str(answer_2_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+333+',"<b><font color=red><i>" +  str(answer_3_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+444+',"<b><font color=red><i>" +  str(answer_4_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+555+',"<b><font color=red><i>" +  str(answer_5_false)+ "</font></i></b>")

class Reverser:

    def reverse(self, num):
        num_check = num if not isinstance(num, str) else bin_to_dec(num)
        if num_check < - 2**31 or num_check >= 2**31:
            return 0
        else:
            if(isinstance(num, str)):
                num_str = str(num)
                mult = ''
                if num_str[0] == '-':
                    num_str = num_str[1:]
                    mult = '-'
                return mult + (num_str[::-1])
            if(not isinstance(num, str)):
                num_str = str(num)
                mult = 1
                if num_str[0] == '-':
                    num_str = num_str[1:]
                    mult = -1
                return int(num_str[::-1]) * mult
    def false_reverse(self, num):
        if(isinstance(num, str)):
            num_str = str(num)
            mult = ''
            if num_str[0] == '-':
                num_str = num_str[1:]
                mult = '-'
            return mult + (num_str[::-1])
        if(not isinstance(num, str)):
            num_str = str(num)
            mult = 1
            if num_str[0] == '-':
                num_str = num_str[1:]
                mult = -1
            return int(num_str[::-1]) * mult

def to_bits(num):
  return '{0:01b}'.format(num)

def bin_to_dec(num):
    if(not isinstance(num, str)): num = str(num)
    mult = 1
    if num[0] == '-':
        num = num[1:]
        mult = -1
    r_num = num[::-1]
    idxs = []
    for i in range(len(r_num)):
        if r_num[i] == '1':
            idxs.append(i)
    result = 0
    for i in idxs:
        result += 2**i
    return result * mult


def binary_sum(num1, num2):
    d_num1 = bin_to_dec(num1)
    d_num2 = bin_to_dec(num2)
    result = d_num1 + d_num2
    return to_bits(result)

