"""
Program: Python Script that searches a file for specific keywords and replaces the word
Reason: I had to replace database settings on many php files so i decided to automate the process with .py
Author: Jonathan Zerox
Date: Thurs - 3rd - March - 2015
"""

import os, sys

old_file = ''
new_file = ''

for files in os.listdir(os.curdir):
    if(files[-3:] == 'php'):
        with(open(files, 'r')) as open_file:
            file_contents = open_file.read()
            split_data = str(file_contents).replace('Connections/connect.php', 'config/db_settings.php').split(' ')

            old_file = open_file.name
            another_file = open('another_file.txt', 'w') 
            another_file.writelines(" ".join(split_data))

            new_file = another_file.name

            another_file.close()

        os.remove(old_file)
        os.rename(new_file, old_file)
        
