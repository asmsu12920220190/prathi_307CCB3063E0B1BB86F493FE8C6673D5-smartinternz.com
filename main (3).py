class Bank_Account:
  def init(self):
    self.balance=0
    print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
  def deposit(self):
    amount=float(input("Enter amount to be Deposited:"))
    self.balance=amount
    print("\n Amount Deposited:",amount)
  def withdraw(self):
    amount=float(input("Enter amount to be Withdawn:"))
    if self.balance>=amount:
      self.balance-=amount
      print("\n You Withdaw:",amount)
    else:
      print("\n Insufficient balance ")
  def display(self):
   print("\n Net Available Balance=",self.balance)
s=Bank_Account()
s.deposit()
s.withdraw()
s.display()