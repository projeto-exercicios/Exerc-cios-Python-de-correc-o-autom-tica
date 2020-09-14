
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
    
    change_all_occurrences('135', _135)
    change_token_all_occurrences('a', a)
    change_token_all_occurrences('i', i)
    change_token_all_occurrences('n', n)
    change_token_all_occurrences('p', p)
    change_token_all_occurrences('P', P)
    change_all_occurrences('13', str(_13))
    change_all_occurrences('3', str(_3))
    change_all_occurrences('33', str(_33))

    _1_1, _1_2, _1_3 = _1_quest()
    _2_1, _2_2 = _2_quest()
    _3 = choice(("alterar o", "aceder ao"))
    # answers
    change_all_occurrences(r'\verb+a+', r'\verb+' + a + '+')
    change_all_occurrences(r'\verb+classP+', r'\verb+' + P + '+')
    change_all_occurrences(r'\verb+classp+', r'\verb+' + p + '+')
    
    # indexes with no repetitions
    [_1, _2] = sample(range(_13), 2)

    change_all_occurrences(r'\verb+1_1+', r'\verb+' + str(_1_1) + '+')
    change_all_occurrences(r'\verb+1_2+', r'\verb+' + str(_1_2) + '+')
    change_all_occurrences(r'\verb+1_3+', r'\verb+' + str(_1_3) + '+')
    change_all_occurrences(r'\verb+2_1+', r'\verb+' + str(_2_1) + '+')
    change_all_occurrences(r'\verb+2_2+', r'\verb+' + str(_2_2) + '+')
    change_all_occurrences(r'\verb+3+', r'\verb+' + str(_3) + '+')


    



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

    the_list = program.get_global(a)
    pt_a = "ã".encode('utf8').decode('iso-8859-1')
    pt_e = "é".encode('utf8').decode('iso-8859-1')
    answer_1_true = "" if _1_1 == "Com" else "n" + pt_a + "o"
    answer_2_true = "pode ser semelhante" if quest_2_type == "correct" \
                    else choice((pt_e + " igual", pt_e + " diferente"))
    answer_3_true = p + "[index] = value" if _3 == "alterar o" \
                    else p + "[index]"
    answer_4_true = "uma string"
    answer_5_true = choice(("o tamanho da lista menos um elemento", str(_13 - 1)))

    # true answers
    change_all_occurrences(r'\verb+11+', answer_1_true)
    change_all_occurrences(r'\verb+22+', answer_2_true)
    change_all_occurrences(r'\verb+33+', answer_3_true)
    change_all_occurrences(r'\verb+44+', answer_4_true)
    change_all_occurrences(r'\verb+55+', answer_5_true)

    # wrong answers
    answer_1_false = "n" + pt_a + "o" if _1_1 == "Com" else ""
    answer_2_false = choice((pt_e + " igual", pt_e + " diferente")) \
                     if quest_2_type == "correct" else "pode ser semelhante"
    answer_3_false = answer_3_true
    answer_4_false = choice(("lista", "lista de ints", "lista de strings"))
    answer_5_false = choice(("o tamanho da lista", "o tamanho da lista que " + pt_e
                             + str(_13), "o tamanho da lista que " + pt_e + str(_13 - 1),
                             str(_13)))

    change_all_occurrences(r'\verb+111+', answer_1_false)
    change_all_occurrences(r'\verb+222+', answer_2_false)
    change_all_occurrences(r'\verb+333+', answer_3_false)
    change_all_occurrences(r'\verb+444+', answer_4_false)
    change_all_occurrences(r'\verb+555+', answer_5_false)


def _1_quest():
    decision_1 = choice(("Sem", "Com"))
    decision_2 = choice(("__getitem__(self, index)",
                         "__setitem__(self, index ,value)"))
    decision_3 = "item assignment" if decision_2 == \
                 "__setitem__(self, index ,value)"\
                 else "indexing"
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
        func_2 = choice(correct_answers_i) if func_1 in correct_answers_ni \
                 else choice(correct_answers_ni)
    return func_1, func_2

    
