from random import choice, randint
from brain_games.functions import calculate_result

operations = ['+', '-', '*']
rules = 'What is the result of the expression?'


def game():
    first = randint(1, 10)
    second = randint(1, 10)
    operator = choice(operations)
    question = f'{first} {operator} {second}'
    correct_answer = calculate_result(first, second, operator)
    return (question, correct_answer)
