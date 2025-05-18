class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = f"{item['description'][:23]:<23}"
            amount = f"{item['amount']:.2f}"
            items += f"{description}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    # Calculate total spent and percentages
    total_spent = sum(
        -sum(item["amount"] for item in category.ledger if item["amount"] < 0)
        for category in categories
    )
    percentages = [
        (sum(-item["amount"] for item in category.ledger if item["amount"] < 0) / total_spent) * 100
        for category in categories
    ]

    # Build the chart
    chart = title
    for i in range(100, -1, -10):
        chart += f"{i:>3}| " + "".join("o  " if percent >= i else "   " for percent in percentages) + "\n"

    # Add bottom border
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Prepare category names vertically
    max_len = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_len) for category in categories]
    for i in range(max_len):
        chart += "     " + "  ".join(name[i] for name in names) + "  \n"

    return chart.rstrip("\n")


# Example usage
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
clothing.deposit(500, 'initial deposit')
clothing.withdraw(50, 'jeans')

entertainment = Category('Entertainment')
entertainment.deposit(300, 'initial deposit')
entertainment.withdraw(30, 'movie tickets')

food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing, entertainment]))
