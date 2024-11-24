import math

class Category:
    def __str__(self):
        title = self.name.center(30, "*") + '\n'
        items = ""
        for item in self.ledger:
            desc = item["description"]
            amount = "{:0.2f}".format(float(item["amount"]))
            if len(desc) > 23: desc = desc[0:23]
            if len(amount) > 7: amount = amount[0:7]
            items = items + desc + (30 - len(desc) - len(amount)) * " " + amount + '\n'

        return title + items + "Total: " + str(float(self.get_balance()))

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.deposit(0 - amount, description)
            return True
        return False
    
    def transfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {category.name}'):
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False


    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def check_funds(self, amount):
        return self.get_balance() >= amount

def create_spend_chart(categories):
    totals = {}
    total = 0
    chart = "Percentage spent by category\n"
    for category in categories:
        totals[category.name] = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                totals[category.name] = totals[category.name] + entry["amount"]

    for k, v in totals.items():
        totals[k] = v * - 1
        total = total - v

    for k, v in totals.items():
        percentage = math.trunc((v / total * 100))
        totals[k] = percentage


    for i in range(100, -10, -10):
        chart = chart + str(i).rjust(3, " ") + "|"
        for k, v in totals.items():
            if v >= i:
                chart = chart + " o "
            else:
                chart = chart + "   "
        chart = chart + " \n"

    chart = chart + 4 * " " + (4 + 2 * len(totals)) * "-"
    i = 0
    while i < max(len(k) for k, v in totals.items()):
        chart = chart + "\n" + 4 * " "
        for key in totals:
            if len(key) <= i:
                chart = chart + "   "
            else:
                chart = chart + " " + key[i] + " "
        chart = chart + " "
        i = i + 1

    return chart
    
food = Category('Food')
food.deposit(100, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

print(food, '\n')
print(clothing, '\n')

print(create_spend_chart([food, clothing]))