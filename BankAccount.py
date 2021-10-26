

class BankAccount:
  def __init__(self, full_name, account_number, balance):
    self.name = full_name
    self.number = account_number
    self.balance = balance

  def deposit(self, amount):
      total = amount + self.balance
      print(f'Amount deposited: ${amount} New Balance: ${total}')
      
  def withdraw(self, amount):
      if amount >= self.balance :
            print('Insufficient Funds.')
            self.balance -= 10
            print(f'{self.name} charged overdraft fee of $10 new balance: ${self.balance}')
      else :
            self.balance -= amount
            print(f'{self.name} withdrew: ${amount} new balance: ${self.balance}')

  def get_balance(self):
      print (f'Account Balance: ${self.balance}')

  def add_interest(self):
      self.balance += self.balance * 0.00083
      print(self.balance)

  def print_statement(self):
      print('\n----- Statement -----')
      print(self.name)
      print(f'Account No.: {self.name}')
      print(f'Balance: ${self.balance}')
      print('---------------------\n')


mitchell_account = BankAccount("Mitchell", 2173542, 100)
mitchell_account.add_interest()
mitchell_account.withdraw(20)
mitchell_account.print_statement()

account_1 = BankAccount('Shawn', '76582065', 9840)
account_1.deposit(50.00)
account_1.get_balance()
account_1.add_interest()
account_1.withdraw(710)
account_1.print_statement()

account_2 = BankAccount('Mary', '86756243', 765850)
account_2.deposit(75.00)
account_2.get_balance()
account_2.withdraw(10000)
account_2.add_interest()
account_2.print_statement()

account_3 = BankAccount('Joshua', '87659123', 20)
account_3.deposit(100.00)
account_3.get_balance()
account_3.withdraw(2)
account_3.add_interest()
account_3.print_statement()


