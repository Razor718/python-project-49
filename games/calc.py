import prompt
import random


def main():
    print("Welcome to the Brain Games!")


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name


main()
name_ = welcome_user()
print('What is the result of the expression?')


def get_expression():
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    operators = ['+', '-', '*', '/']
    random_operator = random.choice(operators)
    expression = a, random_operator, b
    print(f'Question: {expression}')
    answer = input()
    print('Your answer: ' + answer)
    if answer == :
       print('Correct!')
    else:
        print(f'''{answer} is wrong answer ;(.
              Correct answer was .
              Let`s try again, {name_}''') 


get_expression()