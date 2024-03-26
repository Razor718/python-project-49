#!/usr/bin/python3
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    global name1
    name1 = welcome_user()


if __name__ == "__main__":
    main()
