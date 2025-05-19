#TASK 1: OPERATIONS ON TUPLE

fruits=tuple(input(f"enter a fruit {i+1}: ")for i in range (5))
print(f"fruits in tuple:{fruits}")

search_fruit=input("\n Enter a fruit name to search: ")
if search_fruit in fruits:
    print(f"{fruits} is in the tuple.")
else:
    print(f"fruits is not in the tuple.")

print("\noccurence of fruit:")
for fruit in set (fruits):
    count=fruits.count(fruit)
    print(f"{fruit}={count}")

#TASK 2: STUDENT DATA MANAGEMENT USING DICTIONARY
students = {}

def add_student():
    nim = input("Enter NIM: ")
    if nim in students:
        print("Student with this NIM already exists!")
        return
    name = input("Enter Name: ")
    major = input("Enter Major: ")
    try:
        gpa = float(input("Enter GPA: "))
    except ValueError:
        print("Invalid GPA. Please enter a numeric value.")
        return
    students[nim] = {"Name": name, "Major": major, "GPA": gpa}
    print("Student added successfully.\n")

def display_students():
    if not students:
        print("No student data available.\n")
        return
    print("\nAll Student Data:")
    for nim, data in students.items():
        print(f"NIM: {nim}")
        print(f"  Name : {data['Name']}")
        print(f"  Major: {data['Major']}")
        print(f"  GPA  : {data['GPA']}\n")

def search_student():
    nim = input("Enter NIM to search: ")
    if nim in students:
        data = students[nim]
        print(f"Student Found:\n  Name: {data['Name']}\n  Major: {data['Major']}\n  GPA: {data['GPA']}\n")
    else:
        print("Student not found.\n")

def delete_student():
    nim = input("Enter NIM to delete: ")
    if nim in students:
        del students[nim]
        print("Student data deleted.\n")
    else:
        print("Student not found.\n")

def menu():
    while True:
        print("=== Student Data Management ===")
        print("1. Add New Student")
        print("2. Display All Students")
        print("3. Search Student by NIM")
        print("4. Delete Student by NIM")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

menu()


# TASK 3: INVENTORY MANAGEMENT SYSTEM
inventory = {}

def add_item():
    name = input("Enter Item Name: ")
    if name in inventory:
        print("Item already exists in inventory.")
        return
    try:
        price = float(input("Enter Item Price: "))
        stock = int(input("Enter Item Stock Quantity: "))
        inventory[name] = (price, stock)
        print("Item added successfully!\n")
    except ValueError:
        print("Invalid input. Price must be a number and stock must be an integer.\n")

def display_items():
    if not inventory:
        print("No items in inventory.\n")
        return
    print("\n{:<20} {:<10} {:<10}".format("Item Name", "Price", "Stock"))
    print("-" * 40)
    for name, (price, stock) in inventory.items():
        print("{:<20} {:<10.2f} {:<10}".format(name, price, stock))
    print()

def search_item():
    name = input("Enter Item Name to Search: ")
    if name in inventory:
        price, stock = inventory[name]
        print(f"Item Found: {name}, Price: {price}, Stock: {stock}\n")
    else:
        print("Item not found in inventory.\n")

def update_stock():
    name = input("Enter Item Name to Update Stock: ")
    if name in inventory:
        try:
            new_stock = int(input("Enter New Stock Quantity: "))
            price = inventory[name][0]
            inventory[name] = (price, new_stock)
            print("Stock updated successfully!\n")
        except ValueError:
            print("Invalid stock input. Must be an integer.\n")
    else:
        print("Item not found in inventory.\n")

def delete_item():
    name = input("Enter Item Name to Delete: ")
    if name in inventory:
        del inventory[name]
        print("Item deleted successfully!\n")
    else:
        print("Item not found in inventory.\n")

def data_analysis():
    if not inventory:
        print("No items to analyze.\n")
        return

    highest = max(inventory.items(), key=lambda x: x[1][0])
    lowest = min(inventory.items(), key=lambda x: x[1][0])

    total_value = sum(price * stock for price, stock in inventory.values())

    print(f"Most Expensive Item : {highest[0]} (Price: {highest[1][0]})")
    print(f"Least Expensive Item: {lowest[0]} (Price: {lowest[1][0]})")
    print(f"Total Stock Value   : {total_value:.2f}\n")

def menu():
    while True:
        print("=== Inventory Management System ===")
        print("1. Add New Item")
        print("2. Display All Items")
        print("3. Search for an Item")
        print("4. Update Item Stock")
        print("5. Delete Item")
        print("6. Data Analysis")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            display_items()
        elif choice == '3':
            search_item()
        elif choice == '4':
            update_stock()
        elif choice == '5':
            delete_item()
        elif choice == '6':
            data_analysis()
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 7.\n")

menu()




