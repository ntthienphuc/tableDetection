import os
import shutil


def merge_folders(folder1, folder2, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # Copy files from folder1 to output folder
    for item in os.listdir(folder1):
        s = os.path.join(folder1, item)
        d = os.path.join(output_folder, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, False, None)
        else:
            shutil.copy2(s, d)

    # Copy files from folder2 to output folder
    for item in os.listdir(folder2):
        s = os.path.join(folder2, item)
        d = os.path.join(output_folder, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, False, None)
        else:
            shutil.copy2(s, d)
