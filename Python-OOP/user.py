class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.expenses = []
        
    def add_expense(self, expense):
        self.expenses.append(expense)
        
    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)
    
    def __str__(self):
        return f"User(id={self.id}, name={self.name}, total_expenses={self.get_total_expenses})"
    