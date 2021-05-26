# Section 5 TOPIC 9
# Make a guessing number game
import random
# prompt user for their name
print("Hello. What is your name? :)")
username = input()
# generate random number
theNum = random.randint(1, 20)
# tell user the range
print("Well, " + username + " I am thinking of a number between 1 and 20!")

# user gets 6 guesses
for guessesTaken in range(1, 7):
    print("Take a guess;)\n")
    userAnswer = int(input())
    if userAnswer > theNum:
        print("Your guess is too high")
    elif userAnswer < theNum:
        print("your guess is too low")
    else:
        break

if userAnswer == theNum:
    print('Good job, ' + username + " ! You guessed my number om " + guessesTaken + " guesses!")
else:
    print("Nope, The number I was thinking was " + str(theNum))

