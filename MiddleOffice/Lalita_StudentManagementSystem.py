import sqlite3


def CreateTable():
    c.execute("""create table StudentData(
                     First_Name TEXT,
                     Middle_name TEXT,
                     Last_Name TEXT,
                     age INTEGER,
                     Phone_Number INTEGER
                     )""")

    conn.commit()


def NewStudent():
    First_name = input(" enter student name : ")
    Middle_name = input(" enter middle name : ")
    Last_name = input(" enter last name : ")
    age = int(input(" enter  student age : "))
    Phone_number = int(input(" enter phone number : "))
    c.execute("INSERT INTO StudentData VALUES('{}','{}','{}',{},{})".format(First_name, Middle_name, Last_name,age,Phone_number))
    conn.commit()
    print(" student is added ")
    SearchStudent()



def DeleteStudent():
    First_name = input("enter the first name : ")
    Last_name = input("enter the last name : ")
    c.execute("delete from StudenData where First_name = '{}', Last_name = '{}'".format(First_name, Middle_name))
    conn.commit()


def SearchStudent():
    First_name = input("enter the first name for searched : ")
    c.execute("select * from StudentData where First_name = '{}'".format(First_name))
    print(c.fetchall())
    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect('StudentData.db')
    c = conn.cursor()
    CreateTable()
    print("1. New student \n 2.delete Student \n 3.search Student ")
    choice = int(input(" enter your choice : "))
    if choice == 1:
        NewStudent()

    elif choice == 2:
        DeleteStudent()
    elif choice == 3:
        SearchStudent()
    else:
        print(" invalid choice : ")
    conn.close()