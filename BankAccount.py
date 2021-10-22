

class BankAccount:
  def __init__(self, full_name, account_number, balance):
    self.name = full_name
    self.number = account_number
    self.balance = balance

  def deposit(self, amount):
      total = amount + self.balance
      print(f'Amount deposited: ${amount} New Balance: ${total}')
      
  def withdraw(self, amount):
      if amount > self.balance:
          self.balance -= 10
          return ('Insufficient Funds.')
      total = self.balance - amount
      print (f'Amount withdrawn: ${amount} New Balance: ${total}')

  def get_balance(self):
      print (f'Account Balance: ${self.balance}')

  def add_interest(self):
      interest = self.balance * 0.00083
      total = interest + self.balance
      print(total)

  def print_statement(self):
      print(f'{self.name} Account No.:{self.number} Balance: {self.balance}')


mitchell_account = BankAccount("Mitchell", 2173542, 100)
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.withdraw(20)


