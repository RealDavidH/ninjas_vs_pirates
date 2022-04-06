import random

class Ninja:
    Nmove_list = ["block", "attack", "heal", "scream"]
    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self

    def attack(self , pirate ):
        posOrNeg = random.randint(1,3)
        randomNum = random.randint(0,11)
        if posOrNeg == 1:
            if self.strength - randomNum < 0:
                print(f"{self.name} slipped on a banana and completely missed")
            else:
                pirate.health -= (self.strength - randomNum)
                print(f"{pirate.name} took {self.strength - randomNum} damage")
        else: 
            pirate.health -= (self.strength + randomNum)
            print(f"{pirate.name} took {self.strength + randomNum} damage")
        return self
    def heal(self):
        randomNum = random.randint(7,25)
        print(f"{self.name} healed {randomNum}")
        self.health += randomNum
        return self
    def scream(self):
        print("I WILL SLICE YOU UP LIKE A PIZZA")
        randomNum = random.randint(1,3)
        self.strength += randomNum
        print(f"{self.name}'s Strength rose {randomNum} points")