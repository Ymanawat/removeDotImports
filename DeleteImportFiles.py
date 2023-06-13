import os
import send2trash

def move_import_files(source_dir):
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".import"):
                file_path = os.path.join(root, file)
                send2trash.send2trash(file_path)
                print(f"Moved {file_path} to recycle bin")

# Specify the source directory
source_directory = "."  # Directory where the script is run

move_import_files(source_directory)
