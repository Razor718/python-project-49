from random import randint
DESC = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even():
    random_number = randint(1, 1000)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    if random_number % 2 != 0:
        correct_answer = 'no'
    return random_number, correct_answer
