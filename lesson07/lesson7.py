# Lesson 7
#https://www.youtube.com/watch?v=ZP4ASKX7rzw

#inport statment
from random import randrange

#inport
difficulty = int(input("Enter the DC: "))

#proccessing and output
player_roll = randrange(1,21)# randrange(a,b) never includes b; it gose up to b

print(f"The player has rolled {player_roll} on their D20.")

if player_roll >= difficulty:
    print(f"The player is succesful as {player_roll} >= {difficulty}.")
else:
    print(f"The player was not succesful as {player_roll} < {difficulty}.")
