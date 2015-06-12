__author__ = 'Simon'

from dice_fnc import *

print("Welcome to easy-dice-roll!")
print("You can fork me on github!")
print("https://github.com/Winter259/easy-dice-roll")

# init vars
current_dice_type = 0

def display_menu():
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
		current_dice = choose_dice_type()
	else:
		""" do nothing! exit is handle by main"""

while True:
	menu_input = -1 # stops choice looping
	display_menu()
	try:
		menu_input = int(input("Please enter your choice: "))
		menu_choice(menu_input)
	except ValueError:
		print("ERROR: Input out of bounds!")
	if menu_input > 3 or menu_input < 1:
		print("ERROR: No Menu option available!")
	if menu_input == 3:
		print("Bye!")
		break
