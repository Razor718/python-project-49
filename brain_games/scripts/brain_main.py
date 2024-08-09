import prompt


def greet_the_player():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name


if __name__ == '__main__':
    greet_the_player()
