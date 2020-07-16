"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
from problems.tools import is_palindrome


def largest_palindrome_product():
    palindromes = []
    for a in range(99, 999):
        for b in range(a, 999):
            first_number = a
            last_number = b
            result = first_number * last_number
            if is_palindrome(result):
                palindromes.append(result)
    return sorted(palindromes)[-1]


largest_palindrome_product()
# 906609
