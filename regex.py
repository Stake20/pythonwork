import re

text = input("Email Address:")
password = input("Passcode:")

emailaddress = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
passcode = re.compile("[a-zA-Z0-9]+")

email = emailaddress.findall(text)
code = passcode.search(password)


print(email, code)