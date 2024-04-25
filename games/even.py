import prompt
from random import randint
from brain_games.scripts.brain_main import brain_main


def get_number():
    name = brain_main()
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
            Let's try again, {name}!''')
            break
        elif random_number % 2 != 0 and answer != 'no':
            print(f'''{answer} is wrong answer ;(.
            Correct answer was no.
            Let's try again, {name}!''')
            break
        else:
            print('Correct!')
            usercore += 1
        if usercore == 3:
            print(f'Congratulations, {name}!') 

def main():
    get_number()

if __name__ == '__main__':
    main()