#CRUD

students = [
    {
        "id": 1001,
        "name": "John",
        "surname": "Doe",
        "fathers_name": "Michael",
        "age": 15,
        "class": 1,
        "id_number": "AN123456"
    },
    {
        "id": 1002,
        "name": "Nikos",
        "surname": "Strafiotis",
        "fathers_name": "Dimitris",
        "age": 17,
        "class": 2,
        "id_number": "AN135724"
    },
{
        "id": 1003,
        "name": "Anestis",
        "surname": "Strafiotis",
        "fathers_name": "Dimitris",
        "age": 15,
        "class": 1,
        "id_number": "AN246813"
    }
]

def create_student():
    name = input("Give student's name: ")
    surname = input("Give student's surname: ")
    fathers_name = input("Give student's fathers name: ")
    stop = False

    for s in students:
        if name == s["name"] and surname == s["surname"] and fathers_name == s["fathers_name"]:
            print("This student already exists.")
            ch = input("Do you still want to continue: (y-yes , n-no")
            if ch == "n":
                stop = True
                break
    if stop:
        return

    age = int(input("Give age: "))
    students_class = int(input("Give student's class:  "))
    id_card = input("Does he/she has an id card: (y-true , n-false)?")
    student = dict()
    student["name"] = name
    student["surname"] = surname
    student["fathers_name"] = fathers_name
    student["age"] = age
    student["class"] = students_class

    if id_card == "y":
        st_id = input("Give student's id: ")
        student["id_number"] = st_id

    student["id"] = next_id()
    students.append(student)

    return student

def print_student(student):
    print("NEW STUDENT: ")
    print(f"name: {student['name']}")
    print(f"surname: {student['surname']}")
    print(f"fathers name: {student['fathers_name']}")
    print(f"age: {student['age']}")
    print(f"class: {student['class']}")
    if "id_number" in student:
        print(f"id_number: {student['id_number']}")

def next_id():
    ids = []
    for st in students:
        ids.append(st["id"])
    return max(ids) + 1

def print_student_details():
    for student in students:
        print_student(student)
        print("--------------")

def print_student_names():
    for student in students:
        print(f"{student['name']} {student['fathers_name'][0]}. {student['surname']}")

def submenu2():
    ch = input("SubMenu: 1-Print a student, 2-Print all, 3-Print all (only names): ")

    # check if only digits and between limits
    while not (ch.isdigit() and 1 <= int(ch) <= 3):
        ch = input("Wrong input! Choose one of the options (1-3): ")

    ch = int(ch)

    if ch == 1:
        st_id = input("Give student's id: ")
        for student in students:
            if st_id in student['id_number']:
                print_student(student)

    elif ch == 2:
        print_student_details()
    else:
        print_student_names()


def search_student_by_surname(surname):
    match_students = []
    for student in students:
        if surname in student['surname']:
            match_students.append(student)
    return match_students

def search_student_by_id(student_id):
    for student in students:
        if student_id == student['id']:
            return student



def update_student(ch):
    # Update by ID
    if ch ==  1:
        update_sector()
    #Update by username
    elif ch == 2:
        surname = input("Give student's surname: ")
        matching_students = search_student_by_surname(surname)

        if not matching_students:
            print("There are no students with this surname!")

        elif len(matching_students) == 1:
            student = matching_students[0]
            update_sector(student["id"])  # Proceed directly to update if there's only one match

        elif len(matching_students) > 1:
            for s in matching_students:
                print_student(s)
                print(f"id = {s['id']}")
                print("-" * 15)

            # Prompt the user to select a student by ID from the matches
            student_id = int(input("Please select a student's ID from the above list: "))
            update_sector(student_id)  # Proceed to update the selected student


def update_sector(student_id=None):
    if student_id is None:  # If no ID is passed, ask the user for it
        student_id = int(input("Give id: "))

    student = search_student_by_id(student_id)

    if student is None:
        print("Error! There are no students with this id!")

    else:
        sector = input(
            "Choose what sector do you want to change.(N -name, S -surname, F -father's_name, A -age, C -class, I -id_number: ").strip()
        while not (sector == 'S' or sector == 'N' or sector == 'F' or sector == 'A' or sector == 'C' or sector == 'I'):
            sector = input("Wrong input! Choose one of the options (N | F | S | A | C | I)! ").strip()

        if sector == 'S':
            student['surname'] = input("Give student's new surname: ")
        elif sector == 'N':
            student['name'] = input("Give student's new name: ")
        elif sector == 'F':
            student['fathers_name'] = input("Give student's new father's name: ")
        elif sector == 'A':
            student['age'] = int(input("Give student's new age: "))
        elif sector == 'C':
            student['class'] = input("Give students new class: ")
        elif sector == 'I':
            student['id_number'] = input("Give student's new id_number: ")

        print("=" * 15)
        print_student(student)
        print("Student updated!")



def submenu3():
    print("         SUBMENU(UPDATE)         ")
    update_choice = input("Choose 1 if you want to update by id | Choose 2 if you want to update by surname:")
    if update_choice.strip().isdigit():
        update_choice = int(update_choice)
    else:
        print("Wrong input!")

    if update_choice == 1:
        update_student(1)

    elif update_choice == 2:
        update_student(2)

    else:
        print("Invalid choice, please choose 1 or 2.")




def main():

    while True:
        print("--------------")
        print("     MENU     ")
        print("Menu : 1-Register a student, 2-Print, 3-Update a registration, 4-Delete a registration, 5-quit ")
        user = int(input("Choose option 1-5: "))

        if user == 1:
            student = create_student()
            print_student(student)

        elif user == 2:
            submenu2()

        elif user == 3:
            submenu3()

        elif user == 4:
            pass
        elif user == 5:
            break
        else:
            print("Wrong input!")


main()