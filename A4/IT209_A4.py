""" Chris Riley - IT209_A4.py
	Department container assignment
"""

##chnages need to be made to department to add faculty and store different rosters
class Person():
	totalEnrollment = 0
	def __init__(self, name, address, phone, email):
		Person.totalEnrollment += 1
		self.g_num = "G{0:05d}".format(Person.totalEnrollment)
		self.name = name
		self.address = address
		self.phone = phone
		self.switchName = self.name.split(',')[1].strip()
		self.switchName = self.switchName + " " + self.name.split(',')[0].strip()
		self.email = self.name.split(',')[0].strip().lower() + self.name.split(',')[1][0].lower() + '@gmu.edu'

	def __str__(self):
		return "{0}, {1}, {2}".format(self.g_num, self.switchName, self.address)

	def samePerson(self, p):
		if type(p) == Person and self.name == p.name and self.g_num == p.g_num:
			return True
		else:
			return False

class Department():
	"""Department Object
		Passed variabes -- d_code
		Assigned variables -- d_name, capacity, minGPA, num_students, avgGPA, roster
	"""
	univ_students = 0
	def __init__(self, d_code):
		if d_code == 'ENGR':
			self.d_code = d_code
			self.d_name = 'Engineering'
			self.capacity = 5
			self.minGPA = 2.75
		elif d_code == 'ARTS':
			self.d_code = d_code
			self.d_name = 'Art and Architecture'
			self.capacity = 15
			self.minGPA = 2.0
		elif d_code == 'CHHS':
			self.d_code = d_code
			self.d_name = 'College of Health and Human Services'
			self.capacity = 10
			self.minGPA = 2.5
		else:
			print('Invalid department code given')

		self.num_students = 0
		self.avgGPA = 0
		self.roster = []

	def __str__(self):
		return '{0}, {1}, capacity: {2}, number of students: {3}, average GPA: {4:1.3}'.format(
			self.d_code,self.d_name,str(self.capacity),str(self.num_students),str(self.avgGPA))

	def addStudent(self, s):
		valid, reason = self.isQualified(s)
		if valid:
			self.roster.append(s)
			Department.univ_students += 1
			self.num_students += 1
			s.setMajor(self.d_code)
			self.calcAvgGPA()
			return True, reason
		else:
			return False, reason

	def isQualified(self, s):
		if self.num_students < self.capacity:
			if s.isEnrolled:
				for n in self.roster:
					if s.sameStudent(n):
						return False, 'Dup'
				if s.gpa >= self.minGPA:
					return True, 'Valid'
				else:
					return False, 'GPA'
			else:
				return False, '!Enr'
		else:
			return False, 'Cap'

	def calcAvgGPA(self):
		total = 0
		for n in self.roster:
			total += n.gpa
		self.avgGPA = total / len(self.roster)

	def printRoster(self):
		for n in self.roster:
			print(n.g_num + " - " + n.switchName)

class Student(Person):
	"""Student object
		Passed variabes -- name, major, enrolled, credits, qpoints
		Calculated variables -- g_num, status, gpa, switchName
	"""
	majors = ["Acctg", "Art", "CSci", "Hist", "IST", "Math", "Physics"]
	def __init__(self, major='IST', enrolled='y', credits=0,qpoints=0):
		Person.__init__()
		if major in Student.majors:
			self.major = major
		else:
			print("Major given not valid. Default to IST")
		if enrolled in 'yn':
			self.enrolled = enrolled
		else:
			print("Enrollment charachter not valid. Default to 'y'")
		self.credits = credits
		self.qpoints = qpoints
		self.status = Student.status(self)
		self.gpa = Student.gpa(self)
		
	def __str__(self):
		return "{0}, {1}, {2}, {3}".format(self.g_num, self.switchName, self.status, self.major)

	def gpa(self):
		return self.qpoints/self.credits

	def isEnrolled(self):
		if self.enrolled == 'y':
			return True
		else:
			return False

	def status(self):
		if self.credits >= 90:
			return 'Senior'
		elif self.credits >= 60:
			return 'Junior'
		elif self.credits >= 30:
			return 'Sophmore'
		else:
			return 'Freshman'

	def setMajor(self, m):
		self.major = m
		return True

class Faculty(Person):
	specialties = ['teaching', 'research', 'administration', 'combination']
	def __init__(self, rank, active, teach_load, specialty = 'teaching', funding):
		self.rank = rank
		self.active = active
		self.teach_load = teach_load
		if specialty in specialties:
			self.specialty = specialty
		else
			print('Specialty not found. Default to teaching')
		self.funding = funding

#Global code
#creating Department containers
print('Creating Departments')
dep1 = Department('ENGR')
dep2 = Department('ARTS')
dep3 = Department('CHHS')
print('{0} \n{1} \n{2}'.format(dep1, dep2, dep3))
print('Done creating departments\n')

#creating Strudent objects
print('Creating Students')
s1 = Student(name = 'Fillmore, Sonia ', major = 'Math', enrolled = 'y', credits = 90, qpoints = 315)
s2 = Student(name = 'Riley, Chris ', major = 'IST', enrolled = 'y', credits = 78, qpoints = 260)
s3 = Student(name = 'Smith, John ', major = 'Physics', enrolled = 'y', credits = 34, qpoints = 100)
s4 = Student(name = 'Doe, John ', major = 'CSci', enrolled = 'y', credits = 12, qpoints = 36)
s5 = Student(name = 'Lamar, Kendrick ', major = 'Hist', enrolled = 'n', credits = 61, qpoints = 200)
s6 = Student(name = 'Ross, Bob', major = 'Math', enrolled = 'y', credits = 61, qpoints = 200)
s7 = Student(name = 'James, Rick', major = 'IST', enrolled = 'y', credits = 61, qpoints = 200)
s8 = Student(name = 'Bond, James', major = 'Hist', enrolled = 'y', credits = 90, qpoints = 200)
print('{0} \n{1} \n{2} \n{3} \n{4} \n{5} \n{6} \n{7}'.format(
	s1, s2, s3, s4, s5, s6, s7, s8))
print('Done creating students\n')

#filling Departments
print('Filling containers')
print('Adding s1 to dep1:', dep1.addStudent(s1))
print('Adding s2 to dep1:', dep1.addStudent(s2))
print('Adding s3 to dep1:', dep1.addStudent(s3))
print('Adding s4 to dep1:', dep1.addStudent(s4))
print('Attempting to add s1 to dep1 again: ', dep1.addStudent(s1))
print('Adding s5 to dep1:', dep1.addStudent(s5))
print('Attempting to add s1 to dep1 again: ', dep1.addStudent(s1))
print(dep1)
dep1.printRoster()
print('\n')

print('Adding s6 to dep2:', dep2.addStudent(s6))
print(dep2)
dep2.printRoster()
print('\n')

print('Adding s7 to dep3:', dep3.addStudent(s7))
print(dep3)
dep3.printRoster()
print('\nDone adding Students\n')

#causing rejections
print('Attempting to add s7 to dep1: ', dep1.addStudent(s7))
print('Attempting to add s8 to dep2: ', dep2.addStudent(s8))