from unittest import TestCase
from problems.tools import *


class TestTools(TestCase):

    def test_divisibility_to_3_or_5(self):
        self.assertTrue(divisibility_to_3_or_5(5))
        self.assertTrue(divisibility_to_3_or_5(10))
        self.assertFalse(divisibility_to_3_or_5(8))

    def test_is_even(self):
        self.assertTrue(is_even(6))
        self.assertFalse(is_even(7))

    def test_is_prime(self):
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(12))

    def test_is_factor(self):
        self.assertTrue(is_factor(6, 3))
        self.assertFalse(is_factor(5, 2))

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(906609))
        self.assertFalse(is_palindrome(906608))

    def test_evenly_divisible(self):
        self.assertTrue(evenly_divisible(2520, 10))
        self.assertFalse(evenly_divisible(2520, 15))
