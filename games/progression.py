import prompt
import random

def brain_progression():
    print('What number is missing in the progression?')
    global answer, random_index, str_result
    a = random.randint(1, 85)
    b = random.randint(99, 101)
    c = random.randint(2, 3)
    result = list(range(a, b, c))
    random_index = random.choice(result[0:10])
    index = result.index(random_index)
    result[index] = '..'
    str_result = ' '.join(map(str, result))
    print(f'Question: {str_result}')
    answer = prompt.integer('Your answer: ')

def main():
    brain_progression()

if __name__ == '__main__':
    main()
