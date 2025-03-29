class BankAccount:
 def init(self, balance) :
  if balance < 0:
   raise ValueError ("net. ")
  self. balance = balance

 def withdraw(self, amount) :
  if amount <= 0:
   raise ValueError("onet.")
  if amount > self. balance:
   raise ValueError ("gived my money. ")



