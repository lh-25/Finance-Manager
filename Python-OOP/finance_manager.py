class FinanceManager:
    def __init__(self):
        self.users = {}
    
    def add_user(self,user):
        self.users[user.id] = user
        
    def get_user(self, user_id):
        return self.users.get(user_id)
    
    def add_expense(self, user_id, expense):
        user = self.get_user(user_id)
        if user:
            user.add_expense(expense)
        else:
            print("User not found")
    
    def get_user_total_expenses(self, user_id):
        user = self.get_user(user_id)
        if user:
            return user.get_total_expenses()
        else:
            print("User not found")
            return 0