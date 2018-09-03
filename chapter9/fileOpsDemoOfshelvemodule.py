#! /usr/bin/python3

import shelve

fileName = 'mydata'


#shelfFile = shelve.open(fileName)
# cats = ['Zophie', 'Pooka', 'Simon']
#shelfFile['cats'] = cats
#shelfFile.close()

shelfFile = shelve.open(fileName)
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

print()

shelfFile = shelve.open(fileName)
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()



