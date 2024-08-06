from brain_games.scripts import brain_main


def launch_the_game(module):
    brain_main.brain_main()
    print(module.desc)
    userscore = 0
    winscore = 3
    while userscore < winscore:
        module.main()
        if module.correct_answer == module.answer:
            print('Correct!')
            userscore += 1
        else:
            print(f'''
{module.answer} is wrong answer ;(.
Correct answer was {module.correct_answer}.
Let's try again, {brain_main.name}!''')
            break
        if userscore == winscore:
            print(f'Congratulations, {brain_main.name}!')
