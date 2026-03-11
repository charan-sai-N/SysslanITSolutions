import random

mail_id = '@gmail.com'
user_input = input("enter your mail address")
for i in user_input(len(-1,9)):
    if i in  mail_id:
        print("valid mail")
    else:
        print("invalid mail")