##*****wydruk znaków ASCI*******
##for i in range(32,127):
##    print(i, chr(i))


######### rzut kostą##############
##import random
##min = 1
##max = 6
##
##dice = random.choice(range(min,max+1))
##
##if dice == 1:
##    print("o")
##elif dice == 2:
##    print("  o")
##    print("o")
##elif dice == 3:
##    print("  o")
##    print(" o")
##    print("o")
##elif dice == 4:
##    print("o o")
##    print("o o")
##elif dice == 5:
##    print("o o")
##    print(" o")
##    print("o o")
##else:
##    print("o o")
##    print("o o")
##    print("o o")
##print(dice)


#### rzut pięcioma kostkami

dices = []

import random

min = 1
max = 6

for i in range(5):
    dices.append(random.choice(range(min, max + 1)))
dices.sort()
print(dices)

