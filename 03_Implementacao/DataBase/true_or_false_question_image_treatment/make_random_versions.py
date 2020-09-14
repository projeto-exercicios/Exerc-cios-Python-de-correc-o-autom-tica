
import logging

logging.basicConfig(filename='make_random_versions.log', level=logging.DEBUG)





from util_make_random_versions import make_random_versions





# configuration

# variable used to write or read the seed in each version directory
write_seed_flag = True

# files that remain unchanged
fixed_files_list = [
    'questiom.sty',
    'latex_packages.tex'
]

# files to change
general_files_to_change_list = [
    'true_or_false_question.tex',
    "answer_1_true.tex",
    "answer_1_false.tex",
    'answer_2_true.tex',
    'answer_2_false.tex',
    'answer_3_true.tex',
    'answer_3_false.tex',
    'answer_4_true.tex',
    'answer_4_false.tex',
    'answer_5_true.tex',
    'answer_5_false.tex'
]

# a list of ['true_anwser.tex', 'false_answer.tex', 'answer.tex'] a
# random choice of 'true_anwser.tex' is made 'false_answer.tex' and a
# shortcut is created from the chosen one to 'answer.tex'
true_or_false_alternative_answers = [
    ['answer_1_true.tex', 'answer_1_false.tex', 'true_or_false_answer_1.tex'],
    ['answer_2_true.tex', 'answer_2_false.tex', 'true_or_false_answer_2.tex'],
    ['answer_3_true.tex', 'answer_3_false.tex', 'true_or_false_answer_3.tex'],
    ['answer_4_true.tex', 'answer_4_false.tex', 'true_or_false_answer_4.tex'],
    ['answer_5_true.tex', 'answer_5_false.tex', 'true_or_false_answer_5.tex'],
]

# python code files to process. this files are always executed as a
# single program (all files in the list are concatenated, before
# executed, in the order they appear in the list, ).
python_files_list = [
    'program.py',
    'answers_program.py'
]

# programs to run: a list of programs.
# each program is a list of:
# 1. a list of files to concatenate
# 2. the program filename where the source will be stored
# 3. the output filename where the output will be stored
# NOTE: the last program is the one which is passed to
# make_transformations_on_results. It must be the answers program.
programs_to_run = [
    [['program.py', 'answers_program.py'],
     'full_program.py',
     'full_program_output.txt' ]
]

seed_filename         = "seed.txt"
# the script that randomlly generates values for text and python files
make_transformations_script_filename = "make_transformations"

# number of versions to create
number_of_versions = 2
# version directory prefix (it is added with the version number)
version_path_prefix = "question/version_"





make_random_versions(general_files_to_change_list,
                     python_files_list,
                     programs_to_run,
                     seed_filename,
                     make_transformations_script_filename,
                     number_of_versions,
                     version_path_prefix,
                     write_seed_flag,
                     true_or_false_alternative_answers,
                     fixed_files_list)


