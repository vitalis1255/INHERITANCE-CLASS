class Account:#Base class.
    #Read the account balance.
    def __init__(self, filepath):#create a contructor method with required argument.
        self.filepath = filepath
        with open(filepath, "r",encoding="utf-8") as file:
            self.balance = int(file.read())#self.balance is an instance variable.

    def withdraw(self, amt):
        self.balance = self.balance - amt

    def deposit(self, amt):
        self.balance = self.balance + amt
    
    #To overwrite the current balance in the balance.txt
    def commit(self):
        with open(self.filepath, 'w', encoding='utf-8') as file:
            file.write(str(self.balance))

#checking_account is the inheritance class,inheriting the base class Account.
class checking_account(Account):#base class Account will be in the bracket of checking_account.
    def __init__(self,filepath, fee_charged):#init method of the checking account class.
        Account.__init__(self, filepath)#init method of the account class
        self.fee_charged = fee_charged

    def transfer(self, amt):
        self.balance = self.balance - amt - self.fee_charged


checking = checking_account("account\\balance.txt",1)
checking.transfer(900)

checking.commit()
print(checking.balance)
