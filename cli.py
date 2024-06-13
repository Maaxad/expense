from lib.expense import Expense
from lib.category import Category
from lib.user import User

def main():
    print("WELCOME TO EXPENSE TRACKER")
    print("What would you like to do?")
    print("1. Add Expense")
    print("2. Add Category")
    print("3. Add User")
    print("4. View Expenses")
    print("5. View Categories")
    print("6. View Users")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Add Expense")
        description = input("Enter description: ")
        amount = input("Enter amount: ")
        date = input("Enter date: ")
        category_id = input("Enter category_id: ")
        user_id = input("Enter user_id: ")
        expense = Expense(description, amount, date, category_id, user_id)
        expense.create()
        print(expense)

    elif choice == 2:
        print("Add Category")
        name = input("Enter name: ")
        category = Category(name)
        category.create()
        print(category)

    elif choice == 3:
        print("Add User")
        name = input("Enter name: ")
        password = input("Enter password: ")
        user = User(name, password)
        user.create()
        print(user)
        
    elif choice == 4:
        print("View Expenses")
        # Add logic for viewing expenses
        expenses = Expense.get_all()
        for expense in expenses:
            print(expense)
        
    elif choice == 5:
        print("View Categories")
        # Add logic for viewing categories
        categories = Category.get_all()
        for category in categories:
            print(category)

    elif choice == 6:
        print("View Users")
        # Add logic for viewing users
        users = User.get_all()
        for user in users:
            print(user)

    elif choice == 7:
        print("Exiting...")
        return  # Exit the program

    else:
        print("Invalid choice")

    # Call main again to keep the program running until the user chooses to exit
    main()

if __name__ == "__main__":
    main()
