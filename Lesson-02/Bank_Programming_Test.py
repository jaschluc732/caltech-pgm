from colorama import *
init()

class Bank:
    """Bank class with method and attributes to use with different bank instances"""
    def __init__(self, bankname, ifcs_code, branch, location):
        self.bankname = bankname
        self.ifcs_code = ifcs_code
        self.branch = branch
        self.location = location

    def bankinfo(self):
        print(Fore.RED + "*" * 65 +Fore.RESET)
        print("Thank you for choosing " + self.bankname,
              "\nIFSC Code: " + self.ifcs_code,
              "\nBranch: " + self.branch,
              "\nLocation: " + self.location)
        print (Fore.RED + "*" * 65 + Fore.RESET)


class Customer(Bank):
    """Customer class that inherits bank attributes, also has method and attributes to use with different customer instances"""
    def __init__(self, bankname, ifcs_code, branch, location, customer_ID, customer_name, customer_address, contact):
        super ().__init__ (bankname, ifcs_code, branch, location)
        self.customer_ID = customer_ID
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.contact = contact

    def getaccountinfo(self):
        """method and attributes to use with different customer account instances"""
        print ("\nHi " + self.customer_name + ", Welcome to your Account - your customer information is:\nCustomer ID: " + self.customer_ID,
               "\nCustomer Address: " + self.customer_address,
               "\nContact: " + self.contact)

r1 = Customer("Bank of Singapore", "xddg789", "Singapore Main", "123 Singapore Circle", "", "John Smith", "324 Confluence St, East Singapore, Singapore", "+88987765454")
r1.bankinfo()

class Account(Customer):
    """Account class that inherits from Customer class with method and attributes to use with different account instances"""
    def __init__(self, bankname, ifcs_code, branch, location, customer_ID, customer_name, customer_address, contact, accountID, balance=0):
        super ().__init__ (bankname, ifcs_code, branch, location, customer_ID, customer_name, customer_address, contact)
        self.accountID = accountID
        self.balance = balance

    def deposit(self, amount):
        """make a deposit"""
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        """make a withdraw"""
        if amount > self.balance or amount < 0:
            try:
                raise ValueError
            except ValueError:
                print(Fore.RED + "insufficient funds" + Fore.RESET)

        else:
         self.balance -= amount

    def get_balance(self):
        """check the balance"""
        print(Fore.RED + "Your current account balance is $" + str(self.balance) + Fore.RESET)

r2 = Account ("Bank of Singapore", "xddg789", "Singapore Main", "123 Singapore Circle", "", "John Smith", "324 Confluence St, East Singapore, Singapore", "+88987765454", "ACCT87678")


class SavingsAccount(Account):
    """SavingsAccount class that inherits from Account class, with method and attributes to use with different account instances"""
    def __init__(self, bankname, ifcs_code, branch, location, customer_ID, customer_name, customer_address, contact, accountID, balance, minbalance=0):
        super ().__init__ (bankname, ifcs_code, branch, location, customer_ID, customer_name, customer_address, contact, accountID, balance)
        self.minbalance = minbalance

    def getsavingaccountinfo(self):
        """method and attributes to use with different customer account instances"""
        print ("\nHi " + self.customer_name + ", Welcome to your Savings Account - your customer information is:\nCustomer ID: " + self.customer_ID,
               "\nCustomer Address: " + self.customer_address,
               "\nContact: " + self.contact,
               "\nYour Minimum Balance is set to: " + str(self.minbalance))


r3 = SavingsAccount ("Bank of Singapore", "xddg789", "Singapore Main", "123 Singapore Circle", "", "John Smith", "324 Confluence St, East Singapore, Singapore", "+88987765454", "SAV87678", 0)


class Atm(SavingsAccount):
    """Atm class that inherits from SavingsAccount class, with menus to select account type and withdraw, deposit, balance and exit"""
    def __init__(self, bankname, ifcs_code, branch, location, customer_ID, customer_name, customer_address, contact, accountID, balance):
        super ().__init__ (bankname, ifcs_code, branch, location, customer_ID, customer_name, customer_address, contact, accountID, balance)


customer1 = Atm("Bank of Singapore", "xddg789", "Singapore Main", "123 Singapore Circle", "", "John Smith", "324 Confluence St, East Singapore, Singapore", "+88987765454", "JS8767", 0)
customer1.customer_ID = str (input (Fore.RED + "*" * 65 + Fore.RESET + "\nWelcome to the Bank of Singapore - Please enter you Customer ID1: "))

print ("Account ID: "+ customer1.accountID + "\n" + Fore.RED + "*" * 65 + Fore.RESET)

if customer1.customer_ID != 0:

     def menu():
         print ("*" * 65)
         print ("[1] Account")
         print ("[2] Savings Account")
         print ("*" * 65)

     menu ()
     choice = int (input ("Please choose Account or Savings Account: "))

     while choice != 0:
         if choice == 1:

             customer1.getaccountinfo()
             break
         elif choice == 2:
             customer1.getsavingaccountinfo()
             break
         else:
             print (Fore.RED + "Invalid Option" + Fore.RESET)

         menu ()
         choice = int (input ("Please choose Account or Savings Account: "))

else:
 print("not this")


if customer1.customer_ID != 0:

     def menu():
         print ("*" * 48)
         print ("[1] Withdrawal")
         print ("[2] Deposit")
         print ("[3] Balance")
         print ("[0] Exit and return card")
         print ("*" * 48)

     menu ()
     choice = int (input ("Please select Withdrawal, Deposit, Balance or Exit and return card: "))

     while choice != 0:
         if choice == 1:

                 try:
                      amount = int (input ("Please enter Withdraw Amount or enter Q to sign-off $"))
                      customer1.withdraw (amount)
                      customer1.get_balance ()
                 except ValueError:
                     break

         elif choice == 2:

                 try:
                      amount = int (input ("Please enter Deposit Amount or enter Q to sign-off $"))
                      customer1.deposit (amount)
                      customer1.get_balance ()
                 except ValueError:
                     break

         elif choice == 3:
             customer1.get_balance()

         else:
             print (Fore.RED + "Invalid Option" + Fore.RESET)

         menu ()
         choice = int (input ("Please select Withdrawal, Deposit, Balance or Exit and return card: "))
     print ("*" * 48 + "\n")

     print (Fore.RED + "Thank you for using Bank of Singapore. Please remove your card." + Fore.RESET)
else:
 print("not this")
