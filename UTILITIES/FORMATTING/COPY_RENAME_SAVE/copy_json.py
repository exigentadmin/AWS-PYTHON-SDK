import os

# Create a dummy JSON file for demonstration
with open("data.json", "w") as f:
    f.write('{"key": "value"}')

old_file_name = "data.json"
new_file_name = "renamed_data.json"

try:
    os.rename(old_file_name, new_file_name)
    print(f"File '{old_file_name}' successfully renamed to '{new_file_name}'.")
except FileNotFoundError:
    print(f"Error: File '{old_file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")