import random

wordlist = 'python', 'java', 'javascript', 'php'


def hangman():
    print('Hello and welcome to HANGMAN')
    secret = random.choice(wordlist)
    guesses = 'pj'
    turns = 8

    while turns > 0:
        missed = 0
        for letter in secret:
            if letter in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
                missed += 1

        if missed == 0:
            print('\n YOU WON CONGRATULATIONS')
            break
        guess = input('\nWrite a letter ')
        guesses += guess

        if guess not in secret:
            turns -= 1
            print('\nOops mistake')

            print('\n', 'Attempts left: ', turns)

            if turns < 8:
                print('\n    | ')

            if turns < 7:
                print('   ___ ')

            if turns < 6:
                print('  0 - 0 ')

            if turns < 5:
                print('  /| |\ ')

            if turns < 4:
                print(' / | | \ ')

            if turns < 3:
                print('   | | ')

            if turns < 2:
                print('  /   \ ')

            if turns < 1:
                print(' dead... ')

            if turns == 0:
                print('\n\nCorrect answer: ', secret)


ans = 'yes'
while ans == 'yes':
    hangman()

    print('do you want try again? Yes or no?')
    ans = input()
