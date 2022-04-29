def header():
    print('''------------------------ \nGovernment Polytechnic \n------------------------''')


def add():
    print("Add New Student")
    name = input("Enter Name :- ")
    age = int(input("Enter Age :- "))
    mob_number = int(input("Enter mob_number :-"))
    print("New Student is added")


def delete():
    name = input("Enter Name of Student:- ")
    print("Delete Student")


def search():
    name = input("Enter Name of Student:- ")
    print("It should display student Name",)


def choice():
    print(''' 1.Add New Student\n 2.Delete Student\n 3.Search Student''')
    choice = int(input("Enter You choice :- "))
    return choice

if __name__ == "__main__":
    ch = choice()
    if ch == 1:
        header()
        add()
    elif ch == 2:
        header()
        delete()
    elif ch == 3:
        header()
        search()
    else:
        print("Invalid Choice")

