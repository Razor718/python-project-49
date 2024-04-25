import prompt
import random
def main():
    print("Welcome to the Brain Games!")

main()

def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name

def get_progression():
    name_ = welcome_user()
    print('What number is missing in the proggresion?')
    userscore = 0
    winscore = 3
    # Циклом while ставлю ограничение на количество раундов
    while userscore < winscore:
        a = random.randint(1, 30)
        b = random.randint(31, 50)
        result = []
        # Циклом for генерирую последовательность
        for i in range(a, b, 3):
            result.append(i)
        random_index = result.pop(random.randint(0, len(result) - 1))
        print(f'Question: {result}')
        answer = prompt.integer('Your answer: ')
        # Делаю проверку на правильность ответа
        if answer == random_index:
            print('Correct!')
            userscore += 1
        else:
            print(
        f'''Question: {result}
        Your answer: {answer}
        {answer} is wrong answer ;(. Correct answer was {random_index}
        Let's try again, {name_}!''')
            break
        if userscore == 3:
            print(f'Congratulations, {name_}!')
        
get_progression()