from brain_games.games.prime import brain_prime
from brain_games.games import prime
from brain_games.games.game_engine import launch_the_game


def main():
    launch_the_game(prime, brain_prime)


if __name__ == '__main__':
    main()
