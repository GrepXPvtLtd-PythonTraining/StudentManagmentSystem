import sqlite3


def addStudent():
    Id = int(input("Enter The Student Id = "))
    First_Name = input("Enter First Name = ")
    Last_Name = input("Enter Last Name = ")
    DOB = input("Enter Date Of Birth as dd-mm-yyyy = ")
    Phone_Number = int(input("Enter Phone Number = "))
    c.execute("INSERT INTO student VALUES({},'{}','{}','{}',{})".format(Id, First_Name, Last_Name, DOB, Phone_Number))
    con.commit()
    print("New Student Added")
    listStudent()
    print("\n")
    runagain()


def create_Table():
    c.execute("""create table if not exists student (
                Id integer primary key not null,
                First_Name text not null,
                Last_Name text not null ,
                DOB text ,
                Phone_Number integer)""")
    print("table created")
    con.commit()


def listStudent():
    data = c.execute('SELECT * FROM STUDENT ')
    for row in data:
        print(row)
    con.commit()
    print("\n")
    runagain()


def searchstudent():
    f_name = input("Enter The First Name OF The Student To Search = ")
    data = c.execute("select * from student where First_name = '{}'".format(f_name))
    for row in data:
        print("Roll No =", row[0])
        print("First Name =", row[1])
        print("Last Name =", row[2])
        print("DOB =", row[3])
        print("Phone Number =", row[4])

    con.commit()
    print("\n")
    runagain()


def deletestudent():
    f_name = input("Enter The First Name : ")
    l_name = input("Enter The Last Name : ")
    c.execute("delete from student where First_name = '{}' and Last_name = '{}'".format(f_name, l_name))
    con.commit()
    print(" Student deleted")
    print("\n")
    runagain()


def runagain():
    r = input("Do You Want To Run Again (y/n) = ")
    if r == 'y':
        managestudent()
    else:
        quit()


def managestudent():
    print(" 1. Add Student \n 2. Search Student \n 3. Delete Student \n 4. List Of Student "
          "Details ")
    ch = int(input("Enter Your Choice = "))
    if ch == 1:
        addStudent()
    elif ch == 2:
        searchstudent()
    elif ch == 3:
        deletestudent()
    elif ch == 4:
        listStudent()
    else:
        print("******invalid Choice******")
        print("\n")
        runagain()


if __name__ == "__main__":
    con = sqlite3.connect("studentinfo.db")
    c = con.cursor()
    create_Table()
    managestudent()
    con.close()
