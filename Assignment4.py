import random

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
    
def alter_text(text_list):
    altered_text = []

    for i, line in enumerate(text_list):
        line = line.strip

        line_with_number = f"{i + 1}: {line}"

        if len(line) > 20:
            line_with_number = line_with_number.lower()
        else:
            line_with_number = line_with_number.upper()
        
        altered_text.append(line_with_number)

    line_to_omit = random.choice(range(len(altered_text)))
    altered_text.pop(line_to_omit)

    return altered_text

def output_text(text_list):
    for line in text_list:
        print(line)