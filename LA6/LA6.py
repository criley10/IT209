""" Chris Riley - IT209 LA6
	Inheritance and derived classes"""

class IntegerList(list):

	"""takes a list and determines if the list contains anything other than int"""
	def validIntList(self):
		for n in self:
			if isinstance(n, int) == False:
				return False, 'error: {0}'.format(n)
		return True, ''

	"""takes a list and finds the max value if valid """	
	def maxInt(self):
		valid, reason = self.validIntList()
		if valid:
			big = self[0]
			for n in self:
				if n > big:
					big = n
			return big
		else:
			return ''

	"""takes a list and finds the min value if valid """
	def minInt(self):
		valid, reason = self.validIntList()
		if valid:
			small = self[0]
			for n in self:
				if n < small:
					small = n
			return small
		else:
			return ''

	"""takes a list and prints it by index if valid """
	def printIntList(self):
		valid, reason = self.validIntList()
		if valid:
			for n in self:
				print(n)
		else:
			print(valid, reason)


IL1 = IntegerList([66,55,98,13,25,48,48,78,168,697,3])
IL2 = IntegerList([123,13,"QWERTY",33])
print('\nList IL1: ')
IL1.printIntList()
print('Largest integer= ', IL1.maxInt())
print('Smallest integer= ', IL1.minInt())
print('\nList IL2: ')
IL2.printIntList()
print('Largest integer= ', IL2.maxInt())
print('Smallest integer= ', IL2.minInt())