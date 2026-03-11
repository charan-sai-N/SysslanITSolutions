def grid():
    numbers = []
    number = 1
    row_sums = []

    for i in range(3):
        row_sum = 0

        for j in range(3):
            print(number, end=" ")
            numbers.append(number)
            row_sum += number
            number += 1

        row_sums.append(row_sum)
        print()

    return numbers, row_sums


grid_numbers, row_sums = grid()

print("\nRow Sums:")

for i in range(len(row_sums)):
    print("Row", i+1, "Sum =", row_sums[i])


if len(grid_numbers) != len(set(grid_numbers)):
    print("the grid contains ")


user_input = int(input("\nEnter a number to check whether it exists in grid: "))

if user_input in grid_numbers:
    print("Number found")
else:
    print("Number not found")