class Polygon(object):
	"""
	Creates a Polygon based on the number
	of sides passed when created
	"""
	def __init__(self, s):
		self.no_of_sides = s
		self.sides = []

	def inputSides(self):
		for n in range(0, self.no_of_sides):
			self.sides.append(int(input('Enter side {}: '.format(n+1))))

	def dispSides(self):
		for n in range(0, len(self.sides)):
			print("Side {} length is {}".format(n+1, self.sides[n]))

class Triangle(Polygon):
	"""Creates a Triangle from Polygon"""
	def __init__(self):
		Polygon.__init__(self, 3)

	def findArea(self):
		a = self.sides[0]
		b = self.sides[1]
		c = self.sides[2]
		s = (a+b+c)/2
		area =  (s*(s-a)*(s-b)*(s-c)) ** 0.5 
		print('The area of the Triangle is {0:0.2f}'.format(area))

class Square(Polygon):
	"""Creates a Square from Polygon"""
	def __init__(self):
		Polygon.__init__(self, 1)

	def findArea(self):
		area = self.sides[0] ** 2
		print('The area of the Square is {0:0.2f}'.format(area))

class Rectangle(Polygon):
	"""Creates a Rectangle from Polygon"""
	def __init__(self):
		Polygon.__init__(self, 2)

	def findArea(self):
		area = self.sides[0] * self.sides[1]
		print('The area of the Rectangle is {0:0.2f}'.format(area))

#Global Code
print('TRIANGLE:')
t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()

print('\n')

print('SQUARE:')
s = Square()
s.inputSides()
s.dispSides()
s.findArea()

print('\n')

print('RECTANGLE:')
r = Rectangle()
r.inputSides()
r.dispSides()
r.findArea()

