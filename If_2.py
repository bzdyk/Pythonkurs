musclePain = True
fever = True
weakness = False

if musclePain and fever and weakness:
    print("suspicion of influenza")
elif weakness and (not fever or not musclePain):
    print("Just take a rest!")
else:
    print("you may be cold")

