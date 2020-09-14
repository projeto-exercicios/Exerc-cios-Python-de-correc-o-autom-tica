
import sys

#sys.path.append(
#    '/home/jbs/develop.old/articles/201509_python_exercises_generator')

#sys.path.append('/home/jbs/develop/201902_questions_transformer')
sys.path.append('../qom_questions_transformer')

import string
import numpy as np
from random import seed
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
add_changeable('b')      # the list
add_changeable('c')      # the list
add_changeable('d')      # the list
add_changeable('e')      # the list
add_changeable('f')      # the list
add_changeable('n')      # the loop variable
add_changeable('numpy_func')

add_changeable('13')     # the list length
add_changeable('3')      # the min value
add_changeable('23')     # the max value
add_changeable('33')     # the 2nd list length

# answers list name
add_changeable(r'\verb+a+')
add_changeable(r'\verb+e+')

# answers (indexes)
add_changeable(r'\verb+1_t+')
add_changeable(r'\verb+1_f+')
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
e  = None
f  = None
_1_t = None
_1_f = None
numpy_func = None
_2 = None
_3 = None
_4 = None
_5_dimension = None
_5 = None
_23 = None

pt_e = "é".encode('utf8').decode('iso-8859-1')
pt_a = "ã".encode('utf8').decode('iso-8859-1')
pt_nao = 'n' + pt_a + 'o ' + pt_e
pt_lancar = 'lan' + 'ç'.encode('utf8').decode('iso-8859-1') + 'ar'
pt_dimensao ='dimens' + 'ã'.encode('utf8').decode('iso-8859-1') + 'o'
pt_dimensoes = 'dimens' + 'õ'.encode('utf8').decode('iso-8859-1') + 'es'
pt_numeros = 'n' + 'ú'.encode('utf8').decode('iso-8859-1') + 'meros'



def make_transformations():

    ''
    global a
    global e
    global f
    global numpy_func
    global _1_t
    global _1_f
    global _2
    global _3
    global _4
    global _5_dimension
    global _5
    global _23
    
    # question
    _135 = str(randint(1000000, 2000000))
    [a, b, c, d, e, f, n] = sample(string.ascii_lowercase, 7)
    _13 = randint(19000, 20000)
    _3 = randint(0, 5)
    _23 = randint(6, 300)
    _33 = randint(6, 600)

    maneiras_corretas = ['np.zeros(0)', 'np.ones(0)', 'np.arange(0)',
                            'np.array([])', 'np.empty(0)', 'np.eye(0)']
    maneiras_incorretas = ['[]', 'array()', 'np.array()', 'np.empty()']
    numpy_func = choice((maneiras_corretas))

    change_all_occurrences('135', _135)
    change_token_all_occurrences('a', a)
    change_token_all_occurrences('b', b)
    change_token_all_occurrences('c', c)
    change_token_all_occurrences('d', d)
    change_token_all_occurrences('e', e)
    change_token_all_occurrences('f', f)
    change_token_all_occurrences('n', n)
    change_all_occurrences('13', str(_13))
    change_all_occurrences('3', str(_3))
    change_all_occurrences('23', str(_23))
    change_all_occurrences('33', str(_33))
    change_all_occurrences('numpy_func', numpy_func)

    
    # answers
    change_all_occurrences(r'\verb+a+', r'\verb+' + a + '+')
    change_all_occurrences(r'\verb+e+', r'\verb+' + e + '+')
    
    # indexes with no repetitions
    [_5] = sample(range(_13), 1)

    _2 = randint(0,1)
    if _2 == 0:
        change_all_occurrences(r'\verb+2+', r'\verb+' + pt_e + '+')
    if _2 == 1:
        change_all_occurrences(r'\verb+2+', r'\verb+' + pt_nao + '+')
    _3_funcs = ['np.vstack(' + b + ', ' + c + ')', 'np.hstack((' + b + ', ' + c + '))',
                'np.vstack(' + b + ', ' + d + ')', 'np.hstack((' + b + ', ' + d + '))',
                'np.vstack(' + c + ', ' + b + ')', 'np.hstack((' + c + ', ' + b + '))',
                'np.vstack(' + c + ', ' + d + ')', 'np.hstack((' + c + ', ' + d + '))',
                'np.vstack(' + d + ', ' + b + ')', 'np.hstack((' + d + ', ' + b + '))',
                'np.vstack(' + d + ', ' + c + ')', 'np.hstack((' + d + ', ' + c + '))',
                'np.vstack((' + b + ', ' + c + '))', 'np.vstack((' + c + ', ' + d + '))',
                'np.vstack((' + b + ', ' + d + '))', 'np.vstack((' + d + ', ' + c + '))',
                'np.hstack(' + b + ', ' + c + ')', 'np.vstack(([], []))',
                'np.hstack(' + b + ', ' + d + ')', 'np.vstack((' + d + ', ' + d + '))',
                'np.hstack(' + c + ', ' + b + ')', 'np.vstack((' + c + ', ' + c + '))',
                'np.hstack(' + c + ', ' + d + ')', 'np.vstack((' + b + ', ' + b + '))',
                'np.hstack(' + d + ', ' + b + ')']
    
    [_3_idx] = sample(range(len(_3_funcs)), 1)
    change_all_occurrences(r'\verb+3+', r'\verb+' + _3_funcs[_3_idx] + '+')
    if _3_idx % 2 == 0:
        answer_3_true = pt_lancar + ' um erro'
        if _3_idx < 15:
            answer_3_false = 'originar um numpy array de 2 ' + pt_dimensoes
        else:
            answer_3_false = 'originar um numpy array de 1 ' + pt_dimensao
        change_all_occurrences(r'\verb+33+', answer_3_true)
        change_all_occurrences(r'\verb+333+', answer_3_false)
            
    if _3_idx % 2 != 0:
        if _3_idx < 12:
            answer_3_true = 'originar um numpy array de 1 ' + pt_dimensao
            answer_3_false = 'originar um numpy array de 2 ' + pt_dimensoes
        else:
            answer_3_true = 'originar um numpy array de 2 ' + pt_dimensoes
            option_answer_3_false = 'originar um numpy array de 1 ' + pt_dimensao
            answer_3_false = choice((pt_lancar + ' um erro', option_answer_3_false))
        change_all_occurrences(r'\verb+33+', answer_3_true)
        change_all_occurrences(r'\verb+333+', answer_3_false)


    _5_dimension = choice((1, 2))
    if _5_dimension == 1:
        _5 = choice(('-2', '-1', '0', ':', '1'))
        _5 = _5 + ', :' 
    if _5_dimension == 2:
        _5 = ':, ' + str(randint(-_23, _23))
    change_all_occurrences(r'\verb+5+', r'\verb+' + f + '[' + str(_5) + ']+')

    # true answer
    _1_t, answer_1_true = quest_1(maneiras_corretas, maneiras_incorretas, True)
    change_all_occurrences(r'\verb+1_t+', r'\verb+' + _1_t + '+')
    change_all_occurrences(r'\verb+11+', answer_1_true)
    # false answer
    _1_f, answer_1_false = quest_1(maneiras_corretas, maneiras_incorretas, False)
    change_all_occurrences(r'\verb+1_f+', r'\verb+' + _1_f + '+')
    change_all_occurrences(r'\verb+111+', answer_1_false)

def make_transformations_on_results(program):
    ''

    global a
    global e
    global f
    global _1_t
    global _1_f
    global _2
    global _3
    global _4
    global _5


    the_list = program.get_global(a)
    the_list_e = program.get_global(e)
    the_list_f = program.get_global(f)
    
    answer_2_true = possible_shape(len(the_list)) if _2 == 0 \
                    else possible_shape(len(the_list) + choice([1, -1]))
    answer_4_true = np.shape(the_list_e)
    answer_5_true = quest_5(the_list_f)

    # true answers
    change_all_occurrences(r'\verb+22+', str(answer_2_true))
    change_all_occurrences(r'\verb+44+', str(answer_4_true))
    change_all_occurrences(r'\verb+55+', str(answer_5_true))

    # wrong answers
    increment5 = choice([1, -1])

    
    answer_2_false = possible_shape(len(the_list)) if _2 == 1 \
                    else possible_shape(len(the_list) + choice([1, -1]))
    answer_4_false = wrong_shape(answer_4_true)
    answer_5_false = quest_5_wrong_answer(the_list_f, answer_5_true)

    change_all_occurrences(r'\verb+222+', str(answer_2_false))
    change_all_occurrences(r'\verb+444+', str(answer_4_false))
    change_all_occurrences(r'\verb+555+', str(answer_5_false))
    

def func_quest_1(arr, chosen_one):
    result = 0
    while True:
        result = choice((arr))
        if result != chosen_one:
            break
    return result

def quest_1(list_correct, list_wrong, true_answer):
    decision = choice(('correct', 'wrong'))
    if decision == "correct":
        answer = "correta" if true_answer else "incorreta"
        return func_quest_1(list_correct, numpy_func), answer
    answer = "incorreta" if true_answer else "correta"
    return choice((list_wrong)), answer 
    
    

def possible_shape(num):
    idxs = [x for x in range(101)]
    idxs = idxs[1:]
    idxs = idxs[::-1]
    nums_remainder_0 = [x for x in idxs if (num % x)== 0]
    result = []
    result.append(choice(nums_remainder_0))
    result.append(int(num / result[0]))
    shuffle(result)
    return result


def wrong_shape(shape):
    wrong_shapes = ['(' + str(shape[1]) + ', ' + str(shape[0]) + ')',
                    '(' + str(shape[0]) + ', )', '(' + str(shape[0] - 1 ) + ', )',
                    '(' + str(shape[0] * shape[1]) + ', )',
                    '(' + str(shape[0] - 1 ) + ', ' + str(shape[1]) + ')']
    return choice((wrong_shapes))

def quest_5(the_list):
    idx = _5.split(', ')
    if _5_dimension == 1:
        idx = idx[0]
        answer = 'array completo' if idx == ':' else 'array constituido somente por letras' \
               if int(idx) % 2 == 0 else str('array constituido somente por ' + pt_numeros)
        return pt_e + ' ' + answer
    return 'pode ser ' + str(the_list[:,int(idx[1])])

def quest_5_wrong_answer(the_list, true_answer):
    answer = None
    if _5_dimension == 1:
        while True:
            answer = choice((['array completo', 'array constituido somente por letras',
                              'array constituido somente por ' + pt_numeros]))
            if answer != true_answer:
                break
        return pt_e + ' ' + answer
    while True:
        idx = randint(-_23, _23)
        answer = str(the_list[:, idx])
        if answer != true_answer:
            break
    return 'pode ser ' + answer





        
    
