filepath = r'UTILITIES\FORMATTING\Convert_file_to_lower_case\file.txt'

def open_file_convert_lower(filepath):
    with open(filepath, 'r') as file:
        file_convert = file.readlines()
        lowercase_lines = [line.lower() for line in file_convert]
    return lowercase_lines


def write_file(file, lower_arg):
    with open(file, 'w') as file:
            file.writelines(lower_arg)


if filepath !=" ":
    lowercase = open_file_convert_lower(filepath)
    write_file(r'UTILITIES\FORMATTING\Convert_file_to_lower_case\file_lower.txt', lowercase)
else:
     print("No workie")