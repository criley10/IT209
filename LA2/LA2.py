import datetime

class Employee(object):
	"""Employee class 
	
		Variables: Employee number, Name, Birth year, Birth month, Job title, Salary
		Functions: __str___, hourly_rate, age, can_retire
	
	"""
	def __init__(self, empl_num, name, birth_year, birth_month, job_title, salary):
		self.empl_num = empl_num
		self.name = name
		self.birth_month = birth_month
		self.birth_year = birth_year
		self.job_title = job_title
		self.salary = salary

	def __str__(self):
		return  self.name + ", " + self.empl_num + ", " + self.job_title + ", $" + str(self.salary)
	
	def hourly_rate(self):
		return salary/2080 

	#uses datetime to get todays month and year to calculate age	
	def age(self):
		today = datetime.date.today()
		return today.year - self.birth_year - (today.month < self.birth_month)

	def can_retire(self):
		return self.age() > 65

#global code
e1 = Employee('E34568', 'David Miller', 1960, 3, 'Accountant', 65000)
e2 = Employee('E22154', 'Margarete Smith', 1972, 10, 'Vice President', 115000)
e3 = Employee('E43344', 'Chase Smedley', 1982, 8, 'Salesman', 75000) 
e4 = Employee('E12157', 'Daniel Arledge', 1952, 11, 'Lawyer', 92000) 

print("Start of Employee class definition program")
print("e1 =" , e1)
print("e2 =" , e2)
print("e3 =" , e3)
print("e4 =" , e4)
print("End of Employee class definition program")