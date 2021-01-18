data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']



##
##for x in data:
##   element = x.split(':')
##   print(element)
##   print('-------------')
##   if element[0] == "Error":
##      print(element[1].upper())
##   else:
##       print(element[1])
##


##i = 10
##y = 1
##k = 1
##for x in range(1,i+1):
##   y *= x
##   print(y)
##   print('-------')
##
##print(y, "silnia")


list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for x in list_noun:
   for y in list_adj:
      print (x,y)
