import datetime
import pytz

class Account:
    
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for " + self.name)
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))
            
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
            self.show_balance()
        else:
            print("Error in withdraw!")
            self.show_balance()
            
    def show_balance(self):
        print(f"Balance is {self.balance}$.")
        
    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdraw"
                amount *= -1
            print(f"Amount {amount} was {tran_type} in UTC time {date} and in local time {date.astimezone()}")
        
customer = Account("Customer", 0)
customer.deposit(1000)
customer.withdraw(500)
customer.show_transactions()
