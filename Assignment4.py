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

def save_to_file(file_path, text_list):
    with open(file_path, 'w') as file:
        for line in text_list:
            file.write(line + '\n')

def main():
    original_text = read_file('ateam_Original.txt')

    print("-" * 40)
    print("Original Text")
    print("-" * 40)
    output_text(original_text)

    altered_text = alter_text(original_text)

    print("\n-" * 40)
    print("Altered Text")
    print("-" * 40)
    output_text(altered_text)