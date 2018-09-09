import os

path = '/home/xiaodong/Gitroot/automationwithpython/chapter9/demoFolder'

for folderName, subfolders, filenames in os.walk(path):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)