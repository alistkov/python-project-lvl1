from random import randint


def is_even(num):
    return num % 2 == 0


def calculate_result(first, second, operator):
    if operator == '+':
        return first + second
    elif operator == '-':
        return first - second
    else:
        return first * second


def create_sequence(start, step):
    numbers = [start]
    for i in range(1, 5):
        numbers.append(start + step * i)

    random_index = randint(0, len(numbers) - 1)
    random_elem = numbers[random_index]
    numbers[random_index] = ".."
    sequence = ' '.join(str(num) for num in numbers)
    return (sequence, random_elem)
