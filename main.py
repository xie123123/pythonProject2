"""Import random package"""
import random


def get_random_number(left, right):
    """Returns a random number between [left, right]"""
    return random.randint(left, right)


ERROR = '_'
CORRECT = 'O'
WRONG_SPOT = 'X'
RANDNUMBER = None


def get_result(rand_number, guess_):
    """Returns the matching result between the
    guessed number and the actual number"""
    while len(guess_) < len(rand_number):
        guess_ += '_'
    guess_array_ = [ERROR for i in range(len(rand_number))]
    print(rand_number, guess_)
    index = 0
    while index < len(rand_number):
        if guess_[index] == rand_number[index]:
            guess_array_[index] = CORRECT
        elif guess_[index] in rand_number:
            guess_array_[index] = WRONG_SPOT
        index += 1
    return guess_array_


while True:
    RANDNUMBER = str(get_random_number(1000, 9999))
    print("rand: ", RANDNUMBER)
    COUNT = 0
    while True:
        guess = input("Please enter the guessed number ('q' indicates exit):")
        if guess.upper() == 'Q':
            break
        COUNT += 1

        guess_array = get_result(RANDNUMBER, guess)

        print(guess_array)
        if ERROR not in guess_array and WRONG_SPOT not in guess_array:
            print("Congratulations, you guessed it right!")

    print(f"Try {COUNT} times in total")

    op = input("Continue (Y/N):")
    if op.upper() != 'Y':
        break
