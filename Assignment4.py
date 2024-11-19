import random

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
    
def alter_text(text_list):
    altered_text = []

    for i, line in enumerate(text_list):
        line = line.strip

        line_with_number = f"{i + 1}: {line}"