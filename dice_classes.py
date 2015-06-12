__author__ = 'Simon'

from dice_fnc import choose_dice_type

class Dice(object):
    def __init__(self):
        self.type = choose_dice_type()
    def change_type(self):
        self.type = choose_dice_type()
    def roll_dice(self):
        pass
