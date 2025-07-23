filepath = r'UTILITIES\FORMATTING\Convert_file_to_lower_case\file.txt'
filepath_lower = r'UTILITIES\FORMATTING\CONVERT_FILE_TO_LOWER_CASE\file_lower.txt'
combined_file = r'UTILITIES\FORMATTING\CONVERT_FILE_TO_LOWER_CASE\combined_file.txt'

def open_file_convert_lower(filepath):
    with open(filepath, 'r') as file:
        file_convert = file.readlines()
        lowercase_lines = [line.lower() for line in file_convert]
    return lowercase_lines   
    

def write_file_lowercase(file, lower_arg):
    with open(file, 'w') as file:
            file.writelines(lower_arg)

def combine_file(filepath_arg, filepath_lower_arg, combined_file_arg):
    try:
        with open(filepath_lower_arg, 'r') as f1, open(filepath_arg, 'r') as f2, open(combined_file_arg, 'w') as file:
            for line1, line2 in zip(f1, f2):
                line1 = line1.replace('\n', "")
                line1 = line1 + "|" + line2
                file.write(line1)
                
    except FileNotFoundError:
        print("One or both files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
     

if filepath !=" ":
    lowercase = open_file_convert_lower(filepath)
    write_file_lowercase(r'UTILITIES\FORMATTING\Convert_file_to_lower_case\file_lower.txt', lowercase)
    combine_file(filepath, filepath_lower, combined_file)


else:
     print("No workie")