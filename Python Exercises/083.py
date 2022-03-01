from time import time

start = time()

for _ in range(100):
    1 + 1
    
end = time()

print(f"Running time is: {end - start} seconds")

# Solução

from timeit import Timer


t = Timer("for i in range(100): 1 + 1")
print(t.timeit())
