# Homework 1 - Task 7: Package Control in DevEdu
# UCCS SP2025 CS4300-2, Dr. Kristen Walcott (instructor)
# Created by Christopher Helland (student)
# Due: February 10, 2025

# -- Assignment: --
# Use pip package manager to add a Python package of your choice to your project (e.g., requests,
# numpy, matplotlib). Create a new file named task7.py and write a Python script that demon-
# strates how to use the chosen package to perform a specific task or function. Implement pytest test
# cases to verify the correctness of your code when using the package.

import pytest
import numpy as np

# Simple function using numpy to find the median of an array containing numbers
def medianArray():
    numbers = np.median([3, 2, 10, 5, 7])
    return numbers

# Tests

def test_medianArray():
    assert medianArray() == 5