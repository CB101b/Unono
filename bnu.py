import random
import time

colors = ('red','green','blue','yellow','wild','quad')
deck = []
deckPersistent = []
playerDict={}

def genCard(colors, deck, deckPersistent):
	for color in colors:
		if color != 'wild' or 'quad':
			for num in range(10):
				deck.append((color,num))
			deck.append((color,'+2'))
			deck.append((color,'invert'))
		else:
			for _ in range(4):
				deck.append(color)
	for x in deck: deckPersistent.append(x)

def playerGen(playerDict, amount):
	for playerNum in range(amount):
		playerNum += 1
		playerDict.update({"player"+str(playerNum) : []})


genCard(colors, deck, deckPersistent)
playerGen(playerDict, int(input("How many players?\n"))))