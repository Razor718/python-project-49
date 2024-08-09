from brain_games.scripts.brain_main import greet_the_player
from brain_games.games.even import DESC
from brain_games.games.calc import DESC
from brain_games.games.gcd import DESC
from brain_games.games.prime import DESC
from brain_games.games.progression import DESC
WINSCORE = 3

def launch_the_game(game_func):
    userscore = 0
    name = greet_the_player()
    print(DESC)
    while userscore < WINSCORE:
        question, correct_answer = game_func()
        print(f'Question: {question}')
        answer = input()
        print('Your answer:', answer)
        if correct_answer == answer:
            print('Correct!')
            userscore += 1
        else:
            print(f'''
{answer} is wrong answer ;(.
Correct answer was {correct_answer}.
Let's try again, {name}!''')
            break
        if userscore == WINSCORE:
            print(f'Congratulations, {name}!')
