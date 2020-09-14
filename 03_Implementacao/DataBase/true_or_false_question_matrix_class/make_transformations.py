
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
add_changeable('n')      # the loop variable. this was added after an
                         # error ocurred. see ERROR below
add_changeable('13')     # the list length
add_changeable('133')    # matrix min value
add_changeable('255')    # matrix max value

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

# answers variables
add_changeable(r'\verb+cl_1+')
add_changeable(r'\verb+cl_2+')
add_changeable(r'\verb+idx_m1+')
add_changeable(r'\verb+idx_m2+')
add_changeable(r'\verb+v1+')
add_changeable(r'\verb+v2+')
add_changeable(r'\verb+answer_2_decision+')
add_changeable(r'\verb+answer_2_index+')


# variáveis partilhas entre as funções make_transformations e
# make_transformations_on_results
a  = None
_1 = None
_3 = None
_4 = None
_5 = None
idx_m1 = None
idx_m2 = None
answer_2_decision = None
answer_2_index = None
cl_1 = None
cl_2 = None
v1 = None
v2 = None


def make_transformations():

    ''
    global a
    global _1
    global _3
    global _4
    global _5
    global idx_m1
    global idx_m2
    global answer_2_decision
    global answer_2_index
    global cl_1
    global cl_2
    global v1
    global v2
    
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
    [a, n] = sample(string.ascii_lowercase, 2)
    _13 = randint(19000, 20000)
    _133 = randint(-50, 100)
    _255 = randint(101, 255)
    
    change_all_occurrences('135', _135)
    change_token_all_occurrences('a', a)
    change_token_all_occurrences('n', n)
    change_all_occurrences('13', str(_13))
    change_all_occurrences('133', str(_133))
    change_all_occurrences('255', str(_255))

    idx_m1, idx_m2 = idx_getter(_13)
    cl_1, v1, cl_2, v2 = cl_v_getter()
    answer_2_decision = choice(("coluna", "linha"))
    answer_2_index = choice(range(3))
    answer_2_index_str = "primeira" if answer_2_index == 0 else "segunda" if answer_2_index == 1 else "terceira"
    change_all_occurrences(r'\verb+cl_1+', r'\verb+' + cl_1 + '+')
    change_all_occurrences(r'\verb+cl_2+', r'\verb+' + cl_2 + '+')
    change_all_occurrences(r'\verb+v1+', r'\verb+' + str(v1) + '+')
    change_all_occurrences(r'\verb+v2+', r'\verb+' + str(v2) + '+')
    change_all_occurrences(r'\verb+idx_m1+', r'\verb+' + str(idx_m1) + '+')
    change_all_occurrences(r'\verb+idx_m2+', r'\verb+' + str(idx_m2) + '+')
    change_all_occurrences(r'\verb+answer_2_decision+', r'\verb+' + str(answer_2_decision) + '+')
    change_all_occurrences(r'\verb+answer_2_index+', r'\verb+' + answer_2_index_str + '+')
    # answers
    change_all_occurrences(r'\verb+a+', r'\verb+' + a + '+')
    
    # indexes with no repetitions
    [_1,  _3, _4, _5] = sample(range(_13), 4)

    change_all_occurrences(r'\verb+1+', r'\verb+' + str(_1) + '+')
    change_all_occurrences(r'\verb+2+', r'\verb+' + str(idx_m1) + '+')
    change_all_occurrences(r'\verb+3+', r'\verb+' + str(_3) + '+')
    change_all_occurrences(r'\verb+4+', r'\verb+' + str(_4) + '+')
    change_all_occurrences(r'\verb+5+', r'\verb+' + str(_5) + '+')

    



def make_transformations_on_results(program):
    ''
    # os global aqui não são precisos porque não se faz nesta função
    # atribuição a estas variáveis. Só está para para tornar explícito
    # que são variáveis globais partilhadas
    global a
    global _1
    global _3
    global _4
    global _5
    global idx_m1
    global idx_m2
    global answer_2_decision
    global answer_2_index
    global cl_1
    global cl_2
    global v1
    global v2
    
    the_list = program.get_global(a)
    m1 = the_list[idx_m1]
    m2 = the_list[idx_m2]
    m3 = the_list[_3]
    m4 = the_list[_4]
    m5 = the_list[_5]
    
    answer_1_true = m1.row_times_column(cl_1, v1, m2, cl_2, v2)
    if answer_2_decision == "coluna":
        answer_2_true = m1.get_coluna(answer_2_index)
    if answer_2_decision == "linha":
        answer_2_true = m1.get_linha(answer_2_index) 
    answer_3_true = m3.matrix_cross_product()
    answer_4_true = m4.mult_by_itself()
    answer_5_true = m5.std()

    # true answers
    change_all_occurrences(r'\verb+11+', str(answer_1_true))
    change_all_occurrences(r'\verb+22+', str(answer_2_true))
    change_all_occurrences(r'\verb+33+', str(answer_3_true))
    change_all_occurrences(r'\verb+44+', str(answer_4_true))
    change_all_occurrences(r'\verb+55+', str(answer_5_true))

    # wrong answers
    increment1 = choice([1, -1])
    increment3 = choice([1, -1])
    increment5 = choice([1, -1])

    answer_1_false =answer_1_true + increment1
    if answer_2_decision == "coluna":
        answer_2_false = m1.get_linha(answer_2_index)
    if answer_2_decision == "linha":
        answer_2_false = m1.get_coluna(answer_2_index)
    if answer_2_false == answer_2_true:
        answer_2_false = get_answer_2_false(the_list, answer_2_decision, answer_2_true)
    answer_3_false = m1.matrix_cross_product() if answer_3_true != m1.matrix_cross_product() else m1.matrix_cross_product() + increment3
    answer_4_false = m2.mult_by_itself() if answer_4_true != m2.mult_by_itself() else get_answer_4_false(the_list, answer_4_true)
    answer_5_false = m1.std() if answer_5_true != m1.std() else m1.std() + increment5

    change_all_occurrences(r'\verb+111+', str(answer_1_false))
    change_all_occurrences(r'\verb+222+', str(answer_2_false))
    change_all_occurrences(r'\verb+333+', str(answer_3_false))
    change_all_occurrences(r'\verb+444+', str(answer_4_false))
    change_all_occurrences(r'\verb+555+', str(answer_5_false))
    
def idx_getter(length):
    idx_m1 = choice(range(length))
    while True:
        idx_m2 = choice(range(length))
        if idx_m2 != idx_m1:
            break
    return idx_m1, idx_m2
def cl_v_getter():
    cl_1 = choice(("coluna", "linha"))
    cl_2 = choice(("coluna", "linha"))
    if cl_1 == "coluna":
        v1 = choice(range(3))
    if cl_1 == "linha":
        v1 = choice(range(3))
    if cl_2 == "coluna":
        v2 = choice(range(3))
    if cl_2 == "linha":
        v2 = choice(range(3))
    return cl_1, v1, cl_2, v2

def get_answer_2_false(the_list, answer_2_decision, true_answer):
    idx = 0
    while True:
        if answer_2_decision == "coluna":
            answer_2_false = the_list[idx].get_linha(answer_2_index)
        if answer_2_decision == "linha":
            answer_2_false = the_list[idx].get_coluna(answer_2_index)
        if answer_2_false != true_answer:
            break
        idx += 1
    return answer_2_false

def get_answer_4_false(the_list, true_answer):
    idx = 0
    while True:
        answer_4_false = the_list[idx].mult_by_itself()
        if answer_4_false != true_answer:
            break
        idx += 1
    return answer_4_false
