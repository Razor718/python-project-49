import random
desc = 'What is the result of the expression?'
def brain_calc():
    global correct_answer, answer, desc
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
            correct_answer = a + b
        case '-':
            correct_answer = a - b
        case '*':
            correct_answer = a * b

def main():
    brain_calc()

if __name__ == '__main__':
    main()
