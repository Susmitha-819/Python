class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self._account_number="1234567890"
        self._balance=balance

    def get_balance(self):
        return self._balance

    def deposit(self,amount):
        if amount > 0:
            self._balance+=amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "invalid amount"

    def withdraw(self,amount):
        if 0< amount <=self._balance:
            self._balance-= amount                                                                                    
            return f"withdraw ${amount}. New ba;ance:${self._balance}"
        return "insufficient funds or invalid amount"
    

account=BankAccount("john doe",10000)

print(f"Account holder:{account.account_holder}")
print(f"Account number:{account._account_number}")
print(f"Balance:${account.get_balance()}")
try:
    print(account._balance)
except AttributeError as e:
    print(f"Error:{e}")

  
print(account.deposit(500))
print(account.withdraw(2000))
