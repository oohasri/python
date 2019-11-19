class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    	return self
    def make_withdrawl(self, withdrawl_amount):
    	self.account_balance -= withdrawl_amount
    	return self
    def display_balance(self):
    	print(self.account_balance)
    def transfer_money(self, transferred_to, amount):
    	self.account_balance -= amount
    	print("Monty's balance is",self.account_balance)
    	transferred_to.make_deposit(amount)
    	transferred_to.display_balance()
    	return self
john = User("John snow", "john@python.com")
john.make_deposit(100).make_deposit(100).make_deposit(100).make_deposit(100).display_balance()
guido = User("Guido van Rossum", "guido@python.com")
guido.make_deposit(2000).make_deposit(2000).make_withdrawl(2000).display_balance()
monty = User("Monty Python", "monty@python.com")
monty.make_deposit(500).make_withdrawl(100).make_withdrawl(100).make_withdrawl(100).display_balance()
monty.transfer_money(john,2000)
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

