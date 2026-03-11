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
    if i.isalpha():
        string_count += 1
    elif i.isdigit():
        number_count += 1
print("strings count = ",string_count)
print("numbers count = ",number_count)

user_input = int(input("enter a number to print fabonacci series up to number range: "))
a = 0
b
for i in range(user_input):
