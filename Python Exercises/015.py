number = int(input("Enter a number: "))

sum = 0

for i in range(1, 5):
    sum += int(str(number) * i)

print(sum)

print()

a = input("Enter a number: ")
n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
n4 = int("%s%s%s%s" % (a, a, a, a))
print(n1 + n2 + n3 + n4)
