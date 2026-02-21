# FreeCodeCamp Budget App

This project is part of the FreeCodeCamp Scientific Computing with Python certification.  
It implements a Category class and a spend chart generator that visualizes spending across categories.

## Skills demonstrated
- Python classes and OOP
- Data structures (lists, dictionaries)
- String formatting and ASCII chart generation
- Debugging and passing strict automated tests

## Files
- `budget.py` — full project code

## Testing
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
