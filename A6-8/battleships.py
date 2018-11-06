import os
letterList = ['A','B','C','D','E','F','G','H']
indexDict = {}
letterDict = {}
displayDict = {}

for y in range(0, 64):
	indexDict[y] = letterList[(y//8)] + "" + str((y%8)+1)
	letterDict[letterList[(y//8)] + "" + str((y%8)+1)] = y

class Ship(object):
	"""docstring for Ship"""
	def __init__(self, health, location):
		self.health = health
		self.location = location
		self.sunk = False
	
	def hit(self):
		self.health -= 1
		if self.health == 0:
			self.sunk = True

	def setLocation(self, indexes):
		self.location = indexes

	def getLocation(self):
		return self.location


class Cruiser(Ship):
	def __init__(self):
		Ship.__init__(self, 3, [])
		self.mapCode = 'C'
		self.name = 'Cruiser'

class Battleship(Ship):
	def __init__(self):
		Ship.__init__(self, 4, [])
		self.mapCode = 'B'
		self.name = 'Battleship'

class Destroyer(Ship):
	def __init__(self):
		Ship.__init__(self, 2, [])
		self.mapCode = 'D'
		self.name = 'Destroyer'

class Board(object):
	def __init__(self):
		self.board = """
		X 1    2    3    4    5    6    7    8			
		A {0}    {1}    {2}    {3}    {4}    {5}    {6}    {7} 			B = Battleship\n
		B {8}    {9}    {10}    {11}    {12}    {13}    {14}    {15} 			C = Cruiser\n
		C {16}    {17}    {18}    {19}    {20}    {21}    {22}    {23} 			D = Destroyer\n
		D {24}    {25}    {26}    {27}    {28}    {29}    {30}    {31}	 		X = Hit\n
		E {32}    {33}    {34}    {35}    {36}    {37}    {38}    {39}			O = Miss\n
		F {40}    {41}    {42}    {43}    {44}    {45}    {46}    {47}\n
		G {48}    {49}    {50}    {51}    {52}    {53}    {54}    {55}\n
		H {56}    {57}    {58}    {59}    {60}    {61}    {62}    {63}
		"""
		self.args = []

	def createBoard(self):
		for n in range(0, 64):
			self.args.append('~')

	def printBoard(self):
		print(self.board.format(*self.args))

	def createShip(self, ship):
		add = ship.getLocation()
		for n in range(0, 64):
			if indexDict[n] in add:
				self.args[n] = ship.mapCode

	def addShot(self, s, c):
		argsNum = letterDict[s]
		self.args[argsNum] = c

class Player(object):
	def __init__(self, n):
		self.num = n
		self.cruiser = Cruiser()
		self.battleship = Battleship()
		self.destroyer = Destroyer()
		self.ships = [self.cruiser, self.battleship, self.destroyer]
		self.shipCoords = []
		self.playerBoard = Board()
		self.playerBoard.createBoard()
		self.enemyBoard = Board()
		self.enemyBoard.createBoard()
		self.loss = False
		self.enemy = None
		self.sinks = 0
		

	def setLocations(self):
		if self.num == 1:
			global p2
			self.enemy = p2
		else:
			global p1
			self.enemy = p1

		for n in self.ships:
			while True:
				os.system('cls')
				print('Player {} choose the location for your ships:'.format(self.num))
				self.playerBoard.printBoard()
				coordList = input("Please enter {0} sequential coordinate values to set your {1}\nPlease enter the stated number of coordinates in the format 'X1 X2 ...'\n>".format(
					n.health, n.name)).strip().split(' ')
				if len(coordList) != n.health:
					input("Invalid number of coordinates.\nPlease enter the specified number of coordinates.\nPress any key to try again.")
					continue

				for x in coordList:
					if x in self.shipCoords:
						input("Ships can not be overlapping.\nPlease enter valid coordinates where there is not another ship.\nPress any key to try again.")
						break
					if x not in letterDict:
						input("Invalid coordinate of '{0}'\nPlease enter a valid coordinate from the board.\nPress any key to try again.".format(x))
						break
				else:
					if sequential(coordList) == False:
						input("Coordinates must be horizontal or vertical and sequential.\nPress any key to try again.")
						continue
					else:
						n.setLocation(coordList)
						for y in coordList:
							self.shipCoords.append(y)
						self.playerBoard.createShip(n)
						os.system('cls')
						break
				continue	
		
		for n in self.ships:
			for x in n.getLocation():
				self.shipCoords.append(x)

	def turn(self):
		print('Enemy Board')
		self.enemyBoard.printBoard()
		print('Player {} Board'.format(self.num))
		self.playerBoard.printBoard()
		shot = input("Please select a coordinate for your turn \nex: 'X1'\n>").strip()
		if shot in self.enemy.shipCoords:
			print('HIT')
			for n in self.enemy.ships:
				if shot in n.getLocation():
					n.hit()
					if n.sunk:
						print('Enemy {} has been sunk!'.format(n.name))
						self.sinks += 1
			self.enemyBoard.addShot(shot, 'X')
			if self.sinks == 3:
				print('loss')
				self.enemy.loss = True
				return
		else:
			print('MISS')
			self.enemyBoard.addShot(shot, 'O')
		print('Enemy Board')
		self.enemyBoard.printBoard()
		print('Player Board')
		self.playerBoard.printBoard()
		input('Please press any key to complete your turn...')
		os.system('cls')

def sequential(coords):
	last = ' '
	for n in coords:
		if last == ' ':
			last = n
			continue
		else:
			if (abs(letterDict[n] - letterDict[last]) == 1) or (abs(letterDict[n] - letterDict[last]) == 8):
				return True
			else:
				return False

p1 = Player(1)
p2 = Player(2)
os.system('cls')
p1.setLocations()
os.system('cls')
input('Please switch players\nPress any key when ready')
p2.setLocations()

while p1.loss == False and p2.loss == False:
	p1.turn()
	if p2.loss == True:
		break
	os.system('cls')
	input('Please switch players\nPress any key when ready')
	p2.turn()
	if p1.loss == True:
		break
	os.system('cls')
	input('Please switch players\nPress any key when ready')

if p2.loss:
	print('Player 1 wins!!!')
else:
	print('Player 2 wins!!!')




		

