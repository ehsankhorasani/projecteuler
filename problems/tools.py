def divisibility_to_3_or_5(number):
    result = True if number % 3 == 0 or number % 5 == 0 else False
    return result


def is_even(number):
    result = True if number % 2 == 0 else False
    return result


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True


def is_factor(first_number, second_number):
    return first_number % second_number == 0


def is_palindrome(number: int):
    text = str(number)
    for i in range(len(text)):
        if text[i] != text[(i + 1) * (-1)]:
            return False
    return True


def evenly_divisible(divided, divisor: int):
    """
    :param divided: مقسوم
    :param divisor: مقسوم علیه
    :return:
    """
    for n in range(1, divisor):
        if divided % n != 0:
            return False
    return True
