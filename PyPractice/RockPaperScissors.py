import random

choices = ['rock', 'paper', 'scissors']

while True:
    print('Welcome to rock, paper, scissors! Lets see if you can win. (0 to exit.)')
    userChoice = int(input('Choose: 1. rock, 2. paper, 3. scissors\n'))
    randChoice = random.randint(1,3)

    if userChoice == 0:
        print('Come back next time!')
        break

    print('You chose ', choices[userChoice-1])
    print('The computer chose ', choices[randChoice-1])

    if userChoice == randChoice:
        print('This is a draw!')

    if userChoice < randChoice and userChoice != randChoice:
        if userChoice == 1 and randChoice == 3:
            print('Good job! You won against', choices[randChoice-1], '!')
            continue
        print('Woops, you lost to', choices[randChoice-1], '.')
    else:
        print('Good job! You won against', choices[randChoice-1], '!')

exit(1)
