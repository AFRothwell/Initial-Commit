from Player import Player
from random import randint
from Dogs import dogs
from Ladders import ladders

# args and kwargs
# 2 players for now
# roll even = dog, odd = ladder
# dog and ladder is fixed number


turn = 0
game = 1
counter1 = 0
counter2 = 0


player1 = Player(input("What is your name?! "))
player2 = Player(input("What is your name?! "))

def dice_roll():
    return randint(1,6)

while (counter1 and counter2) < 20:
    
    if turn == 0:
        select = input(f"{player1.name}, virtual please virtually roll the virtual dice, virtually, and don't call me Virgil: y/n  " )
        if select == "y":
            diceroll = dice_roll()
            print(f"{player1.name}, congratulations, you have successfully rolled a {diceroll}, I am proud of you")
            counter1 += diceroll
            print(f"You have taken a leisurely stroll to counter {counter1}")
            turn = 1
        else:
            print("Stop virtually wasting our time, you have been fined $30")
            continue
    
    if turn == 1:
        select = input(f"{player2.name}, virtual please virtually roll the virtual dice, virtually, and don't call me Shirley: y/n  ")
        if select == "y":
            diceroll = dice_roll()
            print(f"{player2.name}, congratulations, you have successfully rolled a {diceroll}, I am proud of you")
            counter2 += diceroll
            print(f"You have stumbled aimlessly to counter {counter2}")
            turn = 0
        else:
            print("Stop virtually wasting our time, you have been fined $30")
            continue

if counter1 >= 20:
    print(f"{player1.name} you win! Now go wash the dishes you silly gerblerdlop.")

if counter2 >= 20:
    print(f"{player2.name} you win! Now go wash the dishes you silly gerblerdlop.")





