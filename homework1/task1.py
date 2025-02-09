# Homework 1 - Task 1: Introdction to Python and Testing
# UCCS SP2025 CS4300-2, Dr. Kristen Walcott (instructor)
# Created by Christopher Helland (student)
# Due: February 10, 2025

# -- Assignment: --
# Create a new file named task1.py. Write a Python script that prints "Hello, World!" on the
# console. Set up a pytest test case that verifies the output of your script.

import pytest

# Function which prints "Hello, world!" to console.
def hello():
    print("Hello, world!")

# Tests:
def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"