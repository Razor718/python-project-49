from brain_games.games.calc import brain_calc
from brain_games.games import calc
from brain_games.games.game_engine import launch_the_game


def main():
    launch_the_game(calc, brain_calc)


if __name__ == '__main__':
    main()
