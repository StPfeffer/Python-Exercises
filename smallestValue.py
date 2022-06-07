smallest = None

print("Before")
for value in [6, 3, 41, 12, 9, 74, 15]:
    if smallest is None or value < smallest:
        smallest = value
    print(f"Smallest so far: {smallest}")

print("After")