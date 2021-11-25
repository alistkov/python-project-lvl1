#!/usr/bin/env python
import random
import prompt
from brain_games.cli import welcome_user

operations = ['+', '-', '*']


def calculate_result(first, second, operator):
    if operator == '+':
        return first + second
    elif operator == '-':
        return first - second
    else:
        return first * second


def brain_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    steps = 3
    while steps > 0:
        first = random.randint(1, 10)
        second = random.randint(1, 10)
        operator = random.choice(operations)
        correct_answer = calculate_result(first, second, operator)
        print(f'Question: {first} {operator} {second}')
        user_answer = prompt.integer('Answer: ')
        if user_answer != correct_answer:
            print(
                f'\'{user_answer}\' is wrong ',
                f'answer ;(. Correct answer was \'{correct_answer}\'')
            print(f'Let\'s try again, {name}!')
            return
        print('Correct!')
        steps -= 1
    print(f'Congratulations, {name}!')


def main():
    brain_calc()


if __name__ == '__main__':
    main()
