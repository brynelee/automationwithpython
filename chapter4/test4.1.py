import random

messages = ['It is certain',
            'it is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

for i in range(len(messages)):
    print(messages[random.randint(0, len(messages)-1)])

# demo of list

def listofString(stringList, sep):
    stringOfList = ''
    for i in range(len(stringList)):
        stringOfList += (str(stringList[i]) + sep)
    return stringOfList

globalSep = ', '

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']

#print('Before sorted, the spam list is: ' + listofString(spam, ', '))
print('Before sorted, the spam list is: ' + globalSep.join(spam))

spam.sort()

print('After sorted, the spam list is: ' + globalSep.join(spam))

# demo of list slice
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spamSlice = spam[:4]
spamSliceString = ''
for i in range(len(spamSlice)):
    spamSliceString += (spamSlice[i] + ', ')
print('the spam slice is ' + spamSliceString)

# 多重赋值
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
print(size + " " + color + ' ' + disposition)

print(cat.index('black'))
print(cat.index('loud'))

cat.append('anotherItem')
print(cat[3])

cat.insert(1, 'chicken')
print('the cat now is: ' + globalSep.join(cat))

cat.remove('fat')
print('the cat after removal is: ' + globalSep.join(cat))

cat.sort(reverse=True)
print('the cat after removal and reversely sorted is: ' + globalSep.join(cat))
print()

# 元祖和列表之间的转换
tuple1 = tuple(cat)
print('the tuple is: ' + globalSep.join(tuple1))

list1 = list(tuple1)
print('the list is: ' + globalSep.join(list1))
print()

# 列表是引用传递
list2 = list1
list2[1] = 'hello'
print('list1 is: ' + globalSep.join(list1))
print('list2 is: ' + globalSep.join(list2))
print()

## copy模块可以复制来避免引用, copy() or deepcopy()
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = '42'
print('spam is: ' + globalSep.join(spam))
print('cheese is: ' + globalSep.join(cheese))
print()
