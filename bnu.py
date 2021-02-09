import random
import time

colors = ('red','green','blue','yellow','wild','quad')
deck = []
deckPersistent = []

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
	deckPersistent = [x for x in deck]

genCard(colors, deck, deckPersistent)

