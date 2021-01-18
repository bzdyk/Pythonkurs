##import math
##inputdata = [0,1,2,3,5,8,13,21,34,55,89]
##factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]
##print('input data has  ',len(inputdata),'elements')
##print('factor table has',len(factortable),'elements')
##if len(inputdata) == len(factortable):
##    i=0
##    while i<len(inputdata):
##        minvalue=inputdata[i]-factortable[i]*inputdata[i]
##        maxvalue=inputdata[i]+factortable[i]*inputdata[i]
##        print('minvalue=',minvalue,'maxvalue=',maxvalue)
##
##        mininteger = math.floor(minvalue)
##        maxinteger = math.ceil(maxvalue)
##        print(mininteger,"\t",inputdata[i],"\t",maxinteger)
##        i+=1
##else:
##    print("inputdata and factortable need to have equal number of elements")
##print('-------------------------------------------------------------')


import math
import random

inputdata = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
factortable = [0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.13, 0.21, 0.34, 0.55, 0.89]
print('input data has  ', len(inputdata), 'elements')
print('factor table has', len(factortable), 'elements')
i = 0
while i < len(inputdata):
    minvalue = inputdata[i] - random.random() * inputdata[i]
    maxvalue = inputdata[i] + random.random() * inputdata[i]
    print('minvalue=', minvalue, 'maxvalue=', maxvalue)

    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print(mininteger, "\t", inputdata[i], "\t", maxinteger)
    i += 1
else:
    print("inputdata and factortable need to have equal number of elements")
print('-------------------------------------------------------------')
