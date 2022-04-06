import random

class Pirate:
    Pmove_list = ["block", "attack", "heal", "scream"]
    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self

    def attack ( self , ninja ):
        posOrNeg = random.randint(1,3)
        randomNum = random.randint(0,11)
        if posOrNeg == 1:
            if self.strength - randomNum < 0:
                print(f"{self.name} slipped on a banana and completely missed")
            else:
                ninja.health -= (self.strength - randomNum)
                print(f"{ninja.name} took {self.strength - randomNum} damage")
        else: 
            ninja.health -= (self.strength + randomNum)
            print(f"{ninja.name} took {self.strength + randomNum} damage")
        return self
    def heal(self):
        randomNum = random.randint(5,15)
        print(f"{self.name} healed {randomNum}")
        self.health += randomNum
        return self
    def scream(self):
        print("Arg.. I AM PIRATE AND I DON'T TAKE CARE OF MY TEETH")
        randomNum = random.randint(0,3)
        self.strength += randomNum
        print(f"{self.name}'s Strength rose {randomNum} points")