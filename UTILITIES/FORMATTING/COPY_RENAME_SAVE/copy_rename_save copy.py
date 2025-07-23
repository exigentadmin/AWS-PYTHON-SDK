import shutil
import os
import json


# Define the source file path and the destination directory
source_file = r"UTILITIES\FORMATTING\COPY_RENAME_SAVE\config_chat_template.json"
destination_directory = r"UTILITIES\FORMATTING\COPY_RENAME_SAVE\file_lower.txt"
filepath = r"UTILITIES\FORMATTING\COPY_RENAME_SAVE\file_lower.txt"

if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)
    print(f"Created directory: {destination_directory}")

#filepath = os.path.join(destination_directory, 'file_lower.txt')

with open (filepath, 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        line = "".join(([line, ".json"]))
        #print(line)
        try:
            with open(source_file, 'r') as f:
                data = json.load(f)
                print(data)
            with open(line, 'w') as f:
                json.dump(data, f, indent=4)
        # except FileNotFoundError as ex:
        #     print(f"Error: Source file '{source_file}' not found.", {ex})
        # except PermissionError:
        #     print(f"Error: Permission denied to access '{source_file}' or '{destination_directory}'.")
        # except Exception as e:
        #     print(f"An unexpected error occurred: {e}")
        except:
            print("No workie")