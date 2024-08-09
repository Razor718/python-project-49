import random
DESC = 'Find the greatest common divisor of given numbers.'


def brain_gcd():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = f'{a} {b}'
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    correct_answer = a + b
    return question, str(correct_answer)


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
