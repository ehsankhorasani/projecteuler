"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from problems.tools import is_prime, is_factor
import math


def largest_prime_factor():
    goal_number = 600851475143
    factors = []
    for i in range(2, goal_number):
        if math.prod(factors) == goal_number:
            break

        if is_factor(goal_number, i) and is_prime(i):
            factors.append(i)

    return sorted(factors)[-1]


print(largest_prime_factor())
