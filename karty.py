colors = ['Hearts','Diamonds','Clubs','Spades']

figures = ['Ace','King','Queen','Jack','10','9']

allCards = []


###############wersja 1###########
##z = 0
##
##for i in colors:
##    #print(colors[z])
##    #color = colors[z]
##    k = 0
##    for j in figures:
##       los = colors[z] + "-" + figures[k]
##       allCards.append(los)
##       #print(colors[z])
##       #print(figures[k])
##       k +=1
##    z +=1
##print(allCards)


################wersja 2##########

for i in colors:
       for j in figures:
         los = i + " - " + j
         allCards.append(los)
print(allCards)


import random

random.shuffle(allCards)

print(allCards)

player1 = []
player2 = []

################# sposob 1 #########
##
##max = len(allCards)
##
##for i in range(0, max-1):
## if i % 2 == 0:
##     player1.append(allCards[i])
## if i % 2 != 0:
##      player2.append(allCards[i])
##print("****************************")
##print("player1: " ,player1)
##print("player2: ", player2)


################ sposób 2 ##############
player1.append(allCards[:12])
player2.append(allCards[12:])

print("player1: " ,player1)
print("player2: ", player2)




############### sposob 2 ############
