import random
import time
rood0=[1, 0]
rood1=[1, 1]
rood2=[1, 2]
rood3=[1, 3]
rood4=[1, 4]
rood5=[1, 5]
rood6=[1, 6]
rood7=[1, 7]
rood8=[1, 8]
rood9=[1, 9]
rood10 = [1, 10] #pak twee kaarten
rood11 = [1, 11] #invert gamedir

green0 = [2, 0]
green1 = [2, 1]
green2 = [2, 2]
green3 = [2, 3]
green4 = [2, 4]
green5 = [2, 5]
green6 = [2, 6]
green7 = [2, 7]
green8 = [2, 8]
green9 = [2, 9]
green10 = [2, 10] #pak twee kaarten
green11 = [2, 11] #invert gamedir

blauw0 = [3, 0]
blauw1 = [3, 1]
blauw2 = [3, 2]
blauw3 = [3, 3]
blauw4 = [3, 4]
blauw5 = [3, 5]
blauw6 = [3, 6]
blauw7 = [3, 7]
blauw8 = [3, 8]
blauw9 = [3, 9]
blauw10 = [3, 10] #pak twee kaarten
blauw11 = [3, 11] #invert gamedir

yellow0 = [4, 0]
yellow1 = [4, 1]
yellow2 = [4, 2]
yellow3 = [4, 3]
yellow4 = [4, 4]
yellow5 = [4, 5]
yellow6 = [4, 6]
yellow7 = [4, 7]
yellow8 = [4, 8]
yellow9 = [4, 9]
yellow10 = [4, 10] #pak twee kaarten
yellow11 = [4, 11] #invert gamedir

wild1 = [5, 0] #pak 2 kaarten
wild2 = [6, 0] #pak 4 kaarten

allcards=[wild1, wild2, rood0, rood1, rood2, rood3, rood4, rood5, rood6, rood7, rood8, rood9, rood10, rood11, green0, green1, green2, green3, green4, green5, green6, green7, green8, green9, green10, green11, blauw0, blauw1, blauw2, blauw3, blauw4, blauw5, blauw6, blauw7, blauw8, blauw9, blauw10, blauw11, yellow0, yellow1, yellow2, yellow3, yellow4, yellow5, yellow6, yellow7, yellow8, yellow9, yellow10, yellow11]
tempcards=[wild1, wild2, rood0, rood1, rood2, rood3, rood4, rood5, rood6, rood7, rood8, rood9, rood10, rood11, green0, green1, green2, green3, green4, green5, green6, green7, green8, green9, green10, green11, blauw0, blauw1, blauw2, blauw3, blauw4, blauw5, blauw6, blauw7, blauw8, blauw9, blauw10, blauw11, yellow0, yellow1, yellow2, yellow3, yellow4, yellow5, yellow6, yellow7, yellow8, yellow9, yellow10, yellow11]

player1=[]
player2=[]
player3=[]
player4=[]

players = [player1, player2, player3, player4]
playernames = ['player1', 'player2', 'player3', 'player4']

needHelp = input('Do you need help? (y to display, anythin else to continue) ')
if needHelp == "y":
  print('Alle spelers ontvangen aan het begin van het spel zeven kaarten. De overgebleven speelkaarten worden gesloten op de speeltafel gelegd, dit wordt ook wel de stock genoemd. Dan zal de eerste kaart van de stock worden opengelegd. De eerste speler kan vervolgens een kaart op deze kaart neerleggen, deze moet of hetzelfde nummer, kleur of symbool hebben. Voorbeeld, er ligt een rode 8, dan mag er een kaart met een 8 of een rode kleur op neergelegd worden. Een Joker kan ook worden neergelegd, dat is een uitzondering.Kan de speler geen kaart neerleggen, dan moet er een kaart van de stock worden gehaald. Deze mag direct neergelegd worden, maar als dat niet kan gaat de beurt over. Mocht een deelnemer nog maar één kaart overhebben, dan moet hij of zij UNO roepen. Vergeet de speler dat en speelt hij het spel uit, dan moeten er twee kaarten van de stock gehaald worden.')
  print('commands')
  print('kaarten neerleggen: dit doe je door positie van de kaarten in de spelers hand te zeggen. Van 0 t/m (5),(je begint met tellen bij nul en niet bij 1')
  print('kaarten pakken: dit doe je door -1 in te voeren.')

  #ga ff gekke kaulo help schrijven dreiries

#kaarten uitdelen

def addCard(playerinv, amount): #function to add a amount of cards to a inventory
  for x in range(amount):
    plo = random.randint(0, (len(tempcards)-1))
    playerinv.append(tempcards[plo])
    tempcards.pop(plo)

for i in range(4):
  addCard(players[i], 7)
  

# start spel

playerid = 0

def choosingcard(firstcard, playerid, gamedir):
  for x in range(0, (len(players))):
    topcard = allcards[firstcard]
    topcardnummer = topcard[1]
    topcardtype = topcard[0]

    if topcardtype == 5: #If there's a wild card these actions are taken
      print('\nYou got 2 cards...')
      addCard(players[playerid], 2)
      time.sleep(1)
    elif topcardtype == 6:
      addCard(players[playerid], 4)
      print('\nYou got 4 cards...')
      time.sleep(1)
    elif topcardnummer == 10:
      print('\nYou got 2 cards...')
      addCard(players[playerid], 2)
      time.sleep(1)
    elif topcardnummer == 11:
      print('\n Your turn is sadly skipped...')
      time.sleep(1)
      if playerid == 0:
        playerid = 1
      elif playerid == 1:
        playerid = 2
      elif playerid == 2:
        playerid = 3
      elif playerid == 3:
        playerid = 1

    print("\n It's now ", playernames[playerid], "'s turn")
    print ('The card on top is: ', topcard)
    print ('Your cards: ', players[playerid])
    
    nummer=input('\n Choose a card: ')

    if type(nummer) is not int:
      print('\nNot a valid card number...')
      print('Skipping turn... \n')
      playerid += gamedir
    elif nummer == -1:
      print('what')
      addCard(players[playerid], 1)
      playerid += gamedir
     
    elif type(nummer) is int:
      nummer = int(nummer)
      if nummer > (len(players[playerid])-1): #If the player tpes a invalid number, this happens
        print('This number is too high or low')
        print('please try again')
        choosingcard(firstcard, playerid, gamedir)
      elif nummer < -1:
        print('This number is too high or low')
        print('please try again')
        choosingcard(firstcard, playerid, gamedir)
        
      if nummer == -1:
        ding = random.randint(0, (len(tempcards)-1))
        players[playerid].append(tempcards[ding])

      
      chosencard = players[playerid][nummer]
      
      kleurkaart=chosencard[0]
      nummerkaart=chosencard[1]
      kleurcheck = topcard[0]
      nummercheck = topcard[1]
      
      if kleurcheck == kleurkaart and chosencard in players[x] or kleurcheck == 5  or kleurcheck == 6 or nummercheck == nummerkaart:
        print('\n You can place this card on the stack!')
        if input('Are you sure you want to place this card? (y to place)') == "y":
          #verwijder het kaart uit het players hand en voeg hem toe aan de stapel
          players[playerid].remove(chosencard)
          firstcard = chosencard
          firstcard = allcards.index(firstcard)
          if len(players[playerid]) == 0:
            print(playernames[playerid], ' Has won!')
            exit() 
          else:
            playerid += gamedir
        else:
          print('\n Ok, skipping turn...')
          addCard(players[playerid], 1)
          playerid += gamedir
      else:
        print('Incompatible card... Skipping to next person...')
        addCard(players[playerid], 1)
        playerid += gamedir

  if playerid == 5:
    playerid = 0
    print('check')
    choosingcard(firstcard, playerid, gamedir)
  else:
    playerid = 0
    choosingcard(firstcard, playerid, gamedir)
  

gamedir = 1
p = random.randint(1,len(tempcards))

choosingcard(p, playerid, gamedir)
