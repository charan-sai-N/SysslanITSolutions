import os
import shutil

while True:

    print("\nLEVEL 4 TASKS")
    print("1 Organize Files")
    print("2 Student Report")
    print("3 Daily Task List")
    print("4 Number File Analysis")
    print("5 Exit")

    choice = input("Enter your choice: ")

# Task 1 - Organize files
    if choice == "1":

        file_list = os.listdir()

        for f in file_list:

            if f.endswith(".txt"):
                os.makedirs("Text_Files", exist_ok=True)
                shutil.move(f, "Text_Files/" + f)

            elif f.endswith(".jpg"):
                os.makedirs("Images", exist_ok=True)
                shutil.move(f, "Images/" + f)

            elif f.endswith(".pdf"):
                os.makedirs("PDF_Files", exist_ok=True)
                shutil.move(f, "PDF_Files/" + f)

        print("Files moved to folders")

# Task 2 - Student report
    elif choice == "2":

        students = {
            "Ali": 80,
            "Sara": 45,
            "John": 70
        }

        print("\nStudent Report")

        for name in students:
            marks = students[name]

            if marks >= 50:
                result = "Pass"
            else:
                result = "Fail"

            print(name, "-", marks, "-", result)

# Task 3 - Daily task list
    elif choice == "3":

        task = input("Enter today's task: ")

        file = open("tasks.txt", "a")
        file.write(task + "\n")
        file.close()

        print("Task saved")

        print("\nYour tasks:")

        file = open("tasks.txt", "r")

        for line in file:
            print(line.strip())

        file.close()

# Task 4 - Number file analysis
    elif choice == "4":

        numbers = []

        try:
            file = open("numbers.txt", "r")

            for line in file:
                num = int(line.strip())
                numbers.append(num)

            file.close()

            total = sum(numbers)
            avg = total / len(numbers)
            highest = max(numbers)

            print("Total =", total)
            print("Average =", avg)
            print("Maximum =", highest)

        except:
            print("numbers.txt file not found")

# Exit
    elif choice == "5":
        print("Program finished")
        break

    else:
        print("Wrong choice")


'''
Expected Output:

LEVEL 4 TASKS
1 Organize Files
2 Student Report
3 Daily Task List
4 Number File Analysis
5 Exit
Enter your choice: 1
Files moved to folders

LEVEL 4 TASKS
1 Organize Files
2 Student Report
3 Daily Task List
4 Number File Analysis
5 Exit
Enter your choice: 2

Student Report
Ali - 80 - Pass
Sara - 45 - Fail
John - 70 - Pass

LEVEL 4 TASKS
1 Organize Files
2 Student Report
3 Daily Task List
4 Number File Analysis
5 Exit
Enter your choice: 3
Enter today's task: python level 4
Task saved

Your tasks:
python level 4

LEVEL 4 TASKS
1 Organize Files
2 Student Report
3 Daily Task List
4 Number File Analysis
5 Exit
Enter your choice: 4
numbers.txt file not found

LEVEL 4 TASKS
1 Organize Files
2 Student Report
3 Daily Task List
4 Number File Analysis
5 Exit
Enter your choice: 5
Program finished
'''