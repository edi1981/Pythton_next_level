import os
import string


def rename_file():
    """ the function opens specific folder, lists it, and then removes all didgits from the
          the file name and renames the files in our folder"""
    file_list = os.listdir("D:/Users/pbutkowski/Desktop/prank")
    saved_path = os.getcwd()
    os.chdir("D:/Users/pbutkowski/Desktop/prank")

    for file_name in file_list:
        translation_table = str.maketrans("0123456789", "          ", "0123456789")
        os.rename(file_name, file_name.translate(translation_table))
    os.chdir(saved_path)


rename_file()
