filepath = r'UTILITIES\FORMATTING\CONVERT_FILE_TO_UPPERCASE\file.txt'
filepath_upper = r'UTILITIES\FORMATTING\CONVERT_FILE_TO_UPPER_CASE\file_upper.txt'
combined_file = r'UTILITIES\FORMATTING\CONVERT_FILE_TO_UPPER_CASE\combined_file.txt'

def open_file_convert_upper(filepath):
    with open(filepath, 'r') as file:
        file_convert = file.readlines()
        uppercase_lines = [line.upper() for line in file_convert]
    return uppercase_lines   
    

def write_file_uppercase(file, upper_arg):
    with open(file, 'w') as file:
            file.writelines(upper_arg)

def combine_file(filepath_arg, filepath_upper_arg, combined_file_arg):
    try:
        with open(filepath_upper_arg, 'r') as f1, open(filepath_arg, 'r') as f2, open(combined_file_arg, 'w') as file:
            for line1, line2 in zip(f1, f2):
                line1 = line1.replace('\n', "")
                line1 = line1 + "|" + line2
                file.write(line1)
                
    except FileNotFoundError:
        print("One or both files not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
     

if filepath !=" ":
    uppercase = open_file_convert_upper(filepath)
    write_file_uppercase(r'UTILITIES\FORMATTING\CONVERT_FILE_TO_UPPERCASE\file_upper.txt', uppercase)
    combine_file(filepath, filepath_upper, combined_file)


else:
     print("No workie")