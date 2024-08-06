import random

def brain_calc():
    print('What is the result of the expression?')
    global a, b, c, answer, str_operator
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    operators = ['+', '-', '*']
    random_operator = random.choice(operators)
    str_operator = ' '.join(map(str, random_operator))
    print('Question:', a, str_operator, b)
    answer = int(input())
    print('Your answer:', answer)
    match random_operator:
        case '+':
            c = a + b
        case '-':
            c = a - b
        case '*':
            c = a * b

def main():
    brain_calc()

if __name__ == '__main__':
    main()
