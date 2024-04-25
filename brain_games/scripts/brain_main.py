import prompt
def brain_main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    return name

if __name__ == '__main__':
    brain_main()
