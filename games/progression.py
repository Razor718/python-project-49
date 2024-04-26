import prompt
import random
from brain_games.scripts.brain_main import brain_main


def get_progression():
    name = brain_main()
    print('What number is missing in the progression?')
    userscore = 0
    winscore = 3
    # Циклом while ставлю ограничение на количество раундов
    while userscore < winscore:
        a = random.randint(1, 50)
        b = random.randint(51, 100)
        result = []
        # Циклом for генерирую последовательность
        for i in range(a, b, 3):
            result.append(i)
            ten_numbers = result[0:10]
        random_index = random.choice(ten_numbers)
        index = ten_numbers.index(random_index)
        ten_numbers[index] = '..'
        question = ''
        for elem in ten_numbers:
            question += str(elem)
            question += ' '
        print(f'Question: {question}')
        answer = prompt.integer('Your answer: ')
        # Делаю проверку на правильность ответа
        if answer == random_index:
            print('Correct!')
            userscore += 1
        else:
            print(
f'''Question: {question}
Your answer: {answer}
{answer} is wrong answer ;(. Correct answer was {random_index}
Let's try again, {name}!''')
            break
        if userscore == 3:
            print(f'Congratulations, {name}!')


def main():
    get_progression()


if __name__ == '__main__':
    main()
