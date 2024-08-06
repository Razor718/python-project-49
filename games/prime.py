import prompt
import random

def is_simple(number):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def brain_prime():
    global is_prime, answer, random_number
    random_number = random.randint(1, 100)
    is_prime = is_simple(random_number)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')

def main():
    brain_prime()

if __name__ == '__main__':
    main()
