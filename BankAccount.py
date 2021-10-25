

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
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.withdraw(20)
mitchell_account.checkorsave()


