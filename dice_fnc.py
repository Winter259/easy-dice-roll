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
    completed_rolls = 0
    total_roll_value = 0
    roll_hits = 0 # as in shadowrun 5e
    roll_misses = 0 # as in shadowrun 5e
    required_rolls = int(input(("How many d{} do you want to roll: ").format(current_dice.type)))
    required_rolls = check_integer_loop(required_rolls,0,999)
    modifier = int(input("Do you want to add any modifiers? (Input 0 if not): "))
    modifier = check_integer_loop(modifier,-999,999)
    print("Lets roll!")
    while completed_rolls < required_rolls:
        current_roll_result = random.randint(1,current_dice.type) + modifier
        total_roll_value += current_roll_result
        if total_roll_value >= 5:
            roll_hits += 1
        elif total_roll_value == 1:
            roll_misses += 1
        print("Roll {} of {} with a d{}: {}".format((completed_rolls + 1),required_rolls,current_dice.type,current_roll_result))
        completed_rolls += 1
    print("Roll Value Sum: {} Total Hits: {} Total Misses: {}".format(total_roll_value,roll_hits,roll_misses))
