import random

def dice_roll(dice,sides):

    roll = []

    for i in range(dice):
        face = random.randint(1,sides)
        roll.append(face)

    return roll 
try:   

    dice = int(input("Dice: "))
    if (dice <= 0):
       print("Must have at least one dice!")
       quit()
except ValueError: 
    print("Invalid input! Please enter a number for dice.")
    quit

try:

    sides = int(input("Sides(max 6): "))
    if (sides <= 0):
       print("Must have at least one side!")
       quit()
    elif sides > 6:
        print("Sides cannot be more than 6, setting sides = 6.")
        sides = 6
except ValueError:
    print("Invalid input! Please enter a number of sides.")
    quit


roll = dice_roll(dice, sides)
print("You rolled:", roll)