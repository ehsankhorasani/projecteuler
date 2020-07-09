"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
https://projecteuler.net/problem=1
"""

from problems.tools import divisibility_to_3_or_5


def multiples_of_3_and_5():
    result = 0
    for number in range(1000):
        if divisibility_to_3_or_5(number):
            result += number
    return result


print(multiples_of_3_and_5())

# Answer: 233168
