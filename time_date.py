##import time
##import calendar
##print(time.time())
##print(time.localtime(time.time()))
###calendar.
##
##
##print(calendar.month(2020,9))
##print("**********************")
##calendar.setfirstweekday(6)
##print(calendar.month(2020,9))
##print("**********************")
##print(calendar.isleap(2020))
##print(calendar.calendar(2019))
##
##print("cos\n\n")
##print(r'cos\n\n')
##print("cos")




##inputdata = [0,1,2,3,5,8,13,21,34,55,89]
##factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]
##
##import math
##print(len(inputdata))
##print(len(factortable))
##
##print("\n\n")
##if len(inputdata) == len(factortable):
##    print("ok")
##    n = 0
##    while n <len(inputdata):
##        #print(inputdata[n])
##        minvalue = (inputdata[n] - factortable[n])*inputdata[n]
##        maxvalue = (inputdata[n] + factortable[n])*inputdata[n]
##        print("minvalue:", minvalue)
##        print("maxvalue:", maxvalue)
##
##        mininteger = math.floor(minvalue)
##        maxinteger = math.ceil(maxvalue)
##        print(mininteger,"\t",inputdata[n],"\t",maxinteger)
##        n +=1
##else:
##    print("inputdata and factortable need to have equal number of elements")
##




import datetime

print(datetime.datetime.today())
print(datetime.datetime.now().strftime("%Y-%m-%d"))
