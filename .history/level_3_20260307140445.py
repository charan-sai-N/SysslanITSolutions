records = []

while True:
    print("\n1 Add Record")
    print("2 Show Records")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        records.append(name)

    elif choice == "2":
        print("Records:")
        for r in records:
            print(r)

    elif choice == "3":
        break

    else:
        print("Invalid choice")


records = []

name = input("Enter name: ")
records.append(name)

file = open("records.txt", "a")

for r in records:
    file.write(r + "\n")

file.close()

print("Record saved")