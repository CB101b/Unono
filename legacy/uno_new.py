#!/usr/bin/python
# imports
import json
import math
import random
import checkdecks
import evaluate
import time
# load JSON files (read mode)
cards = json.load(open('cards.json','r'))

# declare card color sets
blue = cards["blue"]
red = cards["red"]
yellow = cards["yellow"]
green = cards["green"]
special = cards["special"]

# declare playstack
playStack = []

# declare player arrays
player1 = []
player2 = []
player3 = []
player4 = []
players = [player1, player2, player3, player4]
playersName = []

print("Welcome to Uno!")
input("Press any key to continue...")

playersName.append(input("Enter player 1's name: "))
playersName.append(input("Enter player 2's name: "))
playersName.append(input("Enter player 3's name: "))
playersName.append(input("Enter player 4's name: "))
print(playersName)

print("Handing cards out...")


for x in range(4):
    current_deal_player = players[x]
    successful = 0
    while not successful:
        cardtype = random.choice([blue, red, yellow, green, special])
        cardchoice = random.choice(cardtype)
        # if cardchoice not in player1 and cardchoice not in player2 and cardchoice not in player3 and cardchoice not in player4:
        if not checkdecks.checkdecks(cardchoice, player1, player2, player3, player4):
            current_deal_player.append(cardchoice)
        if len(current_deal_player) == 7:
            successful = 1

cardtype = random.choice([blue,red,yellow,green,special])
carchoice = random.choice(cardtype)
if cardchoice not in special or cardchoice.split("#")[1] not in ["skip", "flip", "two+"]:
	playStack.append(cardchoice)

# Uwowono
# time.sleep(3)
# print("Done dealing!")
# time.sleep(1)
# print("Let's start!")
# time.sleep(1)

# Gamedir = 'ccw'

# while 1: #Main game loop
#       i = 0 # i for which player's turn it is (0, 1, 2, 3)
#       for player in players:
#               print("It's now ", playersName[i], "'s turn.")
#               def ChooseCard():
#                       print("\n\n Card on stack: ", playStack[-1])
#                       print("\n\nThese are your cards: ", player, sep='\n')
#                       userchoice = input('Type the card you want to play: ')
#                       evalResult = evaluate.evalCard(userchoice, player, playStack) #Find if the card the user selects is compatible with the card on the playstack

#                       if evalResult == 1 and userchoice in player: # If the cards are compatible remove card from player and add card to playstack
#                               playStack.append(userchoice)
#                               player.remove(userchoice)
#                               if len(player) == 0: # If the p-layer has 0 cards he wins
#                                       print("Player", playersName[1], " has won!")
#                               elif Gamedir != 'ccw':
#                                       i += 1
#                               elif Gamedir == 'ccw':
#                                       i -= 1

#                       else:
#                               print('nope')
#                               ChooseCard()