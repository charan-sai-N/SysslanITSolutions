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



