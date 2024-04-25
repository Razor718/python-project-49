import prompt
from random import randint


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name


def main():
    print("Welcome to the Brain Games!")


main()



def get_number():
    name_ = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    usercore = 0
    winscore = 3
    while usercore < winscore:
        random_number = randint(1, 1000)
        print(f'Question: {random_number}')
        answer = input()
        print('Your answer: ' + answer)
        if random_number % 2 == 0 and answer != 'yes':
            print(f'''{answer} is wrong answer ;(.
            Correct answer was yes.
            Let`s try again, {name_}''')
            break
        elif random_number % 2 != 0 and answer != 'no':
            print(f'''{answer} is wrong answer ;(.
            Correct answer was no.
            Let`s try again, {name_}''')
            break
        else:
            print('Correct!')
            usercore += 1
        if usercore == 3:
            print(f'Congratulation, {name_}!') 
get_number()