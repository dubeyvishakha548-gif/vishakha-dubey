class BankAccount:
  def _init_(self, name, balance):
    self.account_number = random.randint(10*15, 10*16 - 1)
    self.AccountHolderName = name
    self.balance = balance
  def deposite(self, amount):
    if amount > 0:
      self.balance += amount
      return "Balance has been updated."
    else:
      return "Invalid amount"
def display_balance(self):
    print(f"Current Balance: Rs{self.balance}")
class SavingAccount(BankAccount):
    interest_rate = 4
    def apply_interest(self):
        interest = self.balance * (self.interest_rate/100)
        self.balance += interest
        print(f"Interest of Rs{interest} added at {self.interest_rate}% rate")
class CurrentAccount(BankAccount):
    overdraft_limit = 50000
    def withdraw(self, amount):
       if self.balance - amount >= self.overdraft_limit:
           self.balance -= amount
           print(f"{amount} withdrawn successfully")
       else:
           print("limit exceeded")

print("Welcome to INDIAN bank ltd")
acc_type = input("Enter account type(Saving/Current):")
name = input("Enter account holder name:")
initial_balance = float(input("Enter Initial balance:"))
if acc_type =="saving":
  account = SavingAccount(name, initial_balance)
  print("Your saving account has been created successfully")
  print(f"Account Number: {account.account_number}")
elif acc_type == "current":
  account = CurrentAccount(name, initial_balance)
  print("Your current account has been created successfully")
  print(f"Account Number: {account.account_number}")
else:
  print("invalid account type")
  exit()
while True:

    print("1. Deposit\n2. Withdraw\n3. Display Balance\n5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Enter deposit amount: "))
        account.deposite(amt)
        break

    elif choice == "2":
        amt = float(input("Enter withdraw amount: "))
        account.withdraw(amt)
        break

    elif choice == "3":
        account.display_balance()
        break

    elif choice == "4" and acc_type == "saving":
        account.apply_interest()
        break

    elif choice == "5":
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice!")