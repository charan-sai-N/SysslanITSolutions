def grid():
    numbers = []
    number = 1

    for i in range(3):
        for j in range(3):
            print(number, end=" ")
            numbers.append(number)
            number += 1
        print()
    
    return numbers
grid_numbers = grid()

user_input = int(input("Enter a number to check whether it exists in grid: "))

if user_input in grid_numbers:
    print("Number found")
else:
    print("Number not found")


number = 1
for i in range(3):
    sum = 0
    for j in range(3):
        sum = sum + number
        
