import prompt
import random


def main():
    print("Welcome to the Brain Games!")

main()


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name


def find_divisor():
    name_ = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    user_score = 0
    winscore = 3
    while user_score < winscore:
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
        if answer == result:
            print('Correct!')
            user_score += 1
        else:
            print(f'''{answer} is wrong answer ;(.
            Correct answer was {result}.
            Let's try again, {name_}!''')
            break

        if user_score == 3:
            print(f"Congratulations, {name_}!")


find_divisor()
