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


from Account_class import Account # type: ignore
import pandas as pd



class Bank:
    
    
  def __init__(self):
        # Empty dictionary to store all accounts with account numbers as keys
        self.accounts = {}
        
        # Read CSV file into pandas DataFrame
        self.df = pd.read_csv('Account_details.csv')
        print(self.df)
        
        # Populate the accounts dictionary from the DataFrame
        for index, row in self.df.iterrows():
            account_no = row['Account_Number']
            name = row['Name']
            balance = row['Balance']
            phone = row['Phone']
            
            # Create an Account object
            account = Account(account_no, name, phone, balance)
            # Store in the dictionary
            self.accounts[account_no] = account  
            
     

        
#   def create_account(self, account_number,account_holder ):
  def create_account(self, account_no, name, ph_no,balance = 500 ):
     new_account = Account(account_no, name, ph_no,balance )
     self.accounts[account_no] = new_account
     self.accounts[name] = new_account
     self.accounts[ph_no] = new_account
     self.accounts[balance]= new_account
     
     new_data = {
        'Account_Number': account_no,
        'Name': name,
        # 'Balance': new_account.balance,
        'Balance': balance,
        'Phone': ph_no
        
        }
    
    # Append the new account to the DataFrame and save it to the CSV file
     self.df = self.df.append(new_data, ignore_index=True)
     print(self.df)
     self.df.to_csv('Account_details.csv', index=False)  # Save to CSV file
     
    #  print(f"Account created for {account_holder}. Account Number: {account_number}")

      
# Method to display all accounts
  def display_accounts(self):
    if not self.accounts:
        print("No accounts available.")
    else:
        for account_no, account in self.accounts.items():
            print(account.display_details())  # Call display_details from the Account class
            
            
     
#get_account(account_number): Returns the account object associated with the given account number.

   # get_account(account_number): Returns the account object associated with the given account number.
  def get_account(self, account_no):
    account = self.accounts.get(account_no)
    return account.display_details()


  def deposite(self, account_no, amount):
        account = self.accounts.get(account_no)
        
        if account:
            account.deposite(amount)
            self.df.loc[self.df['Account_Number'] == account_no, 'Balance' ] = account.balance
            self.df.to_csv('Account_details.csv', index=False)
            print(f"${amount} deposited successfully to {account_no}.")
            print(f" New Balance after deposite ", account.balance)
        else:
            print("Account not found.")
    
  def withdraw(self, account_no, amount):
      account = self.accounts.get(account_no)
      if account:
         account.withdraw(amount) # Call the withdraw method from the Account class
         self.df.loc[self.df['Account_Number'] == account_no, 'Balance' ] = account.balance
         self.df.to_csv('Account_details.csv', index=False)
         print(f"${amount} withdrawn successfully to {account_no}.")
         print(f" New Balance after withdrawn ", account.balance)
      else:
            print("Account not found.")
            
  def transfer(self, from_account_number, to_account_number, amount):
      from_account = self.accounts.get(from_account_number)
      to_account = self.accounts.get(to_account_number)
      
      if from_account and to_account:
          if from_account.withdraw(amount):
            self.df.loc[self.df['Account_Number'] == from_account_number, 'Balance' ] = from_account.balance
            # self.df.to_csv('Account_details.csv', index=False)
            # print(self.df)
            print(f"${amount} withdrawn successfully from {from_account_number}.")
            print(f" New Balance after withdrawn ", from_account.balance)
            to_account.deposite(amount)
            self.df.loc[self.df['Account_Number'] == to_account_number, 'Balance' ] = to_account.balance
            # self.df.to_csv('Account_details.csv', index=False)
            
            print(f"${amount} withdrawn successfully to {to_account_number}.")
            print(f" New Balance after withdrawn ", to_account.balance)
            print(f"${amount} deposited successfully from {from_account_number} to the account {to_account_number}.")
            
            self.df.to_csv('Account_details.csv', index=False)
            print(self.df)
            
      else:
         print("Account not found.")
      
      
# Creating an instance of Bank
bank = Bank()
      

def print_menu():
    print("1. Create Account")
    print("2. Deposite")
    print("3. WithDraw")
    print("4. Transfer")
    print("5. Get Account Details")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
              
            print("You have chosen to Create your account")
            name = input("Please write your name : ")
            ph_no =input("Please write your ph no")
            account_no = name[0:2] + ph_no[0:2]
            print(account_no)
            bank.create_account(account_no, name, ph_no )
            # print(f"Create the account with Account no {Account_no}")
            print(f"Account created for Name: {name}, Account Number: {account_no}")
                
       
        elif choice == '3':
            
            print("You have chosen to deposit money.")
            account_no = input("Please enter your account number: ")
            df = pd.read_csv('Account_details.csv')  # Load account details from CSV

            if df['Account_Number'].isin([account_no]).any():
                print("Account found")
                try:
                    amount = float(input("Enter the amount to deposit: "))
                    bank.deposite(account_no, amount)
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
            else:
                print("Account not found.")  
            
        elif choice == '4':
              
              print("You have chosen to withdraw money.")
              account_no = input("Please enter your account number: ")
              df = pd.read_csv('Account_details.csv')  # Load account details from CSV

              if df['Account_Number'].isin([account_no]).any():
                print("Account found")
                try:
                    amount = float(input("Enter the amount to Withdraw: "))
                    bank.withdraw(account_no, amount)
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
              else:
                print("Account not found.")  
            
             
        elif choice == '4':
            
            print("You have chosen to Transfer the money.")
            
            from_account_number = input("Money will be transferred from :" )
            to_account_number = input (" Money will be transferred to ")
            
            df = pd.read_csv('Account_details.csv')  # Load account details from CSV
            
            if df['Account_Number'].isin([from_account_number]).any() and df['Account_Number'].isin([from_account_number]).any():
                print("Account found")
                try:
                    amount = float(input("Enter the amount to transfer: "))
                    bank.transfer(from_account_number, to_account_number, amount)
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
            else:
                print("Account not found.")  
            
            
            
        elif choice == '5':  
             print("Show the details of the account")
             account_no = input(" Put the account number :" )
             
             df = pd.read_csv('Account_details.csv')  # Load account details from CSV
             
             if df['Account_Number'].isin([account_no]).any():
                print("Account found")
                try:
                    bank.get_account(account_no)
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
             else:
                    print("Account not found.")  
                 
              
             
        
        break
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Creating an instance of Bank
#bank = Bank()

# Creating accounts
#Account1 = bank.create_account("301148", "Chitra")
#Account2 = bank.create_account("301146", "Keya")
#Account3 = bank.create_account("503423", "Shibasish")
#Account4 = bank.create_account("46738", "Adrika")



# Displaying accounts
# bank.display_accounts()
#print(bank.get_account("301148"))

#print(bank.tansfer("301148", "301146", 300))

# from_account_number.display()
# to_account_number.display()
#bank.display_accounts()


    










    


    
            
            

              
        