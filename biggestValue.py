biggest = None

print("Before")
for value in [6, 3, 41, 12, 9, 74, 15]:
    if biggest is None or value > biggest:
        biggest = value
    print(f"Biggest so far: {biggest}")

print("After")
