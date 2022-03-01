def find_number():
    for i in range(2000, 3200 + 1):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end = ", ")
    print("FIM.")


find_number()

print()

numbers = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0 :
        numbers.append(str(i))

print(",".join(numbers))