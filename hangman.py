print("H A N G M A N")

import random
import string
def menu():
    choice = input('Type "play" to play a game, "exit" to quit: ')
    if choice == 'exit':
        quit()
    elif choice != 'play':
        menu()

menu()
possible_answer = ['python', 'java', 'kotlin', 'javascript']
solution = random.choice(possible_answer)
tries = 8

right_input = []
wrong_input = []
output = len(solution) * '-'

while tries > 0:
    print()
    print(output)

    letter = input('Input a letter: ')
    output = ''

    if len(letter) > 1:
        print('You should print a single letter')

    elif letter not in string.ascii_lowercase:
        print('It is not an ASCII lowercase letter')

    elif letter in right_input or letter in wrong_input:
        print('You already typed this letter')

    elif letter not in solution:
        print('No such letter in the word')
        wrong_input.append(letter)
        tries -= 1

    elif letter not in right_input:
        right_input.append(letter)

    for char in solution:
        if char in right_input:
            output += char
        else:
            output += '-'

    if output in possible_answer:
        print(f'You guessed the word {solution}!')
        print('You survived!')
        break

if tries == 0:
    print('You are hanged!')
