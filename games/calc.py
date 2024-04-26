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
        str_operator = ' '.join(map(str, random_operator))
        print('Question:', a, str_operator, b)
        answer = int(input())
        print('Your answer: ', answer)
        match random_operator:
            case '+':
                c = a + b
            case '-':
                c = a - b
            case '*':
                c = a * b
        if c == answer:
            print('Correct!')
            userscore += 1
        else:
            print(f'''
                Question: {a} {str_operator} {b}
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
