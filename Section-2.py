print('\n\tTOPIC 2')
# if statement
name = 'alice'
if name == 'alice':
    print('Hi Alice')
print('Done')

# else statement
password = 'swordfish'
if password == 'swordfish':
    print('Access granted!')
else:
    print('Access not granted!')

# elif statement
name = 'Bob'
age = 3000

if name == 'alice':
    print('Hi, Alice!')
elif age < 12:
    print('You are not Alice, kiddo')
elif age > 2000:
    print('Unlike you, alice is not an undead, immortal vampire!')
elif age > 100:
    print('You are not Alice, grannie -,-')
else:
    print('Who are you?!')

# 'truthy' and 'falsey' statements, where we can tell if a usergives an
# input or not
print('Enter a name:')
name = input()
if name:  # should be more explicit.Like name != ' '
    print('Thanks for entering a name')
else:
    print('You did not enter a name')

print('\n\tTOPIC 3')
# for loop
spam = 0
while spam < 5:
    print('Hello World')
print('Done')

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you')

name = ''
while True:
    print('Please type your name: ')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is' + str(spam))

print('\n\tTOPIC 4')
# for loop
print('My name is')
for i in range(5):
    print('Jimmy Five Times' + str(i))

# Karle genius problem
total = 0
for num in range(101):
    total = total+num
print(total)

# includes range
print('My name is')
for i in range(12, 16):
    print('Jimmy Five Times' + str(i))

# includes range with step arg
print('My name is')
for i in range(0, 10, 2):
    print('Jimmy Five Times' + str(i))
