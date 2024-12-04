# Adds an amount and category to the Expense Tracker
# amount: the amount to be added to the expense list
# category: the category which the amount belongs to
# expenses: the list of all expenses
def add_expense(expenses, amount, category):
    if expenses.get(category):
        expenses[category].append(amount)
    else:
        expenses[category] = [amount]

# Prints out the list of expenses
# expenses: the list of all expenses
def print_expenses(expenses):
    for expense in expenses:
        output = f'{expense}:'
        for amount in expenses[expense]:
            output += f' ${amount},'
        print(output[:-1])

# Shows the total expenses
# expenses: the list of all expenses
def total_expenses(expenses):
    return sum(map(lambda category: sum(map(lambda amount: amount, expenses[category])), expenses))

# Returns only the expenses for a specified category
# category: the specific category to get expenses from
# expenses: the list of all expenses
def filter_expenses_by_category(expenses, category):
    return {category: expenses[category]}
    
# Provides main interface for user to interact with their Expense Tracker
def main():
    expenses = {}
    while True:
        # Options for user to interact with the Expense Tracker
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        # choice: selection made by the user from the options provided, if their input is none of the prior provided, they will be reprompted to make a selection
        choice = input('Enter your choice: ')
        match choice:
            case '1':
                amount = float(input('Enter amount: '))
                category = input('Enter category: ')
                add_expense(expenses, amount, category)
            case '2':
                print('\nAll Expenses:')
                print_expenses(expenses)
            case '3':
                print('\nTotal Expenses: ', total_expenses(expenses))
            case '4':
                # category: specific category entered by user to filter the list of expenses
                category = input('Enter category to filter: ')
                expenses_from_category = filter_expenses_by_category(expenses, category)
                print(f'\nExpenses for {category}:')
                print_expenses(expenses_from_category)
            case '5':
                print('Exiting the program.')
                return
            case _:
                continue    

main()