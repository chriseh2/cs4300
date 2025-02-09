# Homework 1 - Task 3: Control Structures
# UCCS SP2025 CS4300-2, Dr. Kristen Walcott (instructor)
# Created by Christopher Helland (student)
# Due: February 10, 2025

# -- Assignment: --
# Create a new file named task3.py. Create an if statement to check if a given number is positive,
# negative, or zero. Implement a for loop to print the first 10 prime numbers (you may need to
# research how to calculate prime numbers). Create a while loop to find the sum of all numbers from
# 1 to 100. Write pytest test cases to verify the correctness of your code for each control structure

import pytest

# Function to check if a given number, x, is positive, negative, or zero
# The function will return a string indicating "zero", "positive", or "negative", accordingly
def numberSign(x):
    if x == 0:  return "zero"
    elif x > 0: return "positive"
    elif x < 0: return "negative"
    
# Function to print the first 10 prime numbers.
def printPrimes():
    number = 2
    foundPrime = 0

    while foundPrime < 10:
        if isPrime(number) == True:
            print(number)
            foundPrime+=1
        number+=1

def isPrime(number):
    factor = 2
    while factor < number:
        if isFactor(factor, number) == True:
            return False
        factor+=1
    return True

def isFactor(factor, number):
    return number % factor == 0

# Function to find the sum of all numbers from 1 to 100.
def summation():
    sum = 0 # variable to hold the current sum as it loops
    counter = 1 # variable to increment 1 to 100 in the while loop
    while counter <= 100:
        sum+=counter
        counter+=1
    return sum
    
# Tests:

def test_numberSign():
    assert numberSign(5) == "positive"
    assert numberSign(-3) == "negative"
    assert numberSign(0) == "zero"

def test_printPrimes(capsys):
    printPrimes()
    captured = capsys.readouterr()
    assert captured.out == "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n"

def test_summation():
    assert summation() == 5050