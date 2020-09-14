
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
add_changeable('i')      # the loop variable
add_changeable('n')      # the loop variable
add_changeable('p')      # class variable
add_changeable('P')      # class name

add_changeable('13')     # the list length
add_changeable('3')      # min num value
add_changeable('33')     # max num value

# answers class name
add_changeable(r'\verb+classP+')
add_changeable(r'\verb+classp+')

# answers list name
add_changeable(r'\verb+a+')

# answers (indexes)
add_changeable(r'\verb+1_1+')
add_changeable(r'\verb+1_2+')
add_changeable(r'\verb+1_3+')
add_changeable(r'\verb+2_1+')
add_changeable(r'\verb+2_2+')
add_changeable(r'\verb+3+')


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
p = None
P = None
quest_2_type = None
_1_1 = None
_1_2 = None
_1_3 = None
_2_1 = None
_2_2 = None
_3 = None
_13 = None



def make_transformations():

    ''
    global a
    global p
    global P
    global _1_1
    global _1_2
    global _1_3
    global _2_1
    global _2_2
    global _3
    global _13

    
    # question
    _135 = str(randint(1000000, 2000000))
    [a, i, n, p, P] = sample(string.ascii_lowercase, 5)
    _13 = randint(19000, 20000)
    _3 = randint(0, 5)
    _33 = randint(50, 255)
    P = P.upper()
    
    change_all_occurrences('135',"<b><i>" +  _135+ "</b></i>")
    change_token_all_occurrences('a',"<b><i>" +  a+ "</b></i>")
    change_token_all_occurrences('i',"<b><i>" +  i+ "</b></i>")
    change_token_all_occurrences('n',"<b><i>" +  n+ "</b></i>")
    change_token_all_occurrences('p',"<b><i>" +  p+ "</b></i>")
    change_token_all_occurrences('P',"<b><i>" +  P+ "</b></i>")
    change_all_occurrences('13',"<b><i>" +  str(_13)+ "</b></i>")
    change_all_occurrences('3',"<b><i>" +  str(_3)+ "</b></i>")
    change_all_occurrences('33',"<b><i>" +  str(_33)+ "</b></i>")

    _1_1, _1_2, _1_3 = _1_quest()
    _2_1, _2_2 = _2_quest()
    _3 = choice(("alterar o", "aceder ao"))
    # answers
    change_all_occurrences(r'\verb+a+',"<b><i>" +  r'\verb+' + a + '+'+ "</b></i>")
    change_all_occurrences(r'\verb+classP+',"<b><i>" +  r'\verb+' + P + '+'+ "</b></i>")
    change_all_occurrences(r'\verb+classp+',"<b><i>" +  r'\verb+' + p + '+'+ "</b></i>")
    
    # indexes with no repetitions
    [_1, _2] = sample(range(_13), 2)

    change_all_occurrences(r'\verb+1_1+',"<b><i>" +  r'\verb+' + str(_1_1) + '+'+ "</b></i>")
    change_all_occurrences(r'\verb+1_2+',"<b><i>" +  r'\verb+' + str(_1_2) + '+'+ "</b></i>")
    change_all_occurrences(r'\verb+1_3+',"<b><i>" +  r'\verb+' + str(_1_3) + '+'+ "</b></i>")
    change_all_occurrences(r'\verb+2_1+',"<b><i>" +  r'\verb+' + str(_2_1) + '+'+ "</b></i>")
    change_all_occurrences(r'\verb+2_2+',"<b><i>" +  r'\verb+' + str(_2_2) + '+'+ "</b></i>")
    change_all_occurrences(r'\verb+3+',"<b><i>" +  r'\verb+' + str(_3) + '+'+ "</b></i>")


    



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global a
    global p
    global _1_1
    global _1_2
    global _1_3
    global _2
    global _3
    global _4
    global _5

    print('»»»»»»»»»')
    the_list = program.get_global(a)
    pt_a = "ã".encode('utf8').decode('iso-8859-1')
    pt_e = "é".encode('utf8').decode('iso-8859-1')
    answer_1_true = "" if _1_1 == "Com" else "n" + pt_a + "o"
    answer_2_true = "pode ser semelhante" if quest_2_type == "correct"                    else choice((pt_e + " igual", pt_e + " diferente"))
    answer_3_true = p + "[index] = value" if _3 == "alterar o"                    else p + "[index]"
    answer_4_true = "uma string"
    answer_5_true = choice(("o tamanho da lista menos um elemento", str(_13 - 1)))

    # true answers
    change_all_occurrences(r'\verb+11+',"<b><i>" +  answer_1_true+ "</b></i>")
    change_all_occurrences(r'\verb+22+',"<b><i>" +  answer_2_true+ "</b></i>")
    change_all_occurrences(r'\verb+33+',"<b><i>" +  answer_3_true+ "</b></i>")
    change_all_occurrences(r'\verb+44+',"<b><i>" +  answer_4_true+ "</b></i>")
    change_all_occurrences(r'\verb+55+',"<b><i>" +  answer_5_true+ "</b></i>")

    # wrong answers
    answer_1_false = "n" + pt_a + "o" if _1_1 == "Com" else ""
    answer_2_false = choice((pt_e + " igual", pt_e + " diferente"))                     if quest_2_type == "correct" else "pode ser semelhante"
    answer_3_false = answer_3_true
    answer_4_false = choice(("lista", "lista de ints", "lista de strings"))
    answer_5_false = choice(("o tamanho da lista", "o tamanho da lista que " + pt_e
                             + str(_13), "o tamanho da lista que " + pt_e + str(_13 - 1),
                             str(_13)))

    change_all_occurrences(r'\verb+111+',"<b><i>" +  answer_1_false+ "</b></i>")
    change_all_occurrences(r'\verb+222+',"<b><i>" +  answer_2_false+ "</b></i>")
    change_all_occurrences(r'\verb+333+',"<b><i>" +  answer_3_false+ "</b></i>")
    change_all_occurrences(r'\verb+444+',"<b><i>" +  answer_4_false+ "</b></i>")
    change_all_occurrences(r'\verb+555+',"<b><i>" +  answer_5_false+ "</b></i>")


def _1_quest():
    decision_1 = choice(("Sem", "Com"))
    decision_2 = choice(("__getitem__(self, index)",
                         "__setitem__(self, index ,value)"))
    decision_3 = "item assignment" if decision_2 ==                 "__setitem__(self, index ,value)"                 else "indexing"
    return decision_1, decision_2, decision_3

def _2_quest():
    global a
    global p
    global P
    global _13
    global quest_2_type
    idx = choice(range(_13))
    func_1 = None
    func_2 = None
    quest_2_type = choice(("wrong", "correct"))
    wrong_answers = [P + ".getitem(" + str(idx) + ")",
                     p + ".getitem(" + str(idx) + ")",
                     P + "._getitem_(" + str(idx) + ")",
                     p + "._getitem_(" + str(idx) + ")",
                     P + "[" + str(idx)+ "]",
                     P + ".__getitem__(" + str(idx) + ")"]
    correct_answers_i = [P + "(" + a + ")[" + str(idx) + "]",
                         p + "[" + str(idx) + "]"]
    correct_answers_ni = [P + "(" + a + ").__getitem__(" + str(idx) + ")",
                          p + ".__getitem__(" + str(idx) + ")"]
    if quest_2_type == "wrong":
        func_1 = choice(wrong_answers)
        func_2 = choice(choice((correct_answers_i, correct_answers_ni)))
    if quest_2_type == "correct":
        func_1 = choice(choice((correct_answers_i, correct_answers_ni)))
        func_2 = choice(correct_answers_i) if func_1 in correct_answers_ni                 else choice(correct_answers_ni)
    return func_1, func_2

    

