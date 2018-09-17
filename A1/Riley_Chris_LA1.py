"""
	Riley_Chris_LA1.py

	Review of key Python features.
	Read in list items from file and create Dict then output Dict to file
"""

""" 
Loads the items from the external text file given. 
Creates a nested list with a sublist for each category.
Returns the new master list. 
"""
def loadItems():	
	file = open('A1input.txt', 'r')
	content = file.readlines()
	file.close()
	items = [[],[],[],[]]
	#  books0, food1, elect2, cloth3

	for n in content:
		line = n.strip().split(',')
		line[3] = line[3].strip()

		if line[0][0] == 'B':
			items[0].append(line)
		elif line[0][0] == 'F':
			items[1].append(line)
		elif line[0][0] == 'E':
			items[2].append(line)
		else:
			items[3].append(line)
	return items

""" Displays the list provided on call. """
def displayItems(ls):
	[print(n) for n in ls]


#global code
itemList = loadItems()
displayItems(itemList[0])
displayItems(itemList[1])
displayItems(itemList[2])
displayItems(itemList[3])