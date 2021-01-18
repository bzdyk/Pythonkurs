##numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
##i = 0
##maxi = len(numbers)-1
##
##while i <= maxi :
##        print(numbers[i], numbers[i+1])
##        i+=1
##        if ((numbers[i-1])*(numbers[i-1])) == numbers[i] :
##           print("FOUND")


###########################################################

##numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
##i = 0
##maxi = len(numbers)-3
##
##while i <= maxi :
##        print(numbers[i], numbers[i+1], numbers[i+2])
##        i+=1
##        if ((numbers[i-1])*(numbers[i-1])) == numbers[i]  and ((numbers[i])*(numbers[i])) == numbers[i+1]:
##          print("FOUND")


################################################################

##texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
##
##i = 0
##maxi = len(texts)-1
##
##while i < maxi:
##    print(texts[i], texts[i+1])
##    i+=1
##    if len(texts[i-1]) == len(texts[i]):
##        print("FOUND")

###########################################

##number = 1
##previousNumber =0
##
##
##while number < 50:
##    print(number+previousNumber)
##    previousNumber = number
##    number+=1

###############################

import random

my_number = random.randint(0, 20)

guess = -1
print("Guess my number!")
trials = 1
guess = int(input())

while my_number != guess:
    if my_number > guess:
        print("Twoja liczba za małą")
        trials += 1
        guess = int(input())
    if my_number < guess:
        print("Twoja licba za duża")
        trials += 1
        guess = int(input())
    if my_number == guess:
        print("Zgadłeś po:", trials + 1)






