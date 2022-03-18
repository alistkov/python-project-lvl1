#!/usr/bin/env python
from brain_games.game_engine import game_engine
from brain_games.games.gcd import rules, game


def main():
    game_engine(rules, game)


if __name__ == '__main__':
    main()