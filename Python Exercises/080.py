from random import sample

print(sample([i for i in range(0, 1001) if i % 5 == 0 and i % 7 == 0], 5))
