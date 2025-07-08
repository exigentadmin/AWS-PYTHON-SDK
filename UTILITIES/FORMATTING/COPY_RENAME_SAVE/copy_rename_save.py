import shutil
import os
import json


# Define the source file path and the destination directory
source_file = "config_chat_template.json"
destination_directory = r"UTILITIES\FORMATTING\COPY_RENAME_SAVE\NEW_FILES"

with open (r"UTILITIES\FORMATTING\COPY_RENAME_SAVE\file_lower.txt", 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        #line = "".join(([line, ".json"]))
        print(line)
        try:
            # Construct the full path for the new file
            destination_file = os.path.join(destination_directory, line, ".json" ) 
            # Copy the file from the source to the destination with the new name
            shutil.copyfile(source_file, destination_file)
            print(f"File '{source_file}' copied and renamed to '{destination_file}' successfully.")
        except FileNotFoundError:
            print(f"Error: Source file '{source_file}' not found.")
        except PermissionError:
            print(f"Error: Permission denied to access '{source_file}' or '{destination_directory}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")