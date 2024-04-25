import prompt
import random


def main():
    print("Welcome to the Brain Games!")


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name


main()


def get_expression():
    name_ = welcome_user()
    print('What is the result of the expression?')
    userscore = 0
    winscore = 3
    while userscore < winscore:
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        operators = ['+', '-', '*']
        random_operator = random.choice(operators)
        print('Question:', a, random_operator, b)
        answer = int(input())
        print('Your answer: ', answer)
        c = 0
        if random_operator == '+':
            c = a + b
        if random_operator == '-':
            c = a - b
        if random_operator == '*':
            c = a * b
        if c == answer:
            print('Correct!')
            userscore += 1
        else:
            print(f'''
                Question: {a, random_operator, b}
                {answer} is wrong answer ;(.
                Correct answer was {c}.
                Let's try again, {name_}!''')
            break
        if userscore == 3:
            print(f'Congratulations, {name_}!')

get_expression()
