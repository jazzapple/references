############################
# Packages
############################

# Importing a function means you don't have to reference the module when using the function
from module import function

from math import sqrt
print(sqrt(25))

# Inspect module 
dir(module)

############################
# Operations
############################

# Update variable value
sandwich_price = 7.50
sales_tax = .08 * sandwich_price
sandwich_price += sales_tax # shorthand for sandwich_price = sandwhich_price + sales_tax

############################
# Data Types
############################

# Type conversions
str()
int()
float()

# str(): Incorporate values/variables into strings via Concatenation with str()
age = 13
print("I am " + str(age) + " years old!")

# Format strings: Incorporate variables into strings via format strings. The % operator will replace the %s in the string with the string variable that comes after it.
string_1 = "Camelot"
string_2 = "place"
print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

# Format strings: Incorporate integer variables into strings via format strings. Pad with leading zeros if desired
print("03 - %02d - 2019" % (day))
# 03 - 06 - 2019	

############################
# Dates
############################

from datetime import datetime

# current datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day
now.hour
now.minute
now.second

# date formatting dd-mm-yyyy
print('%02d-%02d-%04d' % (now.day, now.month, now.year))

############################
# Command line execution
############################

# User input program: AreaCalculator.py
"""Input: shape; T for triangle, C for Circle
Returns: area"""

print('Starting calculator...')

option = raw_input("Enter C for Circle or T for triangle: ").upper()

if option=='C': 
  radius = float(raw_input("Enter radius: "))
  area = 3.1459*radius**2
  print("Area equals %s" % area)
  
elif option=='T':
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = base*height/2
  print("Area equals %s" % area)

else:
  print("Invalid input")

print("Exiting calculator...")

############################
# Classes
############################

class Car(object):
	# member variables can be created within the class (e.g. condition) or when initialising an object/instance of the class (e.g. model)
	condition = "new"

	def __init__(self, model, color, mpg):
		self.model = model
		self.color = color
		self.mpg   = mpg
	
	# class methods are like functions but are defined within the class definition. "self" must be provided as the first argument of any class method
	def display_car(self):
		print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

	# class methods can be used to change member variable values
	def drive_car(self):
		self.condition = "used"
		return self.condition
	
# create object my_car as an instance of the Car class		
my_car = Car("DeLorean", "silver", 88)

# print member variables
print my_car.condition
print my_car.model
print my_car.color
print my_car.mpg

# call Car class method, display_car
my_car.display_car()

# call Car class method, drive_car and see how it changes the value of condition from "new" to "used"
print(my_car.condition)
my_car.drive_car()
print(my_car.condition)
