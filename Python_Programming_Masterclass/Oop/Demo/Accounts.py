class Account:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.show_balance()
        else:
            print("Error in withdraw!")
            self.show_balance()
            
    def show_balance(self):
        print(f"Balance is {self.balance}.")
        
        
customer1 = Account("Customer 1", 0)
customer1.deposit(1000)
customer1.withdraw(500)
customer1.withdraw(500000)
