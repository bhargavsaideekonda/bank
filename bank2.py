class BankAccount:
    def __init__(self,name):
        self.name=name
        self.balance=0
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Amount must be positive")
        else:
            self.balance+=amount
    def withdraw(self,amount):
        if amount>self.balance:
            raise ValueError("Insufficient funds")
        if amount<=0:
            raise ValueError("Amount must be positive")
        else:
            self.balance-=amount
    def report(self):
        return(f"{self.name} has Rs {self.balance}")
Asha=BankAccount("Asha")
Asha.deposit(1500)
Asha.withdraw(250)
try:
    Asha.withdraw(5000)
except ValueError as e:
    print(e)
try:
    Asha.withdraw(-500)
except ValueError as e:
    print(e)
try:
    Asha.deposit(-100)
except ValueError as e:
    print(e)
try:
    Asha.deposit(0)
except ValueError as e:
    print(e)
print(Asha.report())