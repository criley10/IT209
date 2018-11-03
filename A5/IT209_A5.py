"""
	Chris Riley - IT209_A5.py
	Extending the Dictionary class
"""

class NewDict(dict):

	def displaysorted(self, d):
		sortedKeys = sorted([n for n in self])
		sortedList = [[n, self[n]] for n in sortedKeys]
		if d not in ['D', 'B', 'R']: d = 'D'
		if d == 'D' or d == 'B':
			for n in sortedKeys:
				print(str(n) + ": " + str(self[n]))
			if d == 'B':
				return sortedList
		else:
			return sortedList

	def addfromlist(self, addFrom):
		self.addFrom[0] = addFrom[1:]

	def retrive(self, li):
		returnList = []
		if isinstance(li, list):
			for n in li:
				if n in self:
					returnList.append([n, self[n]])
				else:
					returnList.append([n, 'not found'])
			return True, returnList
		else:
			return False, 'not a list'

	def merge(self, dic):
		dupes = []
		if isinstance(dic, dict):
			for n in dic:
				if n in self:
					dupes.append(n)
				else:
					self[n] = dic[n]
			return True, dupes
		else:
			return False, 'not a dictionary'