records = []

while True:
    print("\n1 Add Record")
    print("2 Show Records")
    print("3 Save Records to File")
    print("4 Read Records from File")
    print("5 Add Log Message")
    print("6 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        records.append(name)

    elif choice == "2":
        print("Records:")
        for r in records:
            print(r)

    elif choice == "3":
        file = open("records.txt", "a")

        for r in records:
            file.write(r + "\n")

        file.close()
        print("Records saved")

    elif choice == "4":
        try:
            file = open("records.txt", "r")

            for line in file:
                print(line.strip())

            file.close()

        except:
            print("File not found")

    elif choice == "5":
        from datetime import datetime

        message = input("Enter log message: ")
        file = open("log.txt", "a")

        time = datetime.now()
        file.write(str(time) + " - " + message + "\n")

        file.close()
        print("Log saved")

    elif choice == "6":
        break

    else:
        print("Invalid choice")


