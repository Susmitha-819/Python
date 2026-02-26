students = ["susmi", "hari", "sai", "harsha", "sree"]

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")
    print("4.Remove")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name to add: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        print("Student List:")
        for student in students:
            print(student)

    elif choice == "3":
        print("Exiting program")
        break
    elif choice=="4":
        name = input("Enter student name to Remove: ")
        students.remove(name)
        print("Student remove successfully!")


    else:
        print("Invalid choice")
