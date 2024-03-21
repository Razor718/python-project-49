from ..cli import name
from random import randint
print('Answer "yes" if the number is even, otherwise answer "no"')
random_number = randint(1, 1000)


def get_number():
    print(f'Question: {random_number}')


get_number()
answer = input()
print('Your answer: ' + answer)
if random_number % 2 == 0 and answer == 'yes':
    print('Correct!')
else:
    print('''"yes" is wrong answer ;(. Correct answer was "no".
          Let`s try again,''' (name))


if random_number % 2 != 0 and answer == 'no':
    print('Correct!')
else:
    print('''"yes" is wrong answer ;(. Correct answer was "no".
          Let`s try again,''' (name))
