from brain_games.games.progression import brain_progression
from brain_games.games import progression
from brain_games.games.game_engine import launch_the_game


def main():
    launch_the_game(progression, brain_progression)


if __name__ == '__main__':
    main()
