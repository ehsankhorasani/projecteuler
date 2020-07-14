from problems.tools import is_palindrome


def largest_palindrome_product():
    palindromes = []
    for a in range(99, 999):
        for b in range(a, 999):
            first_number = a
            last_number = b
            result = first_number * last_number
            if is_palindrome(str(result)):
                palindromes.append(result)
    return sorted(palindromes)[-1]


largest_palindrome_product()
# 906609
