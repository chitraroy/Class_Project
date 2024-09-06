'''
#### Bank Class:
**Variables:**
accounts (dictionary): Stores accounts with account numbers as keys.

**Methods:**
create_account(account_number, account_holder): Creates a new account with the given account number and holder name.
get_account(account_number): Returns the account object associated with the given account number.
deposit(account_number, amount): Deposits the specified amount into the account with the given account number.
withdraw(account_number, amount): Withdraws the specified amount from the account with the given account number.
transfer(from_account_number, to_account_number, amount): Transfers the specified amount from one account to another.
save_to_file(filename): Saves all accounts and their details to a file.
load_from_file(filename): Loads accounts from a file and restores their details.
User Interface:

'''


from Account_class import Account  # Importing the Account class

class Bank:
    
    
  def __init__(self):
        # Empty dictionary to store all accounts with account numbers as keys
        self.accounts = {}
        
# create_account(account_number, account_holder): Creates a new account with the given account number and holder name.
        
  def create_account(self, account_number,account_holder ):
     new_account = Account(account_number, account_holder)
     self.accounts[account_number] = new_account
    #  print(f"Account created for {account_holder}. Account Number: {account_number}")

      
# Method to display all accounts
  def display_accounts(self):
    if not self.accounts:
        print("No accounts available.")
    else:
        for account_number, account in self.accounts.items():
            print(account.display_details())  # Call display_details from the Account class
            
            
     
#get_account(account_number): Returns the account object associated with the given account number.

   # get_account(account_number): Returns the account object associated with the given account number.
  def get_account(self, account_number):
    account = self.accounts.get(account_number)
    
    return account.display_details()


  def deposit(self, account_number, amount):
    account = self.accounts.get(account_number)
    account.deposit(amount)  # Call the deposit method from the Account class
    
  def withdraw(self, account_number, amount):
      account = self.accounts.get(account_number)
      account.withdraw(amount) # Call the withdraw method from the Account class
      
  def tansfer(self, from_account_number, to_account_number, amount):
      from_account_number = self.accounts.get(from_account_number)
      to_account_number = self.accounts.get(to_account_number)
      
      from_account_number.withdraw(amount)
      to_account_number.deposite(amount)
      
      

      
      
      
      
  
        
# Creating an instance of Bank
bank = Bank()

# Creating accounts
Account1 = bank.create_account("301148", "Chitra")
Account2 = bank.create_account("301146", "Keya")
Account3 = bank.create_account("503423", "Shibasish")
Account4 = bank.create_account("46738", "Adrika")



# Displaying accounts
# bank.display_accounts()
print(bank.get_account("301148"))

print(bank.tansfer("301148", "301146", 300))

# from_account_number.display()
# to_account_number.display()
bank.display_accounts()


    










    


    
            
            

              
        