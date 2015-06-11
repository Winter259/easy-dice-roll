print("Welcome to easy-dice-roll!")
print("Made by Winter259/Simon AM")
print("You can fork me on github!")
print("https://github.com/Winter259/easy-dice-roll")

def choose_dice_type():
	dice_type = input("Please enter the kind of dice you will be using: ")

def display_menu():
	menu_input = -1
	while menu_input < 0 or menu_input > 3:
		print("MENU:")
		print("1: Roll Dice")
		print("2: Choose Dice Type")
		print("3: Exit")
		menu_input = int(input("Please enter your choice:"))
		menu_choice(menu_input)
		
def menu_choice(menu_input):
	if menu_input == 1:
		""" roll dice! """
		print("Lets roll a dice!")
	elif menu_input == 2:
		print("Lets change the dice!")
		""" choose dice type! """
	elif menu_input == 3:
		print("Lets get out of here!")
		""" exit! """
	else:
		print("ERROR: Input out of bounds!")
	
while True:
	display_menu()