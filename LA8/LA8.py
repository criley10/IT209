""" LA8.py - Exception Handling
	Chris Riley
"""
class isInt():
	def __contains__(self, n):
		try:
			int(n)
			return True
		except:
			return False

class Error(Exception):

	def __init__(self, error):
		self.error = error

class BankAccount(object):

	def __init__(self, accNo):
		try:
			if (len(accNo) > 9) or (len(accNo) < 9):
				raise Error ('Length of account number invalid')
			elif accNo not in isInt:
				raise Error ('Account number should only contain numbers')
			else:	
				self.accNo = accNo
				self.balance = 0
		except Error as ER:
			print('Error raised in account creation: {}'.format(ER.error))
			quit()

	def withdraw(self, amount):
		try:
			if amount > self.balance:
				raise Error ('Cannot make a withdraw greater than your balance {0}'.format(self.balance))
			else:
				self.balance -= amount
				f = open('{0}.txt'.format(self.accNo), 'a')
				f.write('Amount of {0} withdrawn from account number {1}.\nNew balance: {2}\n'.format(
					amount, self.accNo, self.balance))
				f.close()
				return self.balance
		except Error as ER:
			print('Error raised in withdraw: {0}'.format(ER.error))
			quit()

	def deposit(self, amount):
		try:
			if amount > 5000:
				raise Error ('Cannot deposit more than $5,000')
			else:
				self.balance += amount
				f = open('{0}.txt'.format(self.accNo), 'a')
				f.write('Amount of {0} deposited to account number {1}.\nNew balance: {2}\n'.format(
					amount, self.accNo, self.balance))
				f.close()
				return self.balance
		except Error as ER:
			print('Error raised in deposit: {0}'.format(ER.error))
			quit()

	def printStmt(self):
		f = open('{0}.txt'.format(self.accNo), 'r')
		statement = f.readlines()
		for n in statement:
			print(n)

isInt = isInt()
a = BankAccount('123456789')
a.deposit(500)
a.withdraw(20)
a.printStmt()
