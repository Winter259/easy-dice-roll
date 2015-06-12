__author__ = 'Simon'

from dice_fnc import *
from dice_classes import *

import os
def cls():
	os.system(['clear','cls'][os.name == 'nt'])

print("Welcome to easy-dice-roll!")
print("You can fork me on github!")
print("https://github.com/Winter259/easy-dice-roll")

def display_menu():
	# cls()
	print("Current dice being used: d{}".format(my_dice.type))
	print("MENU:")
	print("1: Roll Dice")
	print("2: Choose Dice Type")
	print("3: Exit")

def menu_choice(choice):
	if choice == 1:
		""" roll dice! """
		print("Lets roll a dice!")
	elif choice == 2:
		""" choose dice type! """
		print("Lets change the dice!")
		my_dice.change_type()
	else:
		""" do nothing! exit is handle by main"""

# init dice
my_dice = Dice()

while True:
	menu_input = -1 # stops choice looping
	display_menu()
	try:
		menu_input = int(input("Please enter your choice: "))
		menu_choice(menu_input)
	except ValueError:
		print("ERROR: Input out of bounds!")
	check_integer_loop(menu_input,1,3)
	if menu_input == 3:
		print("Bye!")
		break
