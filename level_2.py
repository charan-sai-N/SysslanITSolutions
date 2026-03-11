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
print("strings count in password = ",string_count)
print("numbers count in password = ",number_count)

user_input = int(input("enter a number to print fibonacci series up to number range: "))
a = 0
b = 1
for i in range(user_input):
    print(a,end =" ")
    a,b = b,a + b
    
'''Expected Output:
Enter your mail address: charan@gmail.com
Valid email
Generated Password: Q2wBatwW
strings count in password =  7
numbers count in password =  1
enter a number to print fibonacci series up to number range: 13
0 1 1 2 3 5 8 13 21 34 55 89 144
'''