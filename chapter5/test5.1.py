
myCat = {
            'size': 'fat',
            'color': 'gray',
            'disposition': 'cloud'
         }

print(myCat['size'])
print(myCat['color'])

print()

for key, value in myCat.items():
    print(key + ', ' + value)

print()

for item in myCat.items():
    print(item) # item是元祖

# demo of birthday DB
# 遍历字典

birthdays = {
    'Alice': 'April 1',
    'Bob': 'Dec 12',
    'Carol': 'Mar 4'
}

while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break
        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')

# demo of get(), 存在，所以不会使用缺省值
print('Alice birthday is: ' + birthdays.get('Alice', 'Oct 1'))

# demo of get()，并不存在，所以会使用缺省值
print('Jerry birthday is: ' + birthdays.get('Jerry', 'Aug 5'))

print()

# demo of setdefault(), 用来确保一个键存在
birthdays.setdefault('Alice', 'Oct 1')
print('Alice birthday is: ' + birthdays['Alice'])
birthdays.setdefault('Jacob', 'Sep 2')
print('Jacob birthday is: ' + birthdays['Jacob'])

# another demo of setdefault()
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1
print(count)

