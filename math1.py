import random

for i in range(10):
    print(random.randint(1,100))

print("XXXXXXXXXXXXXXXXX")

number1 = random.randint(1,100)
counter = 1
number2 = random.randint(1,100)

print("number1: ",number1)
while number1 != number2:
    print("counter: ", counter, "number2: ", number2)
    counter +=1
    number2 = random.randint(1,100)
print("udalo sie wylosować", number2, "po ",counter, " prubach")

print("xxxxxxxxxxxxxxxxx")

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

random.shuffle(countries)
print(countries)
groupNumber = 0
for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])
