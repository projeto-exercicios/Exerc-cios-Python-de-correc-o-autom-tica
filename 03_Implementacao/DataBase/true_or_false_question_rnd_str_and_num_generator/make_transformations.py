
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
add_changeable('k')      # the loop variable. this was added after an
add_changeable('c')      # error ocurred. see ERROR below
add_changeable('g')
add_changeable('g1')     # random string/number
add_changeable('l')      # list of random string letters
add_changeable('n')      # list of random numbers
add_changeable('20')     # the list length


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
    [a, k, c, g, l, n, g1] = sample(string.ascii_lowercase, 7)
    _20 = randint(18000, 20000)

    
    change_all_occurrences('135', _135)
    change_token_all_occurrences('a', a)
    change_token_all_occurrences('k', k)
    change_token_all_occurrences('c', c)
    change_token_all_occurrences('g', g)
    change_token_all_occurrences('l', l)
    change_token_all_occurrences('n', n)
    change_token_all_occurrences('g1', g1)
    change_all_occurrences('20', str(_20))


    # answers
    change_all_occurrences(r'\verb+a+',r'\verb+' + a + '+')
    
    # indexes with no repetitions
    [_1, _2, _3, _4, _5] = sample(range(_20), 5)

    change_all_occurrences(r'\verb+1+',r'\verb+' + str(_1) + '+')
    change_all_occurrences(r'\verb+2+',r'\verb+' + str(_2) + '+')
    change_all_occurrences(r'\verb+3+',r'\verb+' + str(_3) + '+')
    change_all_occurrences(r'\verb+4+',r'\verb+' + str(_4) + '+')
    change_all_occurrences(r'\verb+5+',r'\verb+' + str(_5) + '+')

    



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

    isNum = "um numero"
    isString = "uma string"
    
    the_list = program.get_global(a)
    #print(the_list)
    answer_1_true = the_list[_1]
    answer_2_true = the_list[_2]
    answer_3_true = ""
    if the_list[_3].isdigit():
        answer_3_true = isString
    if not the_list[_3].isdigit():
        answer_3_true = isNum
    answer_4_true = the_list[_4]
    answer_5_true = ""
    if the_list[_5].isdigit():
        answer_5_true = isString
    if not the_list[_5].isdigit():
        answer_5_true = isNum

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

    answer_1_false = the_list[_1 + increment1]
    answer_2_false = the_list[_2 + increment2]
    answer_3_false = ""
    if the_list[_3 + increment3].isdigit():
        answer_3_false = isString
    if not the_list[_3 + increment3].isdigit():
        answer_3_false = isNum
    answer_4_false = the_list[_4 + increment4]
    answer_5_false = ""
    if the_list[_5 + increment5].isdigit():
        answer_5_false = isString
    if not the_list[_5 + increment5].isdigit():
        answer_5_false = isNum
    change_all_occurrences(r'\verb+111+', str(answer_1_false))
    change_all_occurrences(r'\verb+222+', str(answer_2_false))
    change_all_occurrences(r'\verb+333+', str(answer_3_false))
    change_all_occurrences(r'\verb+444+', str(answer_4_false))
    change_all_occurrences(r'\verb+555+', str(answer_5_false))
    

