from problems.tools import divisibility_to_3_or_5

print(sum([number if divisibility_to_3_or_5(number) else 0 for number in range(1000)]))
# Answer: 233168
