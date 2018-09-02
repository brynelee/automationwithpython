
#demo of slice of string, in and not in

spam = 'Hello world!'
fizz = spam[0:5]
print(fizz)
print('world' in spam)

print()

# demo of usage center(), ljust(), rjust()

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {
    'sandwiches': 4,
    'apples': 12,
    'cups': 4,
    'cookies': 8000
}

printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

#demo of strip(), rstrip(), lstrip()
spam = ' Hello World '
print(spam)
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

