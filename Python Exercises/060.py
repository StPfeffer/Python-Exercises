numbers = [x for x in input("Enter some words: ") if x.isdigit()]
print(numbers)

print()
print("Solution: ")

import re


s = input("Enther some words: ")
print(re.findall("\d+", s))
