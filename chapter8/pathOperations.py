#! /usr/bin/python3

import os
cwdDir = os.getcwd()
print(cwdDir)
print(os.path.basename(cwdDir))
print(os.path.dirname(cwdDir))
print(os.path.relpath('/home/xiaodong/Gitroot', cwdDir))
print()

sampleFile = '/home/xiaodong/Documents/automationwithpython/sampleFileOfContacts.txt'
sampleDir = '/home/xiaodong/Documents'

# demo of split()
tupleOfSampleFilePath = os.path.split(sampleFile)
print(tupleOfSampleFilePath)

print('dirname is: ' + os.path.dirname(sampleFile))
print('basename is: ' + os.path.basename(sampleFile))
print('the file size is: ' + str(os.path.getsize(sampleFile)))
print()

# demo of listdir()

print('the dir list is: \n' + '\n'.join(os.listdir(sampleDir)))
print()

# demo of path validation
print('the path is valid? - ' + str(os.path.exists(sampleFile)))
print('the path is a file? - ' + str(os.path.isfile(sampleFile)))
print('the path is a directory? - ' + str(os.path.isdir(sampleFile)))

