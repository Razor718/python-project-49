from brain_games_ import main
import brain_games_
from random import randint
main()
print('Answer "yes" if the number is even, otherwise answer "no"')
n = 0


def get_number():
    global random_number
    random_number = randint(1, 1000)
    print(f'Question: {random_number}')
    answer = input()
    print('Your answer: ' + answer)
    if random_number % 2 == 0 and answer == 'yes':
        print('Correct!')
    elif random_number % 2 != 0 and answer == 'no':
        print('Correct!')
    else:
        global n
        n = 1
        if answer == 'yes':
            correct_answer = 'no'
        else:
            correct_answer = 'yes'
        print(f'''{answer} is wrong answer ;(.
              Correct answer was {correct_answer}.
              Let`s try again, {brain_games_.name1}''')


for i in range(3):
    i += 1
    get_number()
if n == 0:
    print(f'Congratulations, {brain_games_.name1}!')
