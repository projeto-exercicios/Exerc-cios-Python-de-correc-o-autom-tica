
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
add_changeable('e')      # global variable
add_changeable('M')      # class
add_changeable('m')      # class variable
add_changeable('x')      # the loop variable in list comprehensions
add_changeable('n')      # the loop variable. this was added after an
                         # error ocurred. see ERROR below

add_changeable('13')     # the list length
add_changeable('33')     # min int num
add_changeable('66')     # max int num
add_changeable('35')     # global var to change
add_changeable('36')     # global var to change

# answers list name
add_changeable(r'\verb+a+')
add_changeable(r'\verb+class+')

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
_5 = None
_35 = None
_36 = None




def make_transformations():

    ''
    global a
    global _1
    global _2
    global _5
    global _35
    global _36
    
    # question
    _135 = str(randint(1000000, 2000000))
    [a, n, e, M, m, x] = sample(string.ascii_lowercase, 6)
    _13 = randint(19000, 20000)
    _33 = randint(1, 5000)
    _66 = randint(5000, 10000)
    _35 = randint(1,17984)
    _36 = _35 + 1
    
    change_all_occurrences('135', _135)
    change_token_all_occurrences('a', a)
    change_token_all_occurrences('n', n)
    change_token_all_occurrences('e', e)
    change_token_all_occurrences('m', m)
    change_token_all_occurrences('M', M)
    change_token_all_occurrences('x', x)
    change_all_occurrences('13', str(_13))
    change_all_occurrences('33', str(_33))
    change_all_occurrences('66', str(_66))

    # answers
    change_all_occurrences(r'\verb+a+', r'\verb+' + a + '+')
    change_all_occurrences(r'\verb+class+', r'\verb+' + M + '+')
    functions = {'print_v1()':'NameError',
                 'print_v1(' + str(e) + ')': 'NameError',
                 'print_v2()': 'NameError',
                 'print_v2(' + str(e) + ')': 'NameError',
                 'print_v3()': 'TypeError',
                 str(M) + '.print_v1()':'TypeError',
                 str(M) + '.print_v2(' + str(e) + ')':'TypeError',
                 str(M) + '.print_v3(' + str(e) + ')':'AttributeError',
                 str(m) + '.print_v1(' + str(e) + ')': 'TypeError',
                 str(m) + '.print_v2(' + str(e) + ')': 'TypeError',
                 str(m) + '.print_v3(' + str(e) + ')':'AttributeError',
                 str(M) + '.print_v1(' + str(e) + ')': str(_36),
                 str(m) + '.print_v1()': "function print_v1",
                 str(M) + '.print_v2()':'function print_v2',
                 'print_v3(' + str(e) + ')': str(_36)}
    
    # indexes with no repetitions
    [ _5] = sample(range(_13), 1)
    
    idx = choice(range(len(functions)))
    _1 = list(functions.values())[idx]
    _2 = choice(('pares','impares'))
    change_all_occurrences(r'\verb+1+', r'\verb+' + list(functions.keys())[idx] + '+')
    change_all_occurrences(r'\verb+2+', r'\verb+' + str(_2) + '+')
    change_all_occurrences(r'\verb+5+', r'\verb+' + str(_5) + '+')

    



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global a
    global _1
    global _2
    global _5
    global _35
    global _36


    the_list = program.get_global(a)
    even = program.get_global('even')
    odd = program.get_global('odd')
    fixed_nums_list = program.get_global('fixed_nums_list')
    answer_4 = program.get_global('answer_4_true')
    answer_1_true = _1
    answer_2_true = len(even) if _2 == 'pares' else len(odd)
    answer_3_true = fixed_nums_list
    answer_4_true = answer_4
    answer_5_true = the_list[_5]

    # true answers
    change_all_occurrences(r'\verb+11+', str(answer_1_true))
    change_all_occurrences(r'\verb+22+', str(answer_2_true))
    change_all_occurrences(r'\verb+33+', str(answer_3_true))
    change_all_occurrences(r'\verb+44+', str(answer_4_true))
    change_all_occurrences(r'\verb+55+', str(answer_5_true))

    # wrong answers
    increment3 = choice([1, -1])
    increment4 = choice([1, -1])
    increment5 = choice([1, -1])

    answer_1_false = false_answer_1(answer_1_true)
    answer_2_false = len(odd) if _2 == 'pares' else len(even)
    answer_3_false = false_answer_3(the_list).sort()
    answer_4_false = "impares que pares" if even > odd else "pares que impares" 
    answer_5_false = answer_5_true + increment5

    change_all_occurrences(r'\verb+111+', str(answer_1_false))
    change_all_occurrences(r'\verb+222+', str(answer_2_false))
    change_all_occurrences(r'\verb+333+', str(answer_3_false))
    change_all_occurrences(r'\verb+444+', str(answer_4_false))
    change_all_occurrences(r'\verb+555+', str(answer_5_false))
    
def false_answer_1(true_answer):
    outputs = ['NameError', 'TypeError', 'AttributeError', str(_35), str(_36), "function print_v1",
               'function print_v2']
    result = ''
    while True:
        result = choice(outputs)
        if result != true_answer:
            break
    return result

def false_answer_3(List):
    length = randint(2,6)
    result = []
    while True:
        num = choice(List)
        if num != List[num]:
            result.append(num)
        if len(result) == length:
            break
    return result
