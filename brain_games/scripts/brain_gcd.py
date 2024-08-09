from brain_games.games.gcd import brain_gcd
from brain_games.games import gcd
from brain_games.games.game_engine import launch_the_game


def main():
    launch_the_game(gcd, brain_gcd)


if __name__ == '__main__':
    main()
