#! /usr/bin/python3

filePath = 'sampleFileOfContacts.txt'

fileHandle = open(filePath)
fileContent = fileHandle.read()
fileHandle.close()
print(fileContent)

print()
print('#############  demo of file read and write #################')
print()

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello World!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.\n')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)


