# format: username@companyname.com

email = [x for x in input("Enter the email: ").split("@")]
del email[0]
company_name = [x.split(".") for x in email]
print(company_name[0][0])

print()
print("Solution: ")

import re


emailAddres = input("Enter the email: ")
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2, emailAddres)
print(r2.group(2))
