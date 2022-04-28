import os


def createFile():
    file = open("Studentinfo.txt", "a+")
    return file


def addToFile(file, studentId, name, age, phoneNumber):
    file.write("{}|{}|{}|{}\n".format(studentId, name, age, phoneNumber))
    file.flush()
    file.seek(0)
    file.close()


def readFile():
    file = open("Studentinfo.txt")
    print(file.read())
    file.close()


def checkTheFile(f, studentname):
    f = open("Studentinfo.txt", "r")
    data = " "
    data = f.readlines()
    for line in data:
        splitData = line.split("|")
        rollNum = splitData[0]
        name = splitData[1]
        age = splitData[2]
        phoneNumber = splitData[3]
        if studentname == name:
            print("{}|{}|{}|{}".format(rollNum, name, age, phoneNumber))


def checkIfStudentExit(f, studentname):
    f = open("Studentinfo.txt", "r")
    data = " "
    data = f.readlines()
    for line in data:
        splitData = line.split("|")
        rollNum = splitData[0]
        name = splitData[1]
        age = splitData[2]
        phoneNumber = splitData[3]
        if studentname == name:
            print("\n{}|{}|{}|{}".format(rollNum, name, age, phoneNumber))
            return True


def updateStudentInfo():
    fh_r = open("Studentinfo.txt", "r")
    fh_w = open("temp.txt", "w")
    student_name = input("Enter The Student Name to Update = ")
    data = " "
    while data:
        data = fh_r.readline()
        l = data.split("|")
        for i in range(0, len(l) - (len(l) - 1)):
            roll_no = l[0]
            if len(data) > 0:
                if l[1] == student_name:
                    name = input("Enter New Name = ")
                    age = int(input("Enter New Age = "))
                    ph = int(input("Enter New Phone NUmber = "))
                    fh_w.write("{}|{}|{}|{}\n".format(roll_no, name, age, ph))
                else:
                    fh_w.write(data)
    fh_w.close()
    fh_r.close()
    os.remove("Studentinfo.txt")
    os.rename("temp.txt", "Studentinfo.txt")


def delete():
    fh_r = open("Studentinfo.txt", "r")
    fh_w = open("temp.txt", "w")
    student_name = input("Enter The Student Name to Delete The Record = ")
    data = " "
    while data:
        data = fh_r.readline()
        l = data.split("|")
        for i in range(0, len(l) - (len(l) - 1)):
            roll_no = l[0]
            if len(data) > 0:
                if l[1] != student_name:
                    fh_w.write(data)

    fh_w.close()
    fh_r.close()
    os.remove("Studentinfo.txt")
    os.rename("temp.txt", "Studentinfo.txt")


def choice():
    print("******** Student Management System ********")
    print(
        ''' 1.Add New Student\n 2.Delete Student\n 3.Search Student \n 4.List Student \n 5.Update Student Information 
        \n''')
    choice = int(input("       Enter You choice :- "))
    return choice


def add(file):
    print("*********Add student information********* ")
    f = open("Studentinfo.txt", "r")
    studentId = len(f.readlines()) + 1
    name = input("Enter Student Name = ")
    age = int(input("Enter Age = "))
    phoneNumber = int(input("Enter Phone Number = "))
    check = checkIfStudentExit(file, name)
    if check is True:
        print("student already exist ")
        return False
    else:
        addToFile(file, studentId, name, age, phoneNumber)


if __name__ == '__main__':
    f = createFile()
    ch = choice()
    if ch == 1:
        result = add(f)
        if result is False:
            pass
        else:
            print("\n")
            print("----New Student added-----")
            readFile()
    elif ch == 2:
        f.close()
        print("\n")
        readFile()
        delete()
        print("\n")
        print("File After Deletion")
        readFile()
    elif ch == 3:
        Name = input("Enter the Name You Want To Search = ")
        checkTheFile(f, Name)
    elif ch == 4:
        readFile()
    elif ch == 5:
        readFile()
        f.close()
        updateStudentInfo()
        print("\n")
        print("File After Update")
    else:
        print("Enter A Valid Option")