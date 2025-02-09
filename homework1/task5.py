# Homework 1 - Task 5: Lists and Dictionaries
# UCCS SP2025 CS4300-2, Dr. Kristen Walcott (instructor)
# Created by Christopher Helland (student)
# Due: February 10, 2025

# -- Assignment: --
# Create a new file named task5.py and inside create a list of of your favorite books, including book
# titles and authors. Use list slicing to print the first three books in the list. Create a dictionary that
# represents a basic student database, including student names and their corresponding student IDs.
# Implement pytest test cases to verify the correctness of your code for each data structure.

import pytest

#Function to print the first three books in the list.
def listBooks():
    # Favorite book list (bookName, bookAuthor)
    favoriteBooks = [("Onyx Storm", "Rebecca Yarros"), ("Wings of Starlight", "Allison Saft"), ("Wind and Truth", "Brandon Sanderson"), ("The God of the Woods", "Liz Moore")]
    print(favoriteBooks[:3])

# Function to create a dictionary that represents a basic student database, including student names and their corresponding student IDs
def studentDb():
    # Student database
    studentDatabase = {
        "student1" : {"name" : "Chris Helland", "id" : "24"},
        "student2" : {"name" : "Bob Smith", "id" : "74"},
        "student3" : {"name" : "Robert Doe", "id" : "102"}
    }

# Tests

def test_listBooks(capsys):
    listBooks()
    captured = capsys.readouterr()
    assert captured.out == "[('Onyx Storm', 'Rebecca Yarros'), ('Wings of Starlight', 'Allison Saft'), ('Wind and Truth', 'Brandon Sanderson')]\n"

def test_studentDb():
    studentDb()