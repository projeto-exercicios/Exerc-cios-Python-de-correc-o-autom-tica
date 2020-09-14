
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
add_changeable('135')    # seed
add_changeable('a')      # the list w/ result of func i
add_changeable('b')      # the list w/ numbers random
add_changeable('f')      # the list w/ numbers random
add_changeable('c')      # the loop variable. this was added after an
add_changeable('d')      # error ocurred. see ERROR below
add_changeable('e')
add_changeable('300')    # the list length
add_changeable('125')    # the randint max value 


# answers list name
add_changeable(r'\verb+a+')
add_changeable(r'\verb+b+')
# answers (indexes)
add_changeable(r'\verb+1+')
add_changeable(r'\verb+2+')
add_changeable(r'\verb+3+')
add_changeable(r'\verb+4+')


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
    a = choice(string.ascii_lowercase) # ERROR: isto está mal!!!  a letra 'a'

    # não pode ser uma letra qualquer. porque se for igual a 'n' como
    # há no programa uma variável 'n' isto vai causar um erro
    # deexecuçaõ. Intermitente, o que ainda é pior
    # soluções possíveis:
    # 1. escolher uma letra qualquer execto o 'n'
    # 2. substituir também a variável 'n' escolhendo duas letras diferentes
    # vai ser usada a solução 2 porque assim as versões ainda ficam
    # mais diferentes. a variável 'n' passa também a ser diferente
    [a, b, c, d, e, f] = sample(string.ascii_lowercase, 6)
    _300 = randint(19000, 20000)
    _125 = randint(0, 1500)

    
    change_all_occurrences('135',"<b><i>" +  _135+ "</b></i>")
    change_token_all_occurrences('a',"<b><i>" +  a+ "</b></i>")
    change_token_all_occurrences('b',"<b><i>" +  b+ "</b></i>")
    change_token_all_occurrences('c',"<b><i>" +  c+ "</b></i>")
    change_token_all_occurrences('d',"<b><i>" +  d+ "</b></i>")
    change_token_all_occurrences('e',"<b><i>" +  e+ "</b></i>")
    change_token_all_occurrences('f',"<b><i>" +  f+ "</b></i>")
    change_all_occurrences('300',"<b><i>" +  str(_300)+ "</b></i>")
    change_all_occurrences('125',"<b><i>" +  str(_125)+ "</b></i>")


    # answers
    change_all_occurrences(r'\verb+a+',"<b><i>" +  r'\verb+' + a + '+'+ "</b></i>")
    
    # indexes with no repetitions
    [_1, _3, _4, _5] = sample(range(_300), 4)
##    print(_300 , _1, _2, _3, _4, _5)
    change_all_occurrences(r'\verb+1+',"<b><i>" +  r'\verb+' + str(_1) + '+'+ "</b></i>")
    change_all_occurrences(r'\verb+3+',"<b><i>" +  r'\verb+' + str(_3) + '+'+ "</b></i>")
    change_all_occurrences(r'\verb+4+',"<b><i>" +  r'\verb+' + str(_4) + '+'+ "</b></i>")

    


def random_generator(array):
    num = []

    for n in range(50):
        num.append(randint(min(array),max(array)))
    return choice(num)

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
    _2 = random_generator(the_list)
    change_all_occurrences(r'\verb+2+',"<b><i>" +  r'\verb+' + str(_2) + '+'+ "</b></i>")

    
    answer_1_true = the_list[_1]
    answer_2_true = sum(np.array(the_list) == _2)
    answer_3_true = the_list[_3]
    answer_4_true = the_list[_4]
    answer_5_true = sum(the_list)

    # true answers
    change_all_occurrences(r'\verb+11+',"<b><i>" +  str(answer_1_true)+ "</b></i>")
    change_all_occurrences(r'\verb+22+',"<b><i>" +  str(answer_2_true)+ "</b></i>")
    change_all_occurrences(r'\verb+33+',"<b><i>" +  str(answer_3_true)+ "</b></i>")
    change_all_occurrences(r'\verb+44+',"<b><i>" +  str(answer_4_true)+ "</b></i>")
    change_all_occurrences(r'\verb+55+',"<b><i>" +  str(answer_5_true)+ "</b></i>")

    # wrong answers
    increment1 = choice([1, -1])
    increment2 = choice([1, -1])
    increment3 = choice([1, -1])
    increment4 = choice([1, -1])
    increment5 = choice([1, -1])

    answer_1_false = the_list[_1] + increment1
    answer_2_false = sum(np.array(the_list) == _2) + increment2
    answer_3_false = the_list[_3] + increment3
    answer_4_false = the_list[_4 + increment4]
    answer_5_false = sum(the_list) + increment5
    change_all_occurrences(r'\verb+111+',"<b><i>" +  str(answer_1_false)+ "</b></i>")
    change_all_occurrences(r'\verb+222+',"<b><i>" +  str(answer_2_false)+ "</b></i>")
    change_all_occurrences(r'\verb+333+',"<b><i>" +  str(answer_3_false)+ "</b></i>")
    change_all_occurrences(r'\verb+444+',"<b><i>" +  str(answer_4_false)+ "</b></i>")
    change_all_occurrences(r'\verb+555+',"<b><i>" +  str(answer_5_false)+ "</b></i>")
    

