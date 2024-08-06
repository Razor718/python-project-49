import prompt
import random

def brain_gcd():
    print('Find the greatest common divisor of given numbers.')
    global result, answer
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print(f"Question: {a} {b}")
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    result = a + b
    answer = prompt.integer("Your answer: ")

def main():
    brain_gcd()

if __name__ == '__main__':
    main()
