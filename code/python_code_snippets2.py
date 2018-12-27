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

