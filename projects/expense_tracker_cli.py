import json
import os
from datetime import datetime

filename = "expenses.json"

class Expense_tracker:
    def __init__(self):
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []
    
    # def __init__(self):
    #     self.name = input("Enter the name of the expense: ")
    #     self.amount = float(input("Enter the amount of the expense: "))
    #     self.category = input("Enter the category of the expense: ")
        
    
    def save_expenses(self):
        with open(filename, "w") as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self):
        name = input("Enter the name of the expense: ")
        amount = float(input("Enter the amount of the expense: "))
        category = input("Enter the category of the expense: ")

       
        date = datetime.now().strftime("%d/%m/%Y")
        
        
        expense = {
            "name" : name,
            "amount" : amount,
            "category" : category,
            "date" : date
          }
        self.expenses.append(expense)

        self.save_expenses()
        print("Expenses added Successfully")

    def view_expenses(self):
        if not self.expenses:
            print("No expense yet")
            return
        
        
        for i, exp in enumerate(self.expenses, start=1):
            print(f"{i}. {exp['date']} | {exp['name']} | ₦{exp['amount']:.2f} | {exp['category']}")

    def view_by_category(self):
        cat = input("Enter the category: ")
        found = False

        for exp in self.expenses:
            if exp["category"].lower() == cat.lower():
                print(f"{exp['date']} | {exp['name']} | ${exp['amount']:.2f}")
                found = True

        if not found:
            print("No expense in this category")

    
    def total_spent(self):
        total = sum(exp["amount"] for exp in self.expenses)
        print(f"Total spent: ${total:.2f}")
    
    def delete_expense(self):
        self.view_expenses()

        if not self.expenses:
            return
        
        try:
            index = int(input("Enter the number to delete: "))  -1

            if 0 <= index < len(self.expenses):
                removed = self.expenses.pop(index)
                self.save_expenses()
                print(f"deleted {removed['name']}")

            else:
                print("Invalid number")
        
        except ValueError:
            print("Enter a valid number.")




    def menu(self):
        while True:
            print("\n==== Expense Tracker ====")
            print("1. Add Expense")
            print("2. View All")
            print("3. View By Category")
            print("4. Total Spent")
            print("5. Delete Expense")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_expense()

            elif choice == "2":
                self.view_expenses()

            elif choice == "3":
                self.view_by_category()

            elif choice == "4":
                self.total_spent()

            elif choice == "5":
                self.delete_expense()

            elif choice == "6":
                print("Goodbye 👋")
                break

            else:
                print("Invalid choice.")

def main():
    tracker = Expense_tracker()
    tracker.menu()



if __name__ == "__main__":
    main()