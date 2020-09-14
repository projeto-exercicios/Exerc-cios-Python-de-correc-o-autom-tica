
# configuration

version_path_prefix = "question/version_"

tex_files_to_process = [
    'true_or_false_question.tex',
    'answer_1_true.tex',
    'answer_1_false.tex',
    'true_or_false_answer_1.tex',
    'answer_2_true.tex',
    'answer_2_false.tex',
    'true_or_false_answer_2.tex',
    'answer_3_true.tex',
    'answer_3_false.tex',
    'true_or_false_answer_3.tex',
    'answer_4_true.tex',
    'answer_4_false.tex',
    'true_or_false_answer_4.tex',
    'answer_5_true.tex',
    'answer_5_false.tex',
    'true_or_false_answer_5.tex'
]

# configuration end





import os
import logging

from pathlib import Path

logging.basicConfig(filename='make_pdfs.log', level=logging.DEBUG)





def process_version(version_path):

    current_directory = Path.cwd()
    
    for tex_file in tex_files_to_process:

        #command = 'cd ' + version_path + '; pdflatex ' + tex_file
        os.chdir(version_path)

        command = 'pdflatex ' + tex_file
        
        logging.debug(command)
        os.system(command)

        os.chdir(current_directory)



        
        
version      = 1
version_path = version_path_prefix + str(version)

while os.path.exists(version_path):

    process_version(version_path)
    
    version      = version + 1
    version_path = version_path_prefix + str(version)
    
