import zipfile, shutil, pprint, os

workingDir = '/home/xiaodong/Gitroot/automationwithpython/chapter9'
pathForZip = '/home/xiaodong/Gitroot/automationwithpython/chapter9/demoFolder'
zipFileName = 'example'

os.chdir(workingDir) # move to the folder with example.zip

# make zip file
shutil.make_archive(zipFileName,'zip', pathForZip)

# read zip file and list directory and files
exampleZip = zipfile.ZipFile(zipFileName+'.zip')
pprint.pprint(exampleZip.namelist())

# get specific file information
spamInfo = exampleZip.getinfo('bacon1.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
exampleZip.close()

#make the cleaning by sending the zipfile to trash

import send2trash

send2trash.send2trash(zipFileName+'.zip')

