from classes import ninja
from classes.ninja import Ninja
from classes.pirate import Pirate
import random


michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")



player_list = {
    
}

player_list["p1"] = jack_sparrow.name
player_list["p2"] = michelangelo.name

# while jack_sparrow.health > 0:
#     michelangelo.attack(jack_sparrow)
#     jack_sparrow.show_stats()
#     if jack_sparrow.health <= 0:
#         print("dead")



key2 = player_list["p2"]
key1 = player_list["p1"]


while jack_sparrow.health > 0 or michelangelo.health > 0:
    print(f"{jack_sparrow.name}'s current stats are ")
    jack_sparrow.show_stats()
    print(f"{michelangelo.name}'s current stats are ") 
    michelangelo.show_stats()
    players_gone = 0
    turn = 0
    if jack_sparrow.health <= 0:
        print(f"{jack_sparrow.name} is DEAD. {michelangelo.name} is the winner")
        break
    if michelangelo.health <= 0:
        print(f"{michelangelo.name} is DEAD. {jack_sparrow.name} is the winner")
        break
    if turn == 0:
        print(f"{michelangelo.name}'s turn. Please choose a person to attack ({Ninja.Nmove_list})")
        ninjaInput = input()
        str(ninjaInput)
        if ninjaInput== "":
            print("Please choose a move")
            
        turn = 1
    if turn > 0:
        print(f"{jack_sparrow.name}'s turn. Please choose a move to use ({Pirate.Pmove_list})")
        pirateInput = input()
        str(pirateInput)
        if pirateInput == "":
            print("Please choose a move")
            
        
    if ninjaInput == "heal":
        michelangelo.heal()
    if pirateInput == "heal":
        jack_sparrow.heal()
    if pirateInput == "attack" and ninjaInput == "block":
        print(f"{jack_sparrow.name} tried to attack {michelangelo.name}, but {michelangelo.name} blocked the attack")

    if  ninjaInput == "attack" and pirateInput == "block":
        print(f"{michelangelo.name} tried to attack {jack_sparrow.name}, but {jack_sparrow.name} blocked the attack")
    
    if ninjaInput == "attack" and pirateInput != "block":
        michelangelo.attack(jack_sparrow)
    if pirateInput == "attack" and ninjaInput != "block":
        jack_sparrow.attack(michelangelo)
    if ninjaInput == "scream":
        michelangelo.scream()
    if pirateInput == "scream":
        jack_sparrow.scream()





