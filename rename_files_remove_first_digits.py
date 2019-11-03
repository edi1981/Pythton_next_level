import os
import string


def rename_file():
    """ the function opens specific folder, lists it, and then removes didgits from the
      beginning of the file name and renames the files in our folder"""
    file_list = os.listdir("D:/Users/pbutkowski/Desktop/prank")
    os.chdir("D:/Users/pbutkowski/Desktop/prank")
    for file_name in file_list:
        os.rename(file_name, file_name.lstrip("0123456789 "))


rename_file()
