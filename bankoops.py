from random import randint

class CurrentAcc:
    def validate(self, name, accnumber):
        self.name = name
        self.accnumber = accnumber
    def balance(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        self.amount = amount
    def deposit(self, amount):
        self.deposit = amount
    
    
class CreateNewAcc:
    def name(self, name):
        self.name = name
    def initial_deposit(self, deposit):
        self.deposit = deposit
    def account_number(self, number):
        return self.number =randint(10000, 99999) 
        
    
newacc = CreateNewAcc()
curracc = CreateNewAcc()

print("Do you have an account with bank? Y/N:")
uc = input()
if uc == "Y":
    
    
else:
    name = newacc.name()
    initial_deposit = newacc.initial_deposit()
    saving_accnumber = newacc.account_number()
    
    