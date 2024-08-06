from random import randint
desc = 'Answer "yes" if the number is even, otherwise answer "no".'
def brain_even():
    global desc, correct_answer, answer
    random_number = randint(1, 1000)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    if random_number % 2 != 0:
        correct_answer = 'no'
    print(f'Question: {random_number}')
    answer = input()
    print('Your answer: ' + answer)

def main():
    brain_even()

if __name__ == '__main__':
    main()
