import random
DESC = 'What is the result of the expression?'


def brain_calc():
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)
    str_operator = ' '.join(map(str, random_operator))
    match random_operator:
        case '+':
            correct_answer = a + b
        case '-':
            correct_answer = a - b
        case '*':
            correct_answer = a * b
    return f'{a} {str_operator} {b}', str(correct_answer)
