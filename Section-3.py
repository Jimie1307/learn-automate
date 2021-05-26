
# TOPIC 5: built-in functions
import sys
print('Hello')
sys.exit()
print('Goodbye')

# TOPIC 6: Writing Own Functions


def hello(name):
    print('Howdy ' + name)


def plusOne(num):
    return num+1


hello('Alice')
hello('Bob')
newNumber = plusOne(5)
print(newNumber)

# None value
# Every function has a value. For ones who does not state to return any
# value like int/string, they return None
# None is not printed, simply being ignored.

spam = print()
print(spam == None)

# optional keyword arguments
# print function has optional key arg which are end, sep and file
print('hello ', ' world ', ' cat ', end='')
print('World!')

print('hello ', ' world ', ' cat', sep='booty')

# local and global scope


def spam():
    global eggs;
    eggs = 'Hello'
    print(eggs)


eggs = 42
spam()
print(eggs)
eggs = 'Suzy'
print(eggs)