import sqlite3



def AddStudent():
    StudentId = int(input("Enter The Student Id : "))
    First_Name = input("Enter First Name : ")
    Last_Name = input("Enter Last Name : ")
    DOB = input("Enter Date Of Birth as dd-mm-yyyy : ")
    Phone_no = int(input("Enter Phone Number : "))
    Address = input("Enter Address : ")
    c.execute("INSERT INTO student VALUES({},'{}','{}',{},{},'{}')".format(StudentId, First_Name, Last_Name, DOB, Phone_no, Address))
    conn.commit()
    print ("New Student Add")

def createTable():
    c.execute("""create table student (
                    StudentId integer not null,
                    First_Name text not null,
                    Last_Name text not null,
                    DOB text not null,
                    Phone_No integer not null,
                    Address text not null )""")
    conn.commit()

def Searchstudent():
    First_Name = input("Enter The student Name To Search = ")
    c.execute("select * from student where First_Name = '?'")
    print(c.fetchall())
    conn.commit()

def DeleteStudent():
    First_Name = input("Enter The First Name : ")
    Last_Name = input("Enter The Last Name : ")
    c.execute("delete from student where First_Name = '?' and Last_Name = '?'")
    print(" Student deleted")
    conn.commit()


if __name__== "__main__":
    conn = sqlite3.connect("pythondb.db")
    c=conn.cursor()
    createTable()
    print("1. Add student\n 2. Search student\n 3. Delete student")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        AddStudent()
    elif ch == 2:
        Searchstudent()
    elif ch == 3:
        DeleteStudent()
    else:
        print("Invalid choice")
    conn.close()
