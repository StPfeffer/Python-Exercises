value = []

for i in range(1000, 3001):
    str_i = str(i)

    if int(str_i[0]) % 2 == 0 and int(str_i[1]) % 2 == 0 and int(str_i[2]) % 2 == 0 and int(str_i[3]) % 2 == 0:
        value.append(str_i)

print(", ".join(value))