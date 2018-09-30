""" Chris Riley - IT209_A2.py
	Student object assignment
"""

class Student():
	"""Student object
		Passed variabes -- name, major, enrolled, credits, qpoints
		Calculated variables -- g_num, status, gpa, switchName
	"""
	majors = ["Acctg", "Art", "CSci", "Hist", "IST", "Math", "Physics"]
	totalEnrollment = 0
	def __init__(self, name, major='IST', enrolled='y', credits=0,qpoints=0):
		Student.totalEnrollment += 1
		self.g_num = "G{0:05d}".format(Student.totalEnrollment)
		self.name = name
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
		self.switchName = self.name.split(',')[1].strip()
		self.switchName = self.switchName + " " + self.name.split(',')[0].strip()
		
	def __str__(self):
		return "{0}, {1}, {2}, {3}, active: {4}, credits = {5}, gpa = {6:1.3}".format(self.switchName, 
			self.g_num, self.status, self.major, self.enrolled, self.credits, self.gpa)

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

	def sameStudent(self, s):
		if type(s) == Student and self.name == s.name and self.g_num == s.g_num:
			return True
		else:
			return False

	def setMajor(self, m):
		self.major = major
		return True

#Global Code

#creating Strudent objects
s1 =  Student('Fillmore, Sonia ', major = 'Math', enrolled = 'y', credits = 90, qpoints = 315)
s2 =  Student('Riley, Chris ', major = 'IST', enrolled = 'y', credits = 78, qpoints = 260)
s3 =  Student('Smith, John ', major = 'Physics', enrolled = 'y', credits = 34, qpoints = 100)
s4 =  Student('Doe, John ', major = 'CSci', enrolled = 'y', credits = 12, qpoints = 36)
s5 =  Student('Lamar, Kendrick ', major = 'Hist', enrolled = 'n', credits = 61, qpoints = 200)

#printing student list
print("Star of Student class definition program")
print("s1 = ",s1)
print("s2 = ",s2)
print("s3 = ",s3)
print("s4 = ",s4)
print("s5 = ",s5)
print("End of Student class definition program ")

#changing Student variables for comparison
print("Changing Student variables")
print('s3.name = "Fillmore, Sonia "')
print('s3.g_num = "G00001"')
s3.name = 'Fillmore, Sonia '
s3.g_num = 'G00001'
print("s1 == s3")
print(s1 == s3)
print("s1.sameStudent(s3)")
print(s1.sameStudent(s3))