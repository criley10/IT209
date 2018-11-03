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
		

	def setLocations(self):
		if self.num == 1:
			global p2
			self.enemy = p2
		else:
			global p1
			self.enemy = p1

		self.playerBoard.printBoard()
		self.battleship.setLocation(input("Please enter 4 coordinate values to set your Battleship \nex: 'X1 X2 X3 X4'\n>").strip().split(' '))
		self.playerBoard.createShip(self.battleship)
		bLoc = self.battleship.getLocation()
		os.system('cls')
		self.playerBoard.printBoard()
		self.cruiser.setLocation(input("Please enter 3 coordinate values to set your Battleship \nex: 'X1 X2 X3'\n>").strip().split(' '))
		self.playerBoard.createShip(self.cruiser)
		cLoc = self.cruiser.getLocation()
		os.system('cls')
		self.playerBoard.printBoard()
		self.destroyer.setLocation(input("Please enter 2 coordinate values to set your Battleship \nex: 'X1 X2'\n>").strip().split(' '))
		self.playerBoard.createShip(self.destroyer)
		dLoc = self.destroyer.getLocation()
		os.system('cls')
		self.playerBoard.printBoard()
		for n in self.ships:
			for x in n.getLocation():
				self.shipCoords.append(x)
		os.system('cls')

	def turn(self):
		print("Player {0}'s turn:".format(self.num))
		self.enemyBoard.printBoard()
		self.playerBoard.printBoard()
		shot = input("Please select a coordinate for your turn \nex: 'X1'\n>").strip()
		if shot in self.enemy.shipCoords:
			print('HIT')
			for n in self.enemy.ships:
				if shot in n.getLocation():
					n.hit()
					if n.sunk:
						print('Enemy {} has been sunk!'.format(n.name)) 
			self.enemyBoard.addShot(shot, 'X')
		else:
			print('MISS')
			self.enemyBoard.addShot(shot, 'O')



p1 = Player(1)
p2 = Player(2)
p1.setLocations()
p2.setLocations()





		

