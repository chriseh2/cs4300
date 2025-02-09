# Homework 1 - Task 6: File Handling and Metaprogramming
# UCCS SP2025 CS4300-2, Dr. Kristen Walcott (instructor)
# Created by Christopher Helland (student)
# Due: February 10, 2025

# -- Assignment: --
# Then write a program inside task6.py of that reads task6_read_me.txt and counts the number
# of words in it. Implement metaprogramming techniques to dynamically generate function names
# for your pytest test cases based on the filenames of the text files. Include pytest test cases that verify
# the word count for each text file.

import pytest

# Function wordCount that opens a file whose relative path is variable:filePath and counts the number of words contained inside the file
# A word can be separated by a Separation Character: " " or '\n' or '\t'
def wordCount(filePath):
    words = 0 # holds number of words located
    inWordState = False # When True, the loop is iterating through any character that is not a Separation Character

    # Open file and load its content in variable:content
    file = open(filePath, mode='r')
    content = file.read()
    
    # Loop through each character in variable:content, then increment variable:words by one if a Separation Character is located following a Non-Separation Character
    size = len(content)
    i = 0 # counter
    while i < size:
        currentChar = content[i]

        # If currentChar is a not a Separation Character AND is not currently inWordState, a new word has been found
        if isSeparationCharacter(currentChar) == False and inWordState == False:
            inWordState = True
            words+=1

        # if currentChar is a Separation Character AND currently inWordState, the word has ended, switch inWordState to False
        if isSeparationCharacter(currentChar) == True and inWordState == True:
            inWordState = False
        
        i+=1

    # Close file
    file.close()

    # Return word count
    return words

def isSeparationCharacter(currentChar):
    # If currentChar is a Separation Character, return True
    if currentChar == " " or currentChar == '\n' or currentChar == '\t':
        return True
    else:
        return False

# Tests

test_files = [ # (test_file_path, expected_word_count)
    ("cs4300/task6_test_files/task6_read_me.txt", 104),
    ("cs4300/task6_test_files/test1_91.txt", 91),
    ("cs4300/task6_test_files/test2_104.txt", 104),
    ("cs4300/task6_test_files/test3_129.txt", 129),
    ("cs4300/task6_test_files/test4_0.txt", 0),
    ("cs4300/task6_test_files/test5_25.txt", 25),
]

@pytest.mark.parametrize("test_file_path,expected_word_count", test_files)
def test_wordCount(test_file_path, expected_word_count):
    assert wordCount(test_file_path) == expected_word_count