import sqlite3


def Add_student():
    ID_no = int(input("Enter student ID ="))
    First_name = input("Enter First name =")
    Last_name = input("Enter Last name =")
    Ph_no = int(input("Enter phone number ="))
    D_O_B = input("Enter your date of birth =")
    blue.execute(
        "INSERT INTO student VALUES({}, '{}', '{}', {} ,'{}')".format(ID_no, First_name, Last_name, Ph_no, D_O_B))
    green.commit()
    print("New Student Added")
    List_students()
    run_again()


def Create_table():
    blue.execute("""create table if not exists student (
                     ID_no integer primary key not null,
                     First_name text not null,
                     Last_name text not null,
                     Ph_no integer,
                     D_O_B text)""")
    print("Table is Created")
    green.commit()


def Search_student():
    First_name = input("Enter Your name = ")
    data = blue.execute("select * from student where First_name = '{}'".format(First_name))
    for i in data:
        print("ID_no = ", i[0])
        print("First_name = ", i[1])
        print("Last_name = ", i[2])
        print("Ph_no = ", i[3])
        print("D_O_B = ", i[4])
    green.commit()
    print("Student found")
    run_again()


def Delete_student():
    blue.execute("select * from student")
    print(blue.fetchall())
    green.commit()
    First_name = input("Enter first Name = ")
    Last_name = input("Enter last name = ")
    blue.execute("delete from student where First_name = '{}' and Last_name = '{}'".format(First_name, Last_name))
    green.commit()
    print("Student Deleted")
    run_again()


def List_students():
    data = blue.execute('SELECT * FROM STUDENT ')
    for row in data:
        print(row)
    green.commit()
    run_again()


def run_again():
    r = input("Do you want to run this program again (yes/no) =")
    if r == 'yes':
        Manage_student()
    else:
        quit()


def Manage_student():
    choice = Choices()
    if choice == 1:
        Add_student()

    elif choice == 2:
        Search_student()

    elif choice == 3:
        Delete_student()

    elif choice == 4:
        List_students()

    else:
        print("INVALID CHOICE")

        run_again()


def Choices():
    print(" 1. Add Student \n 2. Search Student \n 3. Delete Student \n 4. List Of Student ")
    choice = int(input("Enter your choice ="))
    return choice


if __name__ == "__main__":
    green = sqlite3.connect("Studentmaster.db")
    blue = green.cursor()
    Create_table()
    Manage_student()
    green.close()
