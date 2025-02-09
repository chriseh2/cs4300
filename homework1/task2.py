# Homework 1 - Task 2: Variables and Data Types
# UCCS SP2025 CS4300-2, Dr. Kristen Walcott (instructor)
# Created by Christopher Helland (student)
# Due: February 10, 2025

# -- Assignment: --
# Create a new file named task2.py demonstrating the use of various data types, including integers,
# floating-point numbers, strings, and boolean. Implement a Python using pytest to test case for each
# data type, ensuring that the script’s behavior matches the expected outcomes.

import pytest
import math

# Function demonstrating the use of integers
# This demo takes two integers, x and y, and returns their product (x*y)
# This demo assumes x and y are already verified to be integers prior to the function call
def intDemo(x, y):
    return x*y

# Function demonstrating the use of floating-point numbers
def fpnDemo():
    return 1+0.25

# Function demonstrating the use of strings
# This demo takes a string, name, and returns the question, "How are you, [name]?"
def strDemo(name):
    return "How are you, " + name + "?"

# Function demonstrating the use of booleans
# This demo takes two variables, x and y, and returns true if they are equal, or false if they are not
def boolDemo(x, y):
    if x==y:
        return True
    if x!=y:
        return False

# Tests:

def test_intDemo():
    assert intDemo(0,0) == 0
    assert intDemo(1,1) == 1
    assert intDemo(0,1) == 0
    assert intDemo(-1,-1) == 1
    assert intDemo(1,-1) == -1

def test_fpnDemo():
    assert fpnDemo() == 1.25

def test_strDemo():
    assert strDemo("William") == "How are you, William?"

def test_boolDemo():
    assert boolDemo(1,2) == False
    assert boolDemo(1,1) == True
    assert boolDemo("a", "b") == False
    assert boolDemo("a", "a") == True
    assert boolDemo("Charles","Tom") == False
    assert boolDemo("Tom", "Tom") == True
    assert boolDemo("tom", "Tom") == False
    assert boolDemo(True,False) == False
    assert boolDemo(False,False) == True
    assert boolDemo("string", 1) == False