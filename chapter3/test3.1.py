
def spam(devideBy):
    try:
        return 42 / devideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(31))
print(spam(0))
print(spam(22))