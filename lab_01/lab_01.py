students = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@gmail.com", "group": "KB-221"},
    {"name": "Emma", "phone": "0632345678", "email": "emma@gmail.com", "group": "KB-222"},
    {"name": "Jon", "phone": "0633456789", "email": "jon@gmail.com", "group": "KB-221"},
    {"name": "Zak", "phone": "0634567890", "email": "zak@gmail.com", "group": "KB-222"}
]

def printAllList():
    for elem in students:
        strForPrint = "Student name is " + elem["name"] + ", Phone is " + elem["phone"] + ", Email is " + elem["email"] + ", Group is " + elem["group"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position " + str(deletePosition))
        del students[deletePosition]
        print("Element has been deleted")
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    for item in students:
        if name == item["name"]:
            updatePosition = students.index(item)
            break
    if updatePosition == -1:
        print("Element was not found")
    else:
        del students[updatePosition]
        print("Enter new information for student:")
        new_name = input("Please enter student name: ")
        new_phone = input("Please enter student phone: ")
        new_email = input("Please enter student email: ")
        new_group = input("Please enter student group: ")
        updatedItem = {"name": new_name, "phone": new_phone, "email": new_email, "group": new_group}
        insertPosition = 0
        for item in students:
            if new_name > item["name"]:
                insertPosition += 1
            else:
                break
        students.insert(insertPosition, updatedItem)
        print("Element has been updated and list remained sorted")
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print, X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")

main()
