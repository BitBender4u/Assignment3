class BankAccount:
    def __init__(self, myBalance=0):
        self.__balance = myBalance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} successfully. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew  {amount} successfully. New balance: {self.__balance}")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

# Example
account = BankAccount(100)  

account.deposit(209500)  
account.withdraw(2000) 
account.withdraw(11500) 