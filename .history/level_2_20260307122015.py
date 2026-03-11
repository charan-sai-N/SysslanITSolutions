import random
import string

def validate_email(email):

    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    at_position = email.index("@")
    if at_position < 3:
        return False

    if not email.endswith("@gmail.com"):
        return False

    return True


email = input("Enter your mail address: ")

if validate_email(email):
    print("Valid email")
else:
    print("Invalid email")





characters = string.ascii_letters + string.digits

password = ""

for i in range(8):
    password += random.choice(characters)

print("Generated Password:", password)

string_count = 0
number_count = 0
for i in password:
    if i == str(i):
        string_count += 1
    else:
        number_count += 1
print(string_count)
print(numb)