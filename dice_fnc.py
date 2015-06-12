__author__ = 'Simon'

dice_types = [4,6,8,10,12,20,20,100]

def choose_dice_type():
    print("Current Dice types available: ")
    for dice in dice_types:
        print(dice), print(" "),
    try:
        dice_choice = int(input("Enter the number of sides the dice you wish to use has:"))
    except ValueError:
        print("ERROR! Input out of bounds")
    while not check_dice_type(dice_choice):
        try:
            dice_choice = int(input("Enter the number of sides the dice you wish to use has:"))
        except ValueError:
            print("ERROR! Input out of bounds")
            dice_choice = 0 # stops double error messages
    return dice_choice


def check_dice_type(chosen_dice):
    if chosen_dice not in dice_types:
        print("That kind of dice does not exist!")
        return False
    else:
        return True