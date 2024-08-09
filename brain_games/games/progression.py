import random
DESC = 'What number is missing in the progression?'


def brain_progression():
    a = random.randint(1, 85)
    b = random.randint(99, 101)
    c = random.randint(2, 3)
    result = list(range(a, b, c))
    random_index = random.choice(result[0:10])
    index = result.index(random_index)
    result[index] = '..'
    correct_answer = random_index
    str_result = ' '.join(map(str, result))
    return str_result, str(correct_answer)
