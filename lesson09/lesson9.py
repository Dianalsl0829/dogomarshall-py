# Lesson 9
#import statment
from random import choice

asking = True
player = " "

while asking:
    player = str(input("Enrter a choice of (rock , paper, scissors): "))

    if player in {'rock','paper','scissors'}:
        # we use in operator in python often with sets because of its faster execution speed
        asking = False
#end of while loop

ai = choice(['rock', 'paper','scissors'])

if player == ai:
    print("Tie Game")
elif player == 'rock':
    if ai == "scissors":
        print(f"You won, AI choose {ai}")
    elif ai == "paper":
        print(f"You lose, AI choose {ai}")
elif player =="paper":
    if ai == "rock":
        print(f"You won, AI choose {ai}")
    elif ai == "scissors":
        print(f"You lose, AI choose {ai}")
elif player =="rock":
    if ai == "scissors":
        print(f"You won, AI choose {ai}")
    elif ai == "paper":
        print(f"You lose, AI choose {ai}")