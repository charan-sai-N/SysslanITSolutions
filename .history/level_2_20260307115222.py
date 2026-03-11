import random

mail_id = "@gmail.com"
user_input = input("Enter your mail address: ")
if user_input.endswith(mail_id) and " ":
    print("Valid mail")
else:
    print("Invalid mail")
