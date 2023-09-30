import random

while True:
    print('Press enter to roll dice, or type "exit" to exit')
    if input() == 'exit':
        break

    print('D4(1) D6(2) D8(3) D10(4) D12(5) D20(6) custom(7) cancel(8)')
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
        try: diceSides = int(input('Enter how many sides you want the dice to have'))
        except ValueError:
            diceSides = '8'
            print('Invalid input')
    elif diceSides == '8':
        continue
    else:
        diceSides = '8'
        print('Invalid input')

    if diceSides != '8':
        try: diceAmount = int(input('How many dice do you want to roll?\n'))
        except ValueError:
            diceAmount = 'error'
            print('Invalid input')
 
        if diceAmount == 'error':
            continue
        elif diceAmount == 1:
            print('You rolled 1 D%s, and got %s.' %(str(diceSides), str(random.randint(1, diceSides))))
        else:
            total = 0
            print('Rolling dice:')
            for i in range(diceAmount):
                roll = random.randint(1, diceSides)
                print(roll)
                total += roll

            print('You rolled %s D%ss and got %s.' % (str(diceAmount), str(diceSides), str(total)))
        input()