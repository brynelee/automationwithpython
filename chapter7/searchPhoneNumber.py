#! /usr/bin/python3

import re
import pprint

# demo of search()

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

pNR = phoneNumRegex.search('321-221-2561 is the number of Mike, and his another number is 138-101-5255')

print(pNR.groups())
print(pNR.group(0))
print(pNR.group(1))
print(pNR.group(2))

# demo of findall()

pNRAll = phoneNumRegex.findall('321-221-2561 is the number of Mike, and his another number is 138-101-5255')

print(pNRAll)
for i in range(len(pNRAll)):
    print('the result of No.' + str(i) + ' is ' + str(pNRAll[i]))

print()
print("##### demo of optional mark '?'#####")
print()

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

print()
print("##### demo of optional mark '*'#####")
print()

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The adventures of Batwowowowowoman')
print(mo3.group())

print()
print("##### demo of optional mark '+'#####")
print()

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
if mo1 == None:
    print(mo1)
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The adventures of Batwowowowowoman')
print(mo3.group())

print()
print("##### demo of \d \D \s \S \w \W#####")
print()

xmasRegex = re.compile(r'\d+\s\w+')
results = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
pprint.pprint(results)

print()
print("##### demo of ^ and $ #####")
# ^表示开始　$表示结束
print()

beginsWithHello = re.compile(r'^Hello')
result1 = beginsWithHello.search('Hello world!')
print(result1.group())

endsWithNumber = re.compile(r'\d$')
result2 = endsWithNumber.search('Your number is 42')
print(result2.group())

wholeStringIsNum = re.compile(r'^\d+$')
result3 = wholeStringIsNum.search('1234567890')
print(result3)
result4 = wholeStringIsNum.search('12345xyz67890')
print(result4)
result5 = wholeStringIsNum.search('1234567890xyz')
print(result5)

print()
print("##### demo of . #####")
# .是通配符
print()

atRegex = re.compile(r'.at')
result = atRegex.findall('The cat in the hat sat on the flat mat.')
print(result)

print()
print("##### demo of .* #####")
# .*用来匹配所有字符（除了\n)
print()

nameRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
result = nameRegex.search('First Name: Xiaodong Last Name: Li')
print(result.group(1))
print(result.group(2))


print()
print("##### demo of .*　贪心和非贪心模式 #####")
# .*用来匹配所有字符（除了\n)
# .*是贪心模式， .*?是非贪心模式
print()

text = '<To serve man> for dinner.>'
nongreedyRegex = re.compile(r'<.*?>')
result1 = nongreedyRegex.search(text)
print(result1.group())

greedyRegex = re.compile(r'<.*>')
result2 = greedyRegex.search(text)
print(result2.group())



