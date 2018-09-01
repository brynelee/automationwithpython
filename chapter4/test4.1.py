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

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']

print('Before sorted, the spam list is: ' + listofString(spam, ', '))

spam.sort()

print('After sorted, the spam list is: ' + listofString(spam, ', '))

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
print('the cat now is: ' + listofString(cat, ', '))

cat.remove('fat')
print('the cat after removal is: ' + listofString(cat, ', '))

cat.sort(reverse=True)
print('the cat after removal and reversely sorted is: ' + listofString(cat, ', '))
print()

# 元祖和列表之间的转换
tuple1 = tuple(cat)
print('the tuple is: ' + listofString(tuple1, ', '))

list1 = list(tuple1)
print('the list is: ' + listofString(list1, ', '))
print()

# 列表是引用传递
list2 = list1
list2[1] = 'hello'
print('list1 is: ' + listofString(list1, ', '))
print('list2 is: ' + listofString(list2, ', '))
print()

## copy模块可以复制来避免引用, copy() or deepcopy()
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print('spam is: ' + listofString(spam, ''))
print('cheese is: ' + listofString(cheese, ' '))
print()
