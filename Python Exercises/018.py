print("Tip: You can enter a sequence of passwords to validate them, just make sure they're comma separated without white space.")
username = str(input("Username: "))
password = [x for x in input("Password: ").split(",")]
valid_passwords = []

for p in password:
    if len(p) < 6 or len(p) > 12:
        continue
    else:
        pass
    for c in p:
        if not c.isalpha:
            continue
        elif not c.isdigit:
            continue
        elif not c in "ABDEFGHIJKLMNOPQRSTUVWXYZ":
            continue
        elif not c in "$#@":
            continue
        else:
            pass
    valid_passwords.append(p)

print(", ".join(valid_passwords))

print()

import re


value = []
items = [x for x in input("Password(s): ").split(",")]

for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    else:
        pass

    if not re.search("[a-z]", p):
        continue
    elif not re.search("[0-9]", p):
        continue
    elif not re.search("[A-Z]", p):
        continue
    elif not re.search("[$#@]", p):
        continue
    elif re.search("\s", p):
        continue
    else:
        pass

    value.append(p)

print(", ".join(value))
