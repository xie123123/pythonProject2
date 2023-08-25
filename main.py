import random


def getRandomNumber(a, b):
    return random.randint(a, b)


ERROR = '_'
CORRECT = 'O'
WRONG_SPOT = 'X'
randNumber = None


def getResult(randNumber, guess):
    while len(guess) < len(randNumber):
        guess += '_'
    guess_array = [ERROR for i in range(len(randNumber))]
    for i in range(len(randNumber)):
        if guess[i] == randNumber[i]:
            guess_array[i] = CORRECT
        elif guess[i] in randNumber:
            guess_array[i] = WRONG_SPOT
    return guess_array


while True:
    randNumber = str(getRandomNumber(1000, 9999))
    print("rand: ", randNumber)
    count = 0
    while True:
        guess = input("Please enter the guessed number ('q' indicates exit):")
        if guess.upper() == 'Q':
            break
        count += 1
        guess_array = getResult(randNumber, guess)

        print(guess_array)
        if ERROR not in guess_array and WRONG_SPOT not in guess_array:
            print("Congratulations, you guessed it right!")

    print("Try {} times in total".format(count))

    op = input("Continue (Y/N):")
    if op.upper() != 'Y':
        break
