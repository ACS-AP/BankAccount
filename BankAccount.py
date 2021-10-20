

class BankAccount:
  def __init__(self, full_name, account_number, balance):
    self.name = full_name
    self.number = account_number
    self.balance = balance

  def deposit(self, amount):
      total = amount + self.balance
      return (f'Amount deposited: ${amount} New Balance: ${total}')
      
  def withdraw(self, amount):
      if amount > self.balance:
          self.balance -= 10
          return ('Insufficient Funds.')
      total = self.balance - amount
      return (f'Amount withdrawn: ${amount} New Balance: ${total}')

  def get_balance(balance):
      return (f'Account Balance: {balance}')

  def add_interest(balance):
      interest = balance * 0.00083
      total = interest + balance
      return(total)

  def print_statement(self, name, number, balance):
      return(f'{name} Account No.:{number} Balance: {balance}')
