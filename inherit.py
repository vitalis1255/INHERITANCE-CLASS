class Account:#Base class.
    #Read the account balance.
    def __init__(self, filepath):#create a contructor method with required argument.
        self.filepath = filepath #instance variable
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
    #Create Doc strings, which is usually created after class name
    """
    INHERITANCE CLASS
    """
    #create class variable, which is declared outside the init method which are shared by all the instances of the class.
    type = "checking"
    def __init__(self,filepath, fee_charged):#init method of the checking account class. init method is a constructor method
        Account.__init__(self, filepath)#init method of the account class
        self.fee_charged = fee_charged

    def transfer(self, amt):#transfer is a class method
        self.balance = self.balance - amt - self.fee_charged


checking = checking_account("account\\balance.txt",1) #checking is the object that stores the inheritance class arguments
#It is inheritance classto call not base class
#Inheritance is when you create sub-class out of a base class
checking = checking_account("account\\izu.txt",1)#checking is the object instaniation of the class
checking.transfer(900)#How to call a class method
checking.commit()
print(checking.balance)
print(checking.type)
print(checking.__doc__)

#Data members are instance variables and class variables such as type(class variable) and self.fee_charged=fee_charged as instance variable.
#instances of the class below:
checking = checking_account("account\\vitalis.txt",1)#checking is the object instaniation of the class
checking.transfer(900)
checking.commit()
print(checking.balance)
print(checking.type)
