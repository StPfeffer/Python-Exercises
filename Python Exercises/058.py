# format: "username@companyname.com"

email = [x for x in input("Enter the email: ").split("@")]
username = email[0]
# companyname = email[1]
print(username)
# print(companyname)

print()
print("Solution:")

import re


emailAddres = input("Enter the email: ")
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2, emailAddres)
print(r2.group(1)) #username
# print(r2.group(2)) # companyname.com
