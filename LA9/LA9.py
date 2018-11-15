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

	@property
	def job_title(self):
		return self.__job_title

	@job_title.setter
	def job_title(self, title):
		self.__job_title = title
		return True

	@property
	def salary(self):
		return self.__salary

	@salary.setter
	def salary(self, salary):
		self.__salary = salary
		return True

	def equalEmp(self, e):
		if type(e) == Employee and self.__name == e.__name and self.__empl_num == e.__empl_num:
			return True
		else:
			return False

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, n):
		self.__name = n
		return True

	@property
	def empl_num(self):
		return self.__empl_num

	@empl_num.setter
	def empl_num(self, e):
		self.__empl_num = e
		return True

	@property
	def birth_month(self):
		return self.__birth_month

	@birth_month.setter
	def birth_month(self, m):
		self.__birth_month = m
		return True

	@property
	def birth_year(self):
		return self.__birth_year

	@birth_year.setter
	def birth_year(self, y):
		self.__birth_year = y
		return True	

#global code
e1 = Employee('E34568', 'David Miller', 1960, 3)
e1.job_title = 'Accountant'
e1.salary = 65000
e2 = Employee('E22154', 'Margarete Smith', 1972, 10)
e2.job_title = 'Vice President'
e2.salary = 115000
e3 = Employee('E43344', 'Chase Smedley', 1982, 8) 
e3.job_title = 'Salesman'
e3.salary = 75000

print("Start of Employee class definition program")
print("e1 =" , e1)
print("e2 =" , e2)
print("e3 =" , e3)
print( e3.empl_num, e3.name, e3.salary, e3.birth_year, e3.birth_month)
e3.empl_num = 'E43345'
e3.name = 'Chuck Smith'
e3.salary = 1000000000
e3.birth_year = 1977
e3.birth_month = 12
print( e3.empl_num, e3.name, e3.salary, e3.birth_year, e3.birth_month)
print("e3 =" , e3)
print("End of Employee class definition program")