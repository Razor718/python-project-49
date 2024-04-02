import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name


def main():
    print("Welcome to the Brain Games!")


main()


name_ = welcome_user()
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
              Let`s try again, {name_}''')


for i in range(3):
    i += 1
    get_number()
if n == 0:
    print(f'Congratulations, {name_}!')
