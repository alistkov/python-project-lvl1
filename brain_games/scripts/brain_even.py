#!/usr/bin/env python
import prompt
import random
from brain_games.cli import welcome_user


def is_even(num):
    return num % 2 == 0


def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    steps = 3
    while steps > 0:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Answer: ')
        correct_answer = 'yes' if is_even(number) else 'no'
        if user_answer.lower() != correct_answer:
            print(
                f'\'{user_answer}\' is wrong ',
                f'answer ;(. Correct answer was \'{correct_answer}\'')
            print(f'Let\'s try again, {name}!')
            return
        print('Correct!')
        steps -= 1
    print(f'Congratulations, {name}!')


def main():
    brain_even()


if __name__ == '__main__':
    main()
