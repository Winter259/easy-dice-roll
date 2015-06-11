print "Welcome to easy-dice-roll!"
print "Made by Winter259/Simon AM"
print "You can fork me on github!"
print "https://github.com/Winter259/easy-dice-roll"

def choose_dice_type():
	dice_type = raw_input("Please enter the kind of dice you will be using: ")

def display_menu():
	input = 0
	while input < 0 || input > 3:
		print "MENU:"
		print "1: Roll Dice"
		print "2: Choose Dice Type"
		print "3: Exit"
		input = raw_input("Please enter your choice:")
		menu_choice(input)
		
def menu_choice(input):
	if input == 1:
		# roll dice!
	elif input == 2:
		# choose dice type!
	elif: input == 3:
		# exit!
	else:
		print "ERROR: Input out of bounds!"
	
while true:
	display_menu()