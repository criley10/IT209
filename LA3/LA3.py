import datetime

class Employee(object):
	"""Employee class 
	
		Variables: Employee number, Name, Birth year, Birth month, Job title, Salary
		Functions: __str___, hourly_rate, age, can_retire
	
	"""
	def __init__(self, empl_num, name, birth_year, birth_month):
		self.__empl_num = empl_num
		self.__name = name
		self.__birth_month = birth_month
		self.__birth_year = birth_year
		self.__job_title = None
		self.__salary = None

	def __str__(self):
		return  self.__name + ", " + self.__empl_num + ", " + self.__job_title + ", $" + str(self.__salary)
	
	def hourly_rate(self):
		return salary/2080 

	#uses datetime to get todays month and year to calculate age	
	def age(self):
		today = datetime.date.today()
		return today.year - self.__birth_year - (today.month < self.__birth_month)

	def can_retire(self):
		return self.age() > 65

	def setTitle(self, title):
		self.__job_title = title
		return True

	def setSalary(self, salary):
		self.__salary = salary
		return True

	def getTitle(self):
		return self.__job_title

	def getSalary(self):
		return self.__salary

	def equalEmp(self, e):
		if type(e) == Employee and self.__name == e.__name and self.__empl_num == e.__empl_num:
			return True
		else:
			return False
	def name(self, e):
		print(e.__name)

#global code
e1 = Employee('E34568', 'David Miller', 1960, 3)
e1.setTitle('Accountant')
e1.setSalary(65000)
e2 = Employee('E22154', 'Margarete Smith', 1972, 10)
e2.setTitle('Vice President')
e2.setSalary(115000)
e3 = Employee('E43344', 'Chase Smedley', 1982, 8) 
e3.setTitle('Salesman')
e3.setSalary(75000)
e4 = Employee('E12157', 'Daniel Arledge', 1952, 11) 
e4.setTitle('Lawyer')
e4.setSalary(92000)

print("Start of Employee class definition program")
print("e1 =" , e1)
print("e2 =" , e2)
print("e3 =" , e3)
print("e4 =" , e4)
print("End of Employee class definition program")