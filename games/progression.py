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
        a = random.randint(1, 85)
        b = random.randint(99, 101)
        c = random.randint(2, 3)
        # Генерирую последовательность функцией range
        result = list(range(a, b, c))
        random_index = random.choice(result[0:10])
        index = result.index(random_index)
        result[index] = '..'
        # Привожу список-прогрессию к строке и ставлю разделитель
        str_result = ' '.join(map(str, result))
        print(f'Question: {str_result}')
        answer = prompt.integer('Your answer: ')
        # Делаю проверку на правильность ответа
        if answer == random_index:
            print('Correct!')
            userscore += 1
        else:
            print(
                f'''Question: {str_result}
                Your answer: {answer}
                {answer} is wrong answer ;(.
                Correct answer was {random_index}
                Let's try again, {name}!''')
            break
        if userscore == 3:
            print(f'Congratulations, {name}!')


def main():
    get_progression()


if __name__ == '__main__':
    main()
