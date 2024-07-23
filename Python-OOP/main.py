from expense import Expense
from user import User
from finance_manager import FinanceManager

finance_manager = FinanceManager()

user1 = User(id="1", name="Jessica")
user2 = User(id="2", name="Tim")

finance_manager.add_user(user1)
finance_manager.add_user(user2)

expense1 = Expense(id ="1", description = "Groceries", amount= 50, date = "05-13-2024")
expense2 = Expense(id ="2", description = "Books", amount= 30, date = "05-25-2024")

finance_manager.add_expense(user_id = "1", expense = expense1)
finance_manager.add_expense(user_id = "2", expense = expense2)

print(f"Jessica's total expenses: ${finance_manager.get_user_total_expenses(user_id = '1')}")

print(f"Tim's total expenses: ${finance_manager.get_user_total_expenses(user_id = '2')}")
