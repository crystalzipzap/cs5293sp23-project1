import os

def add_txt_extension(path_folder):
    for file in os.listdir(path_folder):
        old_file_path = os.path.join(path_folder, file)
        new_file_path = os.path.join(path_folder, f"{file}.txt")
        os.rename(old_file_path, new_file_path)