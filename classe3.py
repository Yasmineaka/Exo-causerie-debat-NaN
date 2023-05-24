import random



class personnage:
    def __init__(self):
        self.point = 0
    def roll_dice(self):
        b = random.randint(6)
        dice = 6
        joueur1 = input("lancez le dé")*3
        joueur2 = input("lancez le dé")*3

 
        