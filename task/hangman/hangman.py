# Write your code here
import random
import sys

print("H A N G M A N")

choice = ''

while choice.lower() not in ['play', 'exit']:
    choice = input('Type "play" to play the game, "exit" to quit:')

if choice.lower() == 'exit':
    end(0)

list_available = ['python', 'java', 'kotlin', 'javascript']
to_guess = random.choice(list_available)
current = '-' * len(to_guess)
tries = 8

letters = set(to_guess)
while tries > 0:
    print()
    print(current)
    # print('Input a letter:')
    letter = input('Input a letter:')

    if letter in letters:
        letters.discard(letter)
        if len(letters) == 0:
            break
        current = to_guess
        for c in letters:
            current = current.replace(c, "-")
    elif letter in set(to_guess):
        print("No improvements")
        tries -= 1
    else:
        print("No such letter in the word")
        tries -= 1

if tries > 0:
    print("You survived!")
else:
    print("You are hanged!")

print("Thanks for playing!")
print("We'll see how well you did in the next stage")
