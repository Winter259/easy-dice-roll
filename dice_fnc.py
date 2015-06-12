__author__ = 'Simon'

import random

dice_types = [4,6,8,10,12,20,20,100]

def choose_dice_type():
    print("Current Dice types available: ")
    for dice in dice_types:
        print(dice, end=' ')
    print("\n")
    try:
        dice_choice = int(input("Enter the number of sides the dice you wish to use has: "))
    except ValueError:
        print("ERROR! Input out of bounds")
        dice_choice = 0
    while not check_dice_type(dice_choice):
        try:
            dice_choice = int(input("Enter the number of sides the dice you wish to use has: "))
        except ValueError:
            print("ERROR: Input out of bounds")
            dice_choice = 0 # stops double error messages
    print("Now using: d{}".format(dice_choice))
    return dice_choice


def check_dice_type(chosen_dice):
    if chosen_dice not in dice_types:
        print("That kind of dice does not exist!")
        return False
    else:
        return True

def check_int_bounds(integer_variable,lower_bound,upper_bound):
    if integer_variable > upper_bound or integer_variable < lower_bound:
        return False
    else:
        return True

def check_integer_loop(integer,lower,upper):
    while not check_int_bounds(integer,lower,upper):
        print("ERROR: Input out of bounds!")
        integer = int(input("Please enter a valid number: "))
    return integer

def roll_dice(current_dice):
    roll_amount = int(input(("How many d% do you want to roll?") % current_dice))
    roll_amount = check_integer_loop(roll_amount,0,100)
