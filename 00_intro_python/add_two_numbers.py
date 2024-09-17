## Problem Statement

"""
Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

1. Prompt the user to enter the first number.

2. Read the input and convert it to an integer.

3. Prompt the user to enter the second number.

4. Read the input and convert it to an integer.

5. Calculate the sum of the two numbers.

6. Print the total sum with an appropriate message.

The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.

"""


prompt_1:str=input("Enter first number: ")
prompt_2:str=input("Enter Second number: ")

inp_1:int=int(prompt_1)
inp_2:int=int(prompt_2)

total_sum:int=inp_1+inp_2
print(f'{prompt_1} + {prompt_2} = {total_sum}')


