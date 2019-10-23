class Account(object):
    
    def __init__(self, name: str, opening_balance: int = 0):
        self.name = name
        self._balance = opening_balance
        print(f"Account created for {self.name}, with amount of {self._balance}$.")
        
    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._balance += amount
            print(f"Deposited {amount / 100}$.")
        return self._balance / 100
    
    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn {amount / 100}$.")
            return amount / 100
        else:
            print(f"Amount must be greater than zero and more than account balance.")
            return 0.0
        
    def show_balance(self):
        print(f"Balance on account owner {self.name} is {self._balance / 100}$.")
        

if __name__ == "__main__":
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()