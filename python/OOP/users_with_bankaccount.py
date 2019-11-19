class User:
    def __init__(self, username, email_address, acc_num):
        self.name = username
        self.email = email_address
        self.acc_num = acc_num
        self.account = BankAccount(acc_num, int_rate=2, balance=0)
class BankAccount:
	def __init__(self, acc_num, int_rate=2, balance=0):
		self.acc_num = acc_num
		self.int_rate = int_rate
		self.account_balance = balance
		print("Acc number",self.acc_num)
		print("Acc balance",self.account_balance)
	def deposit(self,  amount):
		self.account_balance += amount
		return self
	def withdrawl(self, amount):
		self.account_balance -= amount
		if self.account_balance - amount<0:
			print("Insufficient funds")
		return self
	def display_account_info(self):
		print("My account balance",self.account_balance)
	def yield_interest(self, years, int_rate):
		self.int_rate = self.account_balance * years * int_rate/100
		self.account_balance += self.int_rate
		print(self.int_rate)
		return self
ooha = User("ooha","@gmail",1234)
ooha1 = User("ooha","@gmail",3333)
ooha.account.deposit(100)
ooha.account.display_account_info()

# ooha1.make_deposit(200)
# ooha1.display_balance()
# john = BankAccount(23224, 2, 2000)
ooha.account.deposit(1000).deposit(1000).deposit(1000).withdrawl(1000).yield_interest(2,2).display_account_info()
# john = BankAccount(20000, 2, 70000)
# john.deposit(1000).deposit(1000).deposit(1000).withdrawl(1000).yield_interest(2,2).display_account_info()
# rick = BankAccount(21322, 2, 3000)
# rick.deposit(200).deposit(200).withdrawl(100).withdrawl(100).withdrawl(100).withdrawl(100).yield_interest(4,4).display_account_info()