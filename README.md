# Python Budget Tracker

A Python project built as part of the FreeCodeCamp **Scientific Computing with Python** certification.  
This program models budget categories, tracks deposits and withdrawals, and generates a spend chart that visualises how money is allocated across categories.

## 📌 Features

- Create budget categories (e.g., Food, Business, Entertainment)
- Record deposits, withdrawals, and transfers between categories
- Automatically calculate balances
- Validate transactions with fund checks
- Generate a vertical ASCII spend chart showing percentage spent per category
- Clean, readable object‑oriented design

---

## 🧩 How It Works

The project includes:

### **`Category` class**
Handles:
- Deposits  
- Withdrawals  
- Transfers  
- Balance tracking  
- Ledger formatting  

### **`create_spend_chart(categories)`**
Generates a text‑based bar chart showing the percentage of spending per category, rounded down to the nearest 10%.

---

## ▶️ Example Usage

To test the project, you can create a separate file (e.g., `test.py`) and run:

```python
from budget import Category, create_spend_chart

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
food.withdraw(105.55, "groceries")
food.withdraw(33.40, "snacks")

entertainment.deposit(900, "deposit")
entertainment.withdraw(33.40, "movies")

business.deposit(900, "deposit")
business.withdraw(10.99, "paper")

print(create_spend_chart([business, food, entertainment]))
