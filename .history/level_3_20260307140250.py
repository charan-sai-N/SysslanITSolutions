name_list = []

while True:
    print("\n1. Add Name")
    print("2. Save to File")
    print("3. Read File")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        name_list.append(name)

    elif choice == "2":
        file = open("names.txt", "a")

        for n in name_list:
            file.write(n + "\n")

        file.close()
        print("Names saved")

    elif choice == "3":
        try:
            file = open("names.txt", "r")

            for line in file:
                print(line.strip())

            file.close()

        except:
            print("File not found")

    elif choice == "4":
        break

    else:
        print("Invalid option")3
        