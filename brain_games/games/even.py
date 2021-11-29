from random import randint
from brain_games.functions import is_even


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def game():
    question = randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return (question, correct_answer)
