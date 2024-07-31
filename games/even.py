from random import randint

def brain_even():
    global random_number, answer
    random_number = randint(1, 1000)
    print(f'Question: {random_number}')
    answer = input()
    print('Your answer: ' + answer)

def main():
    brain_even()

if __name__ == '__main__':
    main()
