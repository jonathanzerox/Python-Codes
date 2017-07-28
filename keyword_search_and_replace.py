"""
Program: Python Script that searches a file for specific keywords and replaces the word
Reason: I had to replace database settings on many php files so i decided to automate the process with .py
Author: Jonathan Zerox
Date: Thurs - 3rd - March - 2016
Location: KillaDesigns
CS Concepts Used: Recursion
"""

import os, sys

def walk_dir(cur_dir):

    old_file = ''   # variable to hold filename for the original file
    new_file = ''   # variable to hold filename for the new file/file with replaced keyword

    for file_name in os.listdir(cur_dir):
        file_path = os.path.join(cur_dir, file_name)
        if os.path.isfile(file_path) and file_name.split('.')[-1] == 'php':

            with open(file_path, 'r') as open_file:
                file_contents = open_file.read()
                split_data = str(file_contents).replace('Connections/connect.php', 'config/db_settings.php').split(' ')

                old_file = open_file.name
                another_file = open(os.path.join(cur_dir, 'another_file.txt'), 'w')
                another_file.writelines(" ".join(split_data))

                new_file = another_file.name

                another_file.close()

            # after copying the contents file1 to file2 we then rename file2 to the name of file1 then remove file1 and keep file2(whose name has been changed to file1)
            os.remove(old_file)
            os.rename(new_file, old_file)

        if(os.path.isdir(file_path)):
            walk_dir(file_path)

if __name__ == '__main__':
    walk_dir(os.curdir)

