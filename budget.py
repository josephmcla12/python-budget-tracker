class Category:
    def __init__(self, name):
        # Store the category name and initialize an empty ledger
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        # Add a deposit entry to the ledger
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # Withdraw only if sufficient funds exist
        if not self.check_funds(amount):
            return False
        # Store withdrawal as a negative amount
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        # Calculate the current balance by summing all ledger amounts
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def check_funds(self, amount):
        # Return True if enough balance exists, otherwise False
        return amount <= self.get_balance()

    def transfer(self, amount, category):
        # Transfer funds between categories if possible
        if not self.withdraw(amount, "Transfer to " + category.name):
            return False
        category.deposit(amount, "Transfer from " + self.name)
        return True

    def __str__(self):
        # Format the category ledger for printing
        title = self.name.center(30, "*")
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]  # Limit description to 23 chars
            amt = f"{entry['amount']:.2f}"    # Format amount to 2 decimals
            items += f"{desc:<23}{amt:>7}\n"  # Align description + amount
        total = f"Total: {self.get_balance():.2f}"
        return title + "\n" + items + total


def create_spend_chart(categories):
    # Calculate total spent in each category
    spent = []
    for category in categories:
        total = 0
        for entry in category.ledger:
            if entry["amount"] < 0:  # Negative amounts = spending
                total += -entry["amount"]
        spent.append(total)

    total_spent = sum(spent)

    # Convert spending to percentages rounded down to nearest 10
    percentages = []
    for amount in spent:
        percent = int((amount / total_spent) * 100)
        percent -= percent % 10
        percentages.append(percent)

    # Chart header
    chart = "Percentage spent by category\n"

    # Build the vertical percentage bars (100 → 0)
    for level in range(100, -1, -10):
        line = f"{level:>3}|"  # Right-align the percentage labels
        for percent in percentages:
            # Add "o" if category meets this level, else blank space
            if percent >= level:
                line += " o "
            else:
                line += "   "
        chart += line + " \n"  # Space + newline required by FCC tests

    # Add horizontal divider
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Prepare category names for vertical printing
    names = [category.name for category in categories]
    max_len = max(len(name) for name in names)
    padded = [name.ljust(max_len) for name in names]  # Pad names equally

    # Print names vertically
    for i in range(max_len):
        line = "     "  # Indent under the bars
        for name in padded:
            line += name[i] + "  "  # Add each letter + spacing
        if i < max_len - 1:
            chart += line + "\n"
        else:
            chart += line  # No newline at the end

    return chart
