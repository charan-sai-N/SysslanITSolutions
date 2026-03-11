def grid():
    number = 1
        for i in range(3):
            for j in range(3):
                print(number,end = " ")
                number += 1
            print()
user_input = int(input("Enter a number to check weather the number is exists in grid or not: "))
