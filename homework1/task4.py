# Homework 1 - Task 4: Functions and Duck Typing
# UCCS SP2025 CS4300-2, Dr. Kristen Walcott (instructor)
# Created by Christopher Helland (student)
# Due: February 10, 2025

# -- Assignment: --
# Duck typing is the functionality of a language where "if it looks like a duck and quacks like a duck,
# you might as well treat it like a duck." This is quite common in interpreted languages. Create a
# new file named task4.py that calculates the final price of a product after applying a given discount
# percentage inside of a function named calculate_discount. The function should accept any numeric
# type for price and discount. Write pytest test cases to test the calculate_discount function with
# various types (integers, floats) for price and discount.

import pytest

# Function which takes two parameters, price and discount_as_precent, then returns the new price after applying the discount
def calculate_discount(price, discount_as_percent):
    return price-(price*(discount_as_percent/100))

# Tests

def test_calculate_discount():
    assert calculate_discount(50, 25) == 37.50
    assert calculate_discount(50.00, 10.00) == 45.00
    assert calculate_discount(0, 0) == 0.00
    assert calculate_discount(10,0) == 10.00
    assert calculate_discount(112, 100) == 0.00