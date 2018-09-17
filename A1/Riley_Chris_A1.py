"""
	Riley_Chris_A1.py

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

""" Creates a dictioonary from the master list provided on call. """
def buildDict(master):
	webster = {}
	for catList in master:
		valueList = [[item[0], item[2], item[3]] for item in catList]
		webster[catList[0][1]] = valueList
	return webster

""" Displays the dictionary provided on call. """
def displayDict(masterDict):
	for n in masterDict:
		for x in range(0, len(masterDict[n])):
			print(n + ' ' + str(masterDict[n][x]))

""" Writes the dictionary to an output file. """
def writeDictFile(masterDict):
	file = open('RileyCA1output.txt', 'w')
	for n in masterDict:
		for x in range(0, len(masterDict[n])):
			file.write(n + ',' + str(masterDict[n][x][0]) + ',' + str(masterDict[n][x][1]) + ',' + str(masterDict[n][x][2]) + '\n')
	file.close()

#global code
itemList = loadItems()
displayItems(itemList[0])
displayItems(itemList[1])
displayItems(itemList[2])
displayItems(itemList[3])
itemDict = buildDict(itemList)
displayDict(itemDict)
writeDictFile(itemDict)