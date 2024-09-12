## Problem Statement: Banking System Simulation
'''
You are developing a banking system simulation to manage customer accounts and transactions. The system should support basic banking operations such as creating accounts, depositing and withdrawing money, transferring funds between accounts, and viewing account details. Additionally, the system should save account data to a file and load it upon startup.

### Requirements

### Account Class:

**Variables:**
account_number (string): Unique identifier for the account.
account_holder (string): Name of the account holder.
balance (float): Current balance of the account.

**Methods:**
deposit(amount): Adds the specified amount to the account balance.
withdraw(amount): Subtracts the specified amount from the account balance if sufficient funds are available; otherwise, display an error message.
transfer(amount, target_account): Transfers the specified amount to another account if sufficient funds are available; otherwise, display an error message.
display_details(): Prints the account details.


'''

class Account: 

    
    # def __init__(self, account_number, account_holder):
    def __init__(self, account_no, name, ph_no, balance ):
         
            self.account_number = account_no       
            self.name = name
            self.ph_no = ph_no
            self.balance = balance
            
    def display_details(self):
        return self.account_number, self.name, self.balance,self.ph_no
    
    
    def deposite(self, amount):
        self.balance = self. balance + amount
        
        return self.balance


      
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return  self.balance
            
            
# account_chitra = Account("301148", "Chitra")
# account_Keya = Account("301146", "Keya")

# print (account_chitra.account_holder)
# print (account_Keya.account_holder)

# print(account_chitra. display_details())
# print(account_Keya. display_details())

# print(f"The amount after depositing money: {account_chitra.deposite(int(input('Enter the amount to deposit: ')))}")



# print(f"The amount after withdrawing money: {account_chitra.withdraw(int(input('Enter the amount to be withdrawn: ')))}")

            
# print(account_chitra. display_details())
# print(account_Keya. display_details())
           
            
            
#             **Methods:**
# deposit(amount): Adds the specified amount to the account balance.
# withdraw(amount): Subtracts the specified amount from the account balance if sufficient funds are available; otherwise, display an error message.
# transfer(amount, target_account): Transfers the specified amount to another account if sufficient funds are available; otherwise, display an error message.
# display_details(): Prints the account details.
  
# def deposite(self, amount):
#        amount = int(input(f"the amnount deposited:"))
#        self. balance += amount
#        return amount
    
# def withdraw (self, amount):
#     if amount == 200:
#        amountWithdrawn = int(input(f"the amnount deposited:"))
#        self.balance -= amountWithdrawn
#        return amountWithdrawn
   
# def transfer(self, amount, target_account):
#     amount = int(input(f"the amount I want to transfer : "))
#     if amount>= 300.00:
#         AfterTransfer = current_balance - TransferredAmount
#         return AfterTransfer
    
# def display_details(self):
#     return self.account_number, self.account_holder, self.balance
    
    
    



    

    
    
    
      
      

            

    
    