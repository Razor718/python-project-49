import random
DESC = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_simple(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def brain_prime():
    random_number = random.randint(1, 100)
    is_prime = is_simple(random_number)
    correct_answer = 'yes' if is_prime else 'no'
    return random_number, correct_answer
