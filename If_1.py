MIN_LIKES = 500
MIN_SHARES = 100


num_likes = 600
num_shares = 199


if num_likes >= MIN_LIKES and num_shares >= MIN_SHARES:
    print("Jest zniżka")

elif num_likes < MIN_LIKES and num_shares < MIN_SHARES :
    print("za mało laików i udostępnień")
elif num_likes < MIN_LIKES:
    print("za mało laików")
else:
    print("za mało udostępmień")




isPizzaOrdered = False
isBigDrinkOrdered = False
isWeekend = False

if (isBigDrinkOrdered or isPizzaOrdered) and not isWeekend:
    print("jest Burger gratis ")
elif isWeekend:
    print("Burger darmowy tylko w tygodniu")
else:
    print("brak Burgera - musisz zamowić pizze lub duży napój")





diskSize = 160
diskSizeUsed = 133
fileSize = 10

if diskSize-diskSizeUsed > fileSize:
    print("File can be downloaded")
else:
    print("File can't be downloaded")














