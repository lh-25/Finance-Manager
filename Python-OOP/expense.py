class Expense:
    def __init__(self, id, description, amount, date):
        self.id = id
        self.description = description
        self.amount = amount
        self.date = date 
        
    def __str__(self):
        return f"Expense(id={self.id}, description={self.description}, amount={self.amount}, date={self.date})"
    