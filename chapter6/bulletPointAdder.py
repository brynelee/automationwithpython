#! /usr/bin/python3

import pyperclip

text = pyperclip.paste()
print(text)

# Seperate lines and add stars
lines = text.split('\n')
for i in range(len(lines)): #loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
print(pyperclip.paste())