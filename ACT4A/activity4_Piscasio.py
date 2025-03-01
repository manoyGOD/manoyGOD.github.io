import os

student_records = []

def open_file(filename):
    global student_records
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            student_records = [eval(line.strip()) for line in file]
        print(f"File '{filename}' opened successfully.")
    else:
        print(f"File '{filename}' does not exist.")

def save_file(filename):
    with open(filename, 'w') as file:
        for record in student_records:
            file.write(str(record) + '\n')
    print(f"File '{filename}' saved successfully.")

def save_as_file():
    filename = input("Enter new filename: ")
    save_file(filename)

def show_all_students():
    for record in student_records:
        print(record)

def get_last_name(record):
    return record[1][1]

def get_grade(record):
    return 0.6 * record[2] + 0.4 * record[3]

def order_by_last_name():
    sorted_records = sorted(student_records, key=get_last_name)
    for record in sorted_records:
        print(record)

def order_by_grade():
    sorted_records = sorted(student_records, key=get_grade, reverse=True)
    for record in sorted_records:
        print(record)

def show_student_record():
    student_id = input("Enter student ID: ")
    for record in student_records:
        if record[0] == student_id:
            print(record)
            return
    print("Student record not found.")

def add_record():
    student_id = input("Enter student ID (6 digits): ")
    while len(student_id) != 6 or not student_id.isdigit():
        print("Invalid student ID. Please enter a 6-digit number.")
        student_id = input("Enter student ID (6 digits): ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    class_standing = float(input("Enter class standing grade: "))
    major_exam = float(input("Enter major exam grade: "))
    student_records.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Record added successfully.")

def edit_record():
    student_id = input("Enter student ID to edit: ")
    for i, record in enumerate(student_records):
        if record[0] == student_id:
            first_name = input("Enter new first name: ")
            last_name = input("Enter new last name: ")
            class_standing = float(input("Enter new class standing grade: "))
            major_exam = float(input("Enter new major exam grade: "))
            student_records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record updated successfully.")
            return
    print("Student record not found.")

def delete_record():
    student_id = input("Enter student ID to delete: ")
    for i, record in enumerate(student_records):
        if record[0] == student_id:
            del student_records[i]
            print("Record deleted successfully.")
            return
    print("Student record not found.")

def main():
    filename = "student_records.txt"
    menu_options = {
        '1': open_file,
        '2': save_file,
        '3': save_as_file,
        '4': show_all_students,
        '5': order_by_last_name,
        '6': order_by_grade,
        '7': show_student_record,
        '8': add_record,
        '9': edit_record,
        '10': delete_record,
        '11': exit
    }
    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        choice = input("Enter your choice: ")

        if choice in menu_options:
            if choice in ['1', '2']:
                menu_options[choice](filename)
            else:
                menu_options[choice]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()