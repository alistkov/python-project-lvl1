import prompt


def game_engine(rules, game_data):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(rules)
    steps = 3
    while steps > 0:
        (question, correct_answer) = game_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Answer: ')
        if user_answer != str(correct_answer):
            print(
                f'\'{user_answer}\' is wrong ',
                f'answer ;(. Correct answer was \'{correct_answer}\'')
            print(f'Let\'s try again, {name}!')
            return
        print('Correct!')
        steps -= 1
    print(f'Congratulations, {name}!')
