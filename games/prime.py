import prompt
import random
from brain_games.scripts.brain_main import brain_main

def is_simple(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def check_simplicity():
    name = brain_main()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    userscore = 0
    winscore = 3
    while userscore < winscore:
        random_number = random.randint(1, 100)
        is_prime = is_simple(random_number)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if is_prime and answer == 'yes':
            print('Correct!')
            userscore += 1
        elif not is_prime and answer == 'no':
            print('Correct!')
            userscore += 1
        else:
            print(
        f'''Question: {random_number}
        Your answer: {answer}
        {answer} is wrong asnwer;(.
        Correct asnwer was {'yes' if is_prime else 'no'}
        Let's try again, {name}!''')
            break
        if userscore == 3:
            print(f'Congratulations, {name}!')
def main():
    check_simplicity()

if __name__ == '__main__':
    main()
