## Problem Statement
"""
Simulate rolling two dice, three times.  Prints the results of each die roll.  This program is used to show how variable scope works.
"""


import random

def roll_dice()->None:
       dice_sides:int=6
       dice1:int=random.randint(1,dice_sides)
       dice2:int=random.randint(1,dice_sides)

       sum_of_two:int=dice1+dice2
       print(f"The sum of two dice rolls is {sum_of_two}")


def main():

    roll_dice()
    roll_dice()
    roll_dice()



if __name__=='__main__':
     main()
   
   
     





    