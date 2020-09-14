
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
from string import ascii_letters

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
add_changeable('n')      # the loop variable
add_changeable('x')      # the loop variable
add_changeable('d')      # the dictionary variable
add_changeable('dic')    # the dictionary class variable
add_changeable('str_a')  # the list of strings
add_changeable('int_a')  # the list of ints

add_changeable('13')     # the list length
add_changeable('3')      # the min int value
add_changeable('33')     # the max int value

# answers list name
add_changeable(r'\verb+a+')

# answers object dictionary class name
add_changeable(r'\verb+dic+')

# answers object dictionary class val
add_changeable(r'\verb+dic_val+')

# answer new val to add to object dectionary class
add_changeable(r'\verb+add_val+')

# answers dictionary name
add_changeable(r'\verb+d+')

# answers (indexes)
add_changeable(r'\verb+1+')
add_changeable(r'\verb+2+')
add_changeable(r'\verb+3+')
add_changeable(r'\verb+4+')
add_changeable(r'\verb+4_t+')
add_changeable(r'\verb+4_f+')
add_changeable(r'\verb+5+')

# right answers values
add_changeable(r'\verb+11_1+')
add_changeable(r'\verb+11_2+')
add_changeable(r'\verb+22+')
add_changeable(r'\verb+33+')
add_changeable(r'\verb+44+')
add_changeable(r'\verb+55+')

# wrong answers values
add_changeable(r'\verb+111_1+')
add_changeable(r'\verb+111_2+')
add_changeable(r'\verb+222+')
add_changeable(r'\verb+333+')
add_changeable(r'\verb+444+')
add_changeable(r'\verb+555+')





# variáveis partilhas entre as funções make_transformations e
# make_transformations_on_results
a  = None
d = None
str_a = None
int_a = None
dic = None
_2 = None
_3 = None
_3_idx = None
_3_decision = None
_4 = None
_4_decision = None
_5 = None

pt_u = "ú".encode('utf8').decode('iso-8859-1')
pt_numeros = 'n' + pt_u + 'meros'




def make_transformations():

    ''
    global a
    global d
    global str_a
    global int_a
    global dic
    global _2
    global _3_decision
    global _4
    global _4_decision
    global _5
    
    # question
    _135 = str(randint(1000000, 2000000))
    [a, n, x, d, dic] = sample(string.ascii_lowercase, 5)
    _13 = randint(19000, 20000)
    _3 = randint(0, 5)
    _33 = randint(_3, 500)
    str_a = 'str_' + a
    int_a = 'int_' + a
    
    change_all_occurrences('135', _135)
    change_token_all_occurrences('a', a)
    change_token_all_occurrences('n', n)
    change_token_all_occurrences('x', x)
    change_token_all_occurrences('d', d)
    change_token_all_occurrences('dic', dic)
    change_token_all_occurrences('str_a', str_a)
    change_token_all_occurrences('int_a', int_a)
    change_all_occurrences('13', str(_13))
    change_all_occurrences('3', str(_3))
    change_all_occurrences('33', str(_33))

    # answers
    change_all_occurrences(r'\verb+a+', r'\verb+' + a + '+')
    change_all_occurrences(r'\verb+d+', r'\verb+' + d + '+')
    change_all_occurrences(r'\verb+dic+', r'\verb+' + dic + '+')
    
    # indexes with no repetitions
    _2 = choice((d, str_a, int_a, a))
    _3_decision = choice(("int", "float", "str"))
    _4 = choice(ascii_letters)
    _5 = choice(("maior", "menor"))

    change_all_occurrences(r'\verb+2+', r'\verb+' + _2 + '+')
    change_all_occurrences(r'\verb+4+', r'\verb+' + _4 + '+')
    change_all_occurrences(r'\verb+4_t+', r'\verb+"' + _4 + '"+')
    _4_decision = choice((0, 1))
    if _4_decision == 0:
        change_all_occurrences(r'\verb+4_f+', r'\verb+"' + _4 + '"+')
    else:
        change_all_occurrences(r'\verb+4_f+', r'\verb+' + _4 + '+')
    change_all_occurrences(r'\verb+5+', r'\verb+' + _5 + '+')

    



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global a
    global d
    global str_a
    global int_a
    global dic
    global _2
    global _3
    global _3_idx
    global _3_decision
    global _4
    global _4_decision
    global _5

    the_list = program.get_global(a)
    str_the_list = program.get_global(str_a)
    int_the_list = program.get_global(int_a)
    the_dic = program.get_global(dic)
    the_dict = program.get_global(d)
    _3_idx = choice(ascii_letters)
    
    _3 = the_dic[_3_idx][0] if _3_decision == 'int' else the_dic[_3_idx] * 1.0 \
         if _3_decision == 'float' else _3_idx
    # answer index
    change_all_occurrences(r'\verb+3+', r'\verb+' + str(_3) + '+')

    # answer values
    dic_val = the_dic[_4][0]
    change_all_occurrences(r'\verb+dic_val+', r'\verb+' + str(dic_val) + '+')
    add_val = randint(7, 500)
    change_all_occurrences(r'\verb+add_val+', r'\verb+' + str(add_val) + '+')
    
    answer_1_1_true = "letras" if len(str_the_list) > len(int_the_list) else pt_numeros
    answer_1_2_true = pt_numeros if answer_1_1_true == "letras" else "letras"
    answer_2_true = "tamanho maior" if len(d) > len(_2) else "tamanho menor" \
                    if len(d) < len(_2) else "tamanho igual"
    answer_3_true = the_dic[_3][0]
    answer_4_true = 'o valor ' + str(add_val)
    answer_5_true = get_max_key(the_dict) if _5 == "maior" else get_min_key(the_dict)

    
    
    # true answers
    change_all_occurrences(r'\verb+11_1+', str(answer_1_1_true))
    change_all_occurrences(r'\verb+11_2+', str(answer_1_2_true))
    change_all_occurrences(r'\verb+22+', str(answer_2_true))
    change_all_occurrences(r'\verb+33+', str(answer_3_true))
    change_all_occurrences(r'\verb+44+', str(answer_4_true))
    change_all_occurrences(r'\verb+55+', str(answer_5_true))

    # wrong answers
    increment4 = choice([1, -1])
    increment5 = choice([1, -1])

    answer_1_1_false = pt_numeros if answer_1_1_true == "letras" else "letras"
    answer_1_2_false = "letras" if answer_1_1_true == "letras" else pt_numeros
    answer_2_false = choice(("tamanho maior", "tamanho menor"))  \
                     if answer_2_true == "tamanho igual" else \
                     "tamanho maior" if answer_2_true == "tamanho menor" \
                     else "tamanho menor"
    answer_3_false = quest_3_false(answer_3_true)
    answer_4_false = 'os valores ' + str(add_val) + ' e ' + str(dic_val) \
                     if _4_decision == 0 else 'o valor ' + str(add_val)
    answer_5_false = get_min_key(the_dict) if _5 == "maior" else get_max_key(the_dict)


    change_all_occurrences(r'\verb+111_1+', str(answer_1_1_false))
    change_all_occurrences(r'\verb+111_2+', str(answer_1_2_false))
    change_all_occurrences(r'\verb+222+', str(answer_2_false))
    change_all_occurrences(r'\verb+333+', str(answer_3_false))
    change_all_occurrences(r'\verb+444+', str(answer_4_false))
    change_all_occurrences(r'\verb+555+', str(answer_5_false))


def quest_3_false(true_answer):
    false_answer = None
    if true_answer == "None":
        return _3_idx
    if isinstance(true_answer, int):
        return true_answer - 1 if true_answer > 0 else true_answer + 1
    while True:
        false_answer = choice(ascii_letters)
        if false_answer != true_answer:
            break
    return false_answer

def get_max_key(d):
    return max(d, key=d.get)

def get_min_key(d):
    return min(d, key=d.get)


    
