from random import randint
from brain_games.functions import create_sequence


rules = 'What number is missing in the progression?'


def game():
    start_elem = randint(2, 10)
    step = randint(1, 9)
    (question, correct_answer) = create_sequence(start_elem, step)
    return (question, correct_answer)
