import math
from random import randint


rules = 'Find the greatest common divisor of given numbers.'


def game():
    first = randint(2, 20)
    second = randint(2, 20)
    question = f'{first} {second}'
    correct_answer = math.gcd(first, second)
    return (question, correct_answer)
