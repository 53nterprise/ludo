import random as r

def dice_roll():
    return r.randint(1,6),r.randint(1,6)
print("this is a dice roll")

print(dice_roll())