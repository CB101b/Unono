import random
from UnoMisc import *
import time

colors = ('red','green','blue','yellow','wild','quad')
deck = []
deckPersistent = []
playerDict={}
winConditions = {
	"playerCardCount":0
}

# generates cards, puts them in a deck
def genCard(colors, deck, deckPersistent):
	for color in colors:
		if color == 'wild' or color == 'quad':
			for _ in range(4):
				deck.append(color)
		else:
			for num in range(10):
				deck.append((color,num))
			deck.append((color,'+2'))
			deck.append((color,'invert'))
	for x in deck: deckPersistent.append(x)

def playerGen(playerDict, amount):
	for playerNum in range(amount):
		playerNum += 1
		playerDict.update({"player"+str(playerNum) : []})

def initialDealCards(playerDict, deck):
	for player in playerDict:
		for _ in range(7):
			randomCard = deck[random.randint(0,len(deck)-1)]
			playerDict[player].append(randomCard)
			deck.remove(randomCard)


genCard(colors, deck, deckPersistent)

amount = int(input("How many players?\n"))
playerGen(playerDict, amount)

print("Okay, let's play!")
time.sleep(1)

print("Dealing...")
initialDealCards(playerDict,deck)
time.sleep(2)

# main game loop
finished = 0
while not finished:
	for player in playerDict:
		playerCards = playerDict[player]
		print("It's {}'s turn.".format(player))
		print("Available cards: ")
		for x in playerCards: 
			if len(x) == 2:
				print(x[0],str(x[1]))
			else:
				print(x)
		
		playedCard = input("Which card do you want to play?\n\n").split(" ")
		if len(playedCard) > 1:
			if len(playedCard[1]) == 1:
				playedCard = (playedCard[0], int(playedCard[1]))
			else:
				playedCard = (playedCard[0], playedCard[1])
		else:
			playedCard = playedCard[0]

		if playedCard in playerCards:
			print(playedCard, "is erin")
		else: print(playedCard, "is er niet in")