from random import randint
from brain_games.functions import is_prime


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def game():
    question = randint(2, 20)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return(question, correct_answer)
