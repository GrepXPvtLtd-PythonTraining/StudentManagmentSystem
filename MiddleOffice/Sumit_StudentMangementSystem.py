import sqlite3

def NewAdmission():
    co.execute("drop table if exists studentdetail ")
    co.execute("""create table studentdetail(
                  Sequence integer,
                  Name text,
                  Email text,
                  DOB text,
                  Phone_nu integer,
                  Address text
                  )""")
    con.commit()




def AddStudent():
    sequence = int(input("Enter the sequence no. of student :- "))
    Name = input("Enter the Name of Students :- ")
    Email = input("Enter the Email :- ")
    DOB = input("Enter the DOB of Student :- ")
    Phone_nu = int(input("Enter mob_no of student :-"))
    Address = input("Enter the address of student :- ")
    co.execute(
        "insert into studentdetail values({},'{}','{}','{}',{},'{}')".format(sequence, Name, Email, DOB, Phone_nu,
                                                                             Address))
    con.commit()
    print("Student added")
    SearchStudent()



def DeleteStudent():
    Name = input("Enter the Name of Students :- ")
    co.execute("delete from studentdetail where name = '{}'".format(Name))
    print("Student is delete")
    con.commit()




def SearchStudent():
    Name = input("Enter the Name of Students :- ")
    co.execute("select * from studentdetail where name = '{}'".format(Name))
    print(co.fetchall())
    con.commit()



def Choise():
    print("1. Add student \n 2. Delete Student \n 3. Search student")
    Choise = int(input("Enter your choise :- "))
    if Choise == 1:
        AddStudent()
    elif Choise == 2:
        DeleteStudent()
    elif Choise == 3:
        SearchStudent()
    else:
        print("Enter valid choise")




if __name__ == "__main__":
    con = sqlite3.connect('studentdetail.db')
    co = con.cursor()
    NewAdmission()
    Choise()
    con.close()
