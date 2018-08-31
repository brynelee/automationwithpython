
name = 'Mike'
if name == 'Alice':
    print('Hello, Alice')
elif name == 'Bob':
    print('Hello, Bob.')
else:
    print('Hi, ' + name)

print('======================')

spam = 0
while spam < 5:
    print('Hello World!')
    spam += 1

print('======================')

for i in range(5):
    print('here is ' + str(i))

for i in range(5, -1, -1):
    print('here i is ' + str(i))

import random
for i in range(5):
    print(random.randint(1,10))

print('======================')

print('cats', 'dogs', 'mice')

print('cats', 'dogs', 'mice', sep=',')

print('======================')
