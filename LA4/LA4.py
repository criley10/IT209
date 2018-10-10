""" Chris Riley
	LA4.py - Baggage container and InventoryItem
	Baggage containers hold items and manipulate inventory of Items
"""

class Baggage:
	"""Baggage class
	Class that holds InventoryItems
	"""
	allowed_items = ['pen', 'book', 'cap', 'coat', 'umbrella', 'gloves', 
		'jacket', 'food', 'wallet', 'keys', 'laptop', 'phone', 
		'chapstick', 'spectacles', 'calculator']

	def __init__(self, maxCount):
		self.maxCount = maxCount
		self.inventory = []

	def add_item(self, item):
		if len(self.inventory) < self.maxCount:
			if item.item_name.lower() in Baggage.allowed_items:
				self.inventory.append(item)
				return True, 'Success'
			else:
				return False, 'Item not allowed'
		else:
			return False, 'Capacity'

	def remove_item(self, item):
		valid = self.has_item(item)
		if valid:
			self.inventory.remove(item)
			return valid
		else:
			return valid

	def has_item(self, item):
		if item in self.inventory:
			return True
		else:
			return False

	def print_items(self):
		print('Printing inventory')
		for n in self.inventory:
			print(n.item_name)
		print('\n')

class InventoryItem:
	"""InventoryItem"""
	def __init__(self, item_name):
		self.item_name = item_name
		
"""Global Code"""
print('Start of code')
print('Creating Items')
it1 = InventoryItem("book")
print('Created ' + it1.item_name)
it2 = InventoryItem("umbrella")
print('Created ' + it2.item_name)
it3 = InventoryItem("coat")
print('Created ' + it3.item_name)
it4 = InventoryItem("pen")
print('Created ' + it4.item_name)
it5 = InventoryItem("cap")
print('Created ' + it5.item_name) 
print('Done creating Items\n')

print('Created Baggage\n')
backpack = Baggage(maxCount = 3)
satchel = Baggage(maxCount = 5)

print('Adding it1-3 to backpack:')
print(backpack.add_item(it1))
print(backpack.add_item(it2))
print(backpack.add_item(it3))
backpack.print_items()
print('Attempting to add it4:', backpack.add_item(it4))
print('Backpack has item it1:', backpack.has_item(it1))
print('\n')
print('Adding it4 and it5 to satchel:')
print(satchel.add_item(it4))
print(satchel.add_item(it5))
satchel.print_items()
print('Removing it4:', satchel.remove_item(it4))
satchel.print_items()



