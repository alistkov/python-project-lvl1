from random import randint
from brain_games.functions import create_sequence


rules = 'What number is missing in the progression?'


def game():
    start_elem = randint(2, 10)
    step = randint(1, 9)
    (sequence, correct_answer) = create_sequence(start_elem, step)
    question = f'Question {sequence}'
    return (question, correct_answer)
