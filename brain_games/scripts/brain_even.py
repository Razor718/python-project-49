from brain_games.games import even
from brain_games.games.even import brain_even
from brain_games.games.game_engine import launch_the_game


def main():
    launch_the_game(even, brain_even)


if __name__ == '__main__':
    main()
