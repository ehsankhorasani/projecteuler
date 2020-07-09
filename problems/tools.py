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


def is_factor(a, b):
    return a % b == 0
