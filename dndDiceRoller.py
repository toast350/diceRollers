import random

while True:
    print('Press enter to roll dice, or type "exit" to exit')
    if input() == 'exit':
        break

    print('D4(1) D6(2) D8(3) D10(4) D12(5) D20(6) custom(7) exit(8)')
    diceSides = input()        
    if diceSides == '1':
        diceSides = 4
    elif diceSides == '2':
        diceSides = 6        
    elif diceSides == '3':
        diceSides = 8
    elif diceSides == '4':
        diceSides = 10
    elif diceSides == '5':
        diceSides = 12
    elif diceSides == '6':
        diceSides = 20 # reassigns values to diceSides
    elif diceSides == '7':
        print('Enter how many sides you want the dice to have')
        diceSides = int(input())
    elif diceSides == '8':
        continue
    else:
        print('Invalid input, try again')
        diceSides = '8'

    if diceSides != '8':
        print('How many dice do you want to roll?')
        diceAmount = int(input())
 
        print('You rolled ' + str(diceAmount) + ' D' + str(diceSides) + 's and got: ' + str(random.randint(1, (diceSides * diceAmount)))) # prints a random number from 1 to diceSides multiplied by diceNumber
        input()