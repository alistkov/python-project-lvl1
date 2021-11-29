def is_even(num):
    return num % 2 == 0


def calculate_result(first, second, operator):
    if operator == '+':
        return first + second
    elif operator == '-':
        return first - second
    else:
        return first * second
