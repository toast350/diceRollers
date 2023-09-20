import random

while True:
    print('Press enter to roll dice or type "exit" to exit')
    if input() == 'exit':
        break
    print('How many sides on the dice?')
    diceSides = int(input()) # asks how many sides on the dice

    print('How many dice?')
    diceNumber = int(input()) # asks how many dice to roll

    print('You rolled: ' + str(random.randint(1, (diceSides * diceNumber)))) # prints a random number from 1 to diceSides multiplied by diceNumber