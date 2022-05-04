import sqlite3


def newadmission():
    cur.execute("""create table if not exists studentinfo(
                     sequence INTEGER,
                     First_Name TEXT,
                     Last_Name TEXT,
                     Date_of_Birth INTEGER,
                     Phone_Number INTEGER
                     )""")
    conn.commit()


def addstudent():
    sequence = int(input(" enter sequence : "))
    First_name = input(" enter student name : ")
    Last_name = input(" enter your last name : ")
    Date_of_birth = int(input(" enter  student date of birth : "))
    Phone_number = int(input(" enter phone number : "))
    cur.execute(
        "insert into studentinfo values({},'{}','{}',{},{})".format(sequence, First_name, Last_name, Date_of_birth,
                                                                    Phone_number))
    conn.commit()
    print(" student added ")


def deletestudent():
    f_name = input("enter the first name of student to be deleted : ")
    l_name = input("enter the last name of student to be deleted : ")
    cur.execute("delete from studentinfo where First_name = '{}', Last_name = '{}'".format(f_name, l_name))
    conn.commit()


def searchstudent():
    f_name = input("enter the first name of student to be searched : ")
    cur.execute("select * from studentinfo where First_name = '{}'".format(f_name))
    print(cur.fetchall())
    conn.commit()


def liststudent():
    conn.execute("select * from studentinfo ")
    print(cur.fetchall())
    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect('studentinfo.db')
    cur = conn.cursor()
    newadmission()
    print("1.addstudent \n 2.delete \n 3.search \n 4.liststudent ")
    choice = int(input(" enter your choice : "))
    if choice == 1:
        addstudent()

    elif choice == 2:
        deletestudent()
    elif choice == 3:
        searchstudent()
    elif choice == 4:
        liststudent()
    else:
        print(" invalid choice !")
    conn.close()
