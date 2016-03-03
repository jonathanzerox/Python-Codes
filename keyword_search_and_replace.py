"""
Program: Python Script that searches a file for specific keywords and replaces the word
Reason: I had to replace database settings on many php files so i decided to automate the process with .py
Author: Jonathan Zerox
Date: Thurs - 3rd - March - 2015
CS Concepts Used: Recursion
"""

import os, sys

def walk_dir(cur_dir):

    old_file = ''   # variable to hold filename for the original file
    new_file = ''   # variable to hold filename for the new file/file with replaced keyword

    for file_name in os.listdir(cur_dir):
        if(file_name[-3:] == 'php' and os.path.isfile(cur_dir+"/"+file_name)):

            with(open(os.path.abspath(cur_dir+"/"+file_name), 'r')) as open_file:
                file_contents = open_file.read()
                split_data = str(file_contents).replace('Connections/connect.php', 'config/db_settings.php').split(' ')

                old_file = open_file.name
                another_file = open(os.path.abspath(cur_dir+'/'+'another_file.txt'), 'w')
                another_file.writelines(" ".join(split_data))

                new_file = another_file.name

                another_file.close()

            # after copying the contents file1 to file2 we then rename file2 to the name of file1 then remove file1 and keep file2(whose name has been changed to file1)
            os.remove(old_file)
            os.rename(new_file, old_file)

        if(os.path.isdir(cur_dir+'/'+file_name)):
            walk_dir(cur_dir+'/'+file_name)

if __name__ == '__main__':
    walk_dir(os.curdir)

