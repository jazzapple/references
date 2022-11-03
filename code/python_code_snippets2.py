
############################
# Setup
############################
#%%
# Extension reloads
%load_ext autoreload
%autoreload 2

# Display options
pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.options.display.max_colwidth = None
pd.set_option('display.html.use_mathjax', False)

# Suppress scientific notation
pd.options.display.float_format = '{:.2f}'.format
np.set_printoptions(suppress=True)

#%%


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

# list functions within a module
	dir(module)
	
# help on a module's functions
	help(module.function)
	
# OOP
	# methods are run on objects
	b = 'yay'
	b.lower()
	# where b is the object and lower is the method
	
# string value substitution
	'hey %s i hve %d cats' %('sam',3)
	#'hey sam i hve 3 cats'
	
# slice - upper bound is not included
	a='hello'
	a[1:3]
	#'el'
	
	a[1:]
	#'ello'
	
	a[:]
	#'hello'
	
	a[:1]
	#h
	
	a[:1]+a[1:]
	#'hello'
	
	a[-3:]
	#'llo'

############################
# Tuples
############################

# Swapping values
a = 'jelly'
b = 'bean'
a, b = b, a
print(a, b)
>>> 'bean', 'jelly'

# Combinig weather and temp into single listof tuples
features=zip(weather_encoded,temp_encoded)


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

############################
# Input / Output
############################

# Create a list to write to a file
my_list = [i ** 2 for i in range(1, 11)]

# Write to file
# Use a file handler to open a file for writing
my_file = open('output.txt', 'w')  # Declare variable. w: write, r: read-only, r+: read and write, a: append

for line in my_list:
    my_file.write(str(line)+'\n') # separate by new line

my_file.close()
 
# Read from file
my_file = open('output.txt', 'r')
print(my_file.read())
my_file.close()

# Read line by line
my_file = open('output.txt', 'r')

print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

my_file.close()

# Write with auto closing
with open('output.txt', 'w') as my_file:
    my_file.write('ss')
	
# Read with auto closing
with open('output.txt', 'r') as my_file:
   print(my_file.read())
	
# check if file is closed
my_file.closed # returns True or False

############################
# Data Pre-processing
############################

# Check for any missing values
df.isnull().sum()

# Exclude a column by name using columns attribute
df.loc[:, df.columns != 'PassengerID']

############################
# Visualisations
############################

import matplotlib.pyplot as plt 
import seaborn as sns 
%matplotlib inline

# Histogram percentile
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.distplot(df['MEDV'], bins=30)
plt.show()

# Plot correlations between features
correlation_matrix = df.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True) # annot = True to print the values inside the square

# Plot scatter plot of target vs features
plt.figure(figsize=(20, 5))

features = ['LSTAT', 'RM']
target = boston['MEDV']

for i, col in enumerate(features):
    plt.subplot(1, len(features) , i+1)
    x = boston[col]
    y = target
    plt.scatter(x, y, marker='o')
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel('MEDV')
	
# Pair plots coluoured by target
sns.pairplot(processed, hue='Survived', vars=['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_num', 'Embarked_num'])

# Correlation matrix
def plotCorrelationMatrix(df, graphWidth):    
    df = df.dropna('columns') # drop columns with NaN
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
    corrMat = plt.matshow(corr, fignum = 1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Correlation Matrix', fontsize=15)
    plt.show()
    

# Distribution graphs (histogram/bar graph) of column data
def plotPerColumnDistribution(df, nGraphShown, nGraphPerRow):
    """
    Bar chart for categorical, historgram for numeric
    """
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]] # For displaying purposes, pick columns that have between 1 and 50 unique values
    nRow, nCol = df.shape
    columnNames = list(df)
    nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
    plt.figure(num = None, figsize = (6 * nGraphPerRow, 8 * nGraphRow), dpi = 80, facecolor = 'w', edgecolor = 'k')
    for i in range(min(nCol, nGraphShown)):
        if nGraphRow <2: # too few columns with reasonable number of unique values
            plt.subplot(2, 2, i + 1)
        else:
            plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation = 90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad = 1.0, w_pad = 1.0, h_pad = 1.0)
    plt.show()
    
    
# Scatter and density plots
def plotScatterMatrix(df, plotSize=20, textSize=10):
    """
    Numeric columns only
    """
    df = df.select_dtypes(include =[np.number]) # keep only numerical columns
    # Remove rows and columns that would lead to df being singular
    df = df.dropna('columns')
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    columnNames = list(df)
    if len(columnNames) > 10: # reduce the number of columns for matrix inversion of kernel density plots
        columnNames = columnNames[:10]
    df = df[columnNames]
    ax = pd.plotting.scatter_matrix(df, alpha=0.75, figsize=[plotSize, plotSize], diagonal='kde')
    corrs = df.corr().values
    for i, j in zip(*plt.np.triu_indices_from(ax, k = 1)):
        ax[i, j].annotate('Corr. coef = %.3f' % corrs[i, j], (0.8, 0.2), xycoords='axes fraction', ha='center', va='center', size=textSize)
    plt.suptitle('Scatter and Density Plot')
    plt.show() 

##############
# Arrays
##############

# Load library
import numpy as np

# Create row vector
vector = np.array([1, 2, 3, 4, 5, 6])

# Create column vector
vector_col = np.array([[1],
                       [2],
                       [3],
                       [4],
                       [5],
                       [6]])

# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Select third element of vector
vector[2]

# Reshape allows us to restructure an array with same data but it is organized as a different number of rows and columns. 
# -1 argument effectively means “as many as needed,” so reshape(-1, 1) means one row and as many columns as needed:
matrix.reshape(1, -1)

# Concatenate columns for arrays
# how does np.c_[] work? 
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
print('a:', a)
print('\nb:', b)
print('\nnp.c_[a,b]:\n ',np.c_[a, b])

##############
# Anaconda
##############
* Cheat sheet: https://kapeli.com/cheat_sheets/Conda.docset/Contents/Resources/Documents/index