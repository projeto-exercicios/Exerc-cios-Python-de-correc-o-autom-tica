
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
add_changeable('c')      # the list
add_changeable('d')      # range variable
add_changeable('o')      # the loop variable. this was added after an
                         # error ocurred. see ERROR below
add_changeable('11')     # the list min length
add_changeable('55')     # the list max length
add_changeable('333')    # the randint value

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
c  = None
_1 = None
_2 = None
_3 = None
_4 = None
_5 = None





def make_transformations():
    ''
    global c
    global _1
    global _2
    global _3
    global _4
    global _5
    
    # question
    _135 = str(randint(1000000, 2000000))
    c = choice(string.ascii_lowercase) # ERROR: isto está mal!!!  a letra 'a'
    # não pode ser uma letra qualquer. porque se for igual a 'n' como
    # há no programa uma variável 'n' isto vai causar um erro
    # deexecuçaõ. Intermitente, o que ainda é pior
    # soluções possíveis:
    # 1. escolher uma letra qualquer execto o 'n'
    # 2. substituir também a variável 'n' escolhendo duas letras diferentes
    # vai ser usada a solução 2 porque assim as versões ainda ficam
    # mais diferentes. a variável 'n' passa também a ser diferente
    [c, d, o] = sample(string.ascii_lowercase, 3)
    _55 = randint(19000, 20000)
    _11 = randint(500,1000)
    _333 = randint(0, 10000)
    
    change_all_occurrences('135',"<b><font color=red><i>" +  _135+ "</font></i></b>")
    change_token_all_occurrences('c',"<b><font color=red><i>" +  c+ "</font></i></b>")
    change_token_all_occurrences('d',"<b><font color=red><i>" +  d+ "</font></i></b>")
    change_token_all_occurrences('o',"<b><font color=red><i>" +  o+ "</font></i></b>")
    change_all_occurrences('55',"<b><font color=red><i>" +  str(_55)+ "</font></i></b>")
    change_all_occurrences('11',"<b><font color=red><i>" +  str(_11)+ "</font></i></b>")
    change_all_occurrences('333',"<b><font color=red><i>" +  str(_333)+ "</font></i></b>")

    # answers
    change_all_occurrences(r'\verb+a+',"<b><font color=red><i>" +  r'\verb+' + c + '+'+ "</font></i></b>")
    
    # indexes with no repetitions
    [_1, _2, _3, _4, _5] = sample(range(_55), 5)
    print(_1, _2, _3, _4, _5)
    change_all_occurrences(r'\verb+1+',"<b><font color=red><i>" +  r'\verb+' + str(_1) + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+2+',"<b><font color=red><i>" +  r'\verb+' + str(_2) + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+3+',"<b><font color=red><i>" +  r'\verb+' + str(_3) + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+4+',"<b><font color=red><i>" +  r'\verb+' + str(_4) + '+'+ "</font></i></b>")
    change_all_occurrences(r'\verb+5+',"<b><font color=red><i>" +  r'\verb+' + str(_5) + '+'+ "</font></i></b>")

    



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global c
    global _1
    global _2
    global _3
    global _4
    global _5

    #print('»»»»»»»»»')
    #print(a)
    the_list = program.get_global(c)
    print(the_list)
    answer_1_true = the_list[_1]
    answer_2_true = the_list[_2]
    answer_3_true = the_list[_3]
    answer_4_true = the_list[_4]
    answer_5_true = the_list[_5]

    # true answers
    change_all_occurrences(r'\verb+11+',"<b><font color=red><i>" +  str(answer_1_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+22+',"<b><font color=red><i>" +  str(answer_2_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+33+',"<b><font color=red><i>" +  str(answer_3_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+44+',"<b><font color=red><i>" +  str(answer_4_true)+ "</font></i></b>")
    change_all_occurrences(r'\verb+55+',"<b><font color=red><i>" +  str(answer_5_true)+ "</font></i></b>")

    # wrong answers
    increment1 = choice([1, -1])
    increment2 = choice([1, -1])
    increment3 = choice([1, -1])
    increment4 = choice([1, -1])
    increment5 = choice([1, -1])

    answer_1_false = answer_1_true + increment1
    answer_2_false = answer_2_true + increment2
    answer_3_false = answer_3_true + increment3
    answer_4_false = answer_4_true + increment4
    answer_5_false = answer_5_true + increment5

    change_all_occurrences(r'\verb+111+',"<b><font color=red><i>" +  str(answer_1_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+222+',"<b><font color=red><i>" +  str(answer_2_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+333+',"<b><font color=red><i>" +  str(answer_3_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+444+',"<b><font color=red><i>" +  str(answer_4_false)+ "</font></i></b>")
    change_all_occurrences(r'\verb+555+',"<b><font color=red><i>" +  str(answer_5_false)+ "</font></i></b>")
    

