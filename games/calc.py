import prompt
import random
from brain_games.scripts.brain_main import brain_main



def get_expression():
    name = brain_main()
    print('What is the result of the expression?')
    userscore = 0
    winscore = 3
    while userscore < winscore:
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        operators = ['+', '-', '*']
        random_operator = random.choice(operators)
        operator = ''
        for elem in random_operator:
            operator += str(elem)
            operator += ''
        expression = a, operator, b
        print('Question:', a, operator, b)
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
                Question: {a} {operator} {b}
                {answer} is wrong answer ;(.
                Correct answer was {c}.
                Let's try again, {name}!''')
            break
        if userscore == 3:
            print(f'Congratulations, {name}!')

def main():
    get_expression()

if __name__ == '__main__':
    main()

