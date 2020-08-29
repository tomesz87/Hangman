# Write your code here
import random
import sys

print("H A N G M A N")

choice = ''

while choice.lower() not in ['play', 'exit']:
    choice = input('Type "play" to play the game, "exit" to quit:')

if choice.lower() == 'exit':
    sys.exit(0)

list_available = ['python', 'java', 'kotlin', 'javascript']
to_guess = random.choice(list_available)
current = '-' * len(to_guess)
tries = 8

already_typed = set()

letters = set(to_guess)
while tries > 0:
    print()
    print(current)
    # print('Input a letter:')
    letter = input('Input a letter:')

    if len(letter) != 1:
        print('You should input a single letter')
        continue

    if letter not in set('abcdefghijklmnopqrtsuvwxyz'):
        print('It is not an ASCII lowercase letter')
        continue

    if letter in already_typed:
        print("You already typed this letter")
        continue

    if letter in letters:
        letters.discard(letter)
        if len(letters) == 0:
            break
        current = to_guess
        for c in letters:
            current = current.replace(c, "-")
    else:
        print("No such letter in the word")
        tries -= 1
    already_typed.add(letter)
if tries > 0:
    print("You survived!")
else:
    print("You are hanged!")

print("Thanks for playing!")
print("We'll see how well you did in the next stage")
