import random

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
    
def alter_text(text_list):
    altered_text = []