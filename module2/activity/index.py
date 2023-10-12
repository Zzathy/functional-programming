expenses = [
    {"date": "2023-07-25", "description": "Lunch", "amount": 50000},
    {"date": "2023-07-25", "description": "Transportation", "amount": 25000},
    {"date": "2023-07-26", "description": "Shopping", "amount": 100000},
]

# TODO 1 make add_expense function
def add_expense(date, description, amount, expenses):
    expense = {"date": date, "description": description, "amount": amount}
    return expenses.append(expense)

# TODO 2 make calculate_total_expenses function
calculate_total_expenses = lambda inputs : sum(input["amount"] for input in inputs)

# TODO 3 make get_expenses_by_date function
get_expenses_by_date = lambda date, expenses : [data for data in expenses if data["date"] == date]

# TODO 4 make generate_expenses_report function
generate_expenses_report = lambda expenses : (expense for expense in expenses) 
    
# TODO 5 make sure all function that all have is pure function
# if not, moficate it

def add_expense_interactively(expenses):
    date = input("Input expenses date (YYYY-MM-DD): ")
    description = input("Input description expenses: ")
    amount = int(input("Input amount expenses: "))
    new_expenses = add_expense(date, description, amount, expenses)
    print("Expenses successfully added")
    return new_expenses

def view_expenses_by_date(expenses):
    date = input("Input date (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date(date, expenses)
    print(f"\nExpenses on date {date}: ")
    for expense in expenses_on_date:
        print(f"{expense['description']} - Rp {expense['amount']}")

def view_expenses_report(expenses):
    print("\nReport Daily Expenses: ")
    expenses_report = generate_expenses_report(expenses)
    for entry in expenses_report:
        print(entry)

def display_menu():
    print("\n=== Register Daily Expenses App")
    print("1. Add Expenses")
    print("2. Amount Daily Expenses")
    print("3. Check/See/Look Expenses by Date")
    print("4. Check/See/Look Expenses Report by Date")
    print("5. Exit")

# TODO 6 Change this function to lambda
get_user_input = lambda command : int(input(command))

def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Choose menu (1/2/3/4/5): ")

        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nAmount Daily Expenses: Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            print("Thank you for using this app")
            break
        else:
            print("Choose is invalid")

if __name__ == "__main__":
    main()