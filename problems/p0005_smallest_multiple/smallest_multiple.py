"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from problems.tools import evenly_divisible


def smallest_multiple():
    previous_number = 0
    current_number = 0
    stop = False
    while not stop:
        current_number += 1
        if evenly_divisible(current_number, 21):
            if current_number > previous_number:
                stop = True
                return current_number
            previous_number = current_number


print(smallest_multiple())
# 232792560
