## Problem Statement
"""
Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division. 

Here's a sample run of the program (user input is in bold italics):

Please enter an integer to be divided: 5

Please enter an integer to divide by: 3

The result of this division is 1 with a remainder of 2
"""





def remainder_division()->None:
    prompt1:int=int(input('Enter the Numerator : '))
    prompt2:int=int(input('Enter the denominator : '))
    division:int=prompt1//prompt2
    modulus:int=prompt1%prompt2
    print(f'{prompt1}/{prompt2} = {division}')
    print(f'Remainder is = {modulus}')



def main()->None:
   remainder_division()


if __name__=='__main__':
    main()





