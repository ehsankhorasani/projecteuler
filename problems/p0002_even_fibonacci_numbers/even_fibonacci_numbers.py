"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
https://projecteuler.net/problem=2
"""

from problems.tools import is_even


def sum_even_fibonacci_numbers():
    first_number, second_number = 1, 2
    result = 0

    while first_number < 4000000:
        if is_even(first_number):
            result += first_number
        result = first_number + second_number
        first_number, second_number = second_number, result

    return result


print(sum_even_fibonacci_numbers())
# Answer: 4613732
