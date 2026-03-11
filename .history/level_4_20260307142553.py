import os
import shutil

while True:
    print("\nLEVEL 4 TASKS")
    print("1. Organize Files")
    print("2. Student Report")
    print("3. Daily Task Manager")
    print("4. Analyze Numbers from File")
    print("5. Exit")

    choice = input("Enter your choice: ")

# TASK 1 - FILE ORGANIZER
    if choice == "1":
        files = os.listdir()

        for file in files:
            if file.endswith(".txt"):
                os.makedirs("Text_Files", exist_ok=True)
                shutil.move(file, "Text_Files/" + file)

            elif file.endswith(".jpg"):
                os.makedirs("Images", exist_ok=True)
                shutil.move(file, "Images/" + file)

            elif file.endswith(".pdf"):
                os.makedirs("PDF_Files", exist_ok=True)
                shutil.move(file, "PDF_Files/" + file)

        print("Files organized")

# TASK 2 - STUDENT REPORT
    elif choice == "2":
        students = {
            "Alice": 85,
            "Bob": 45,
            "Charlie": 72
        }

        print("\nStudent Report")

        for name, marks in students.items():
            if marks >= 50:
                result = "Pass"
            else:
                result = "Fail"

            print(name, "-", marks, "-", result)

# TASK 3 - DAILY TASK MANAGER
    elif choice == "3":
        task = input("Enter today's task: ")

        file = open("tasks.txt", "a")
        file.write(task + "\n")
        file.close()

        print("Task saved")

        print("Your Tasks:")
        file = open("tasks.txt", "r")

        for line in file:
            print(line.strip())

        file.close()

# TASK 4 - NUMBER DATA ANALYSIS
    elif choice == "4":
        numbers = []

        try:
            file = open("numbers.txt", "r")

            for line in file:
                numbers.append(int(line.strip()))

            file.close()

            total = sum(numbers)
            average = total / len(numbers)
            maximum = max(numbers)

            print("Total:", total)
            print("Average:", average)
            print("Maximum:", maximum)

        except:
            print("numbers.txt file not found")

# EXIT
    elif choice == "5":
        print("Program ended")
        break

    else:
        print("Invalid choice")