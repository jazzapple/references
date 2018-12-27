# R code snippets

#-- Clear all variable assignments
	rm(list=ls())
	
#-- Data manipulation
	
	  # Initialise blank data frame with columns
	    base <- data.frame(matrix(data = NA, nrow = 0, ncol = 6), stringsAsFactors=FALSE)
		
    #	Name columns
		colnames(base)<- c("Suburb", "Address", "Type", "Price", "Result", "Agent")
   
	  # Select specific columns as a list
		fruit <- c(5, 10, 1, 20)
		names(fruit) <- c("orange", "banana", "apple", "peach")
		fruit[c("apple","orange")]
		# apple orange 
		# 1      5 

#--Data Preprocessing
		
		# Taking care of missing data
		# ave produces a single result per factor level and copies it to each position in the original data.
		# ave is handy for producing a new column in a data frame with summary data.
		dataset$Age = ifelse(is.na(dataset$Age),
		                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
		                     dataset$Age)
		
		# Encoding categorical data
		dataset$Country = factor(dataset$Country,
		                         levels = c('France', 'Spain', 'Germany'),
		                         labels = c(1, 2, 3)) #labels are abtirary and have no bearing on calculation
		
		# Splitting the dataset into the Training set and Test set
		# install.packages('caTools')
		library(caTools)
		set.seed(123) #generates same random result each run
		split = sample.split(dataset$DependentVariable, SplitRatio = 0.8) # true if training set, false if test set
		training_set = subset(dataset, split == TRUE)
		test_set = subset(dataset, split == FALSE)
		
		# Feature Scaling - Euclidian distance is skewed towards features with large range/values
		# Most R libraries do the feature scaling for you, so this step may not be neccesary
		
		# Standardise or Normalise: 
		  # x_stand = (x - mean(x)) / stddev(x)
		  # x_norm = (x-min(x)) / (max(x) - min(x))
		
		# scale function default argument, scale & centre = TRUE
		training_set[,2:3] = scale(training_set[,2:3]) # takes numeric input only so exclude features that are factors
		test_set[,2:3] = scale(test_set[,2:3])


#-- Simple linear regression	

# Linear regression package in R takes care of feature scaling, no need to do separately	
# Dummy variable trap - to avoid multicollinarity of independents, for a set of n dummy variables, only include n-1. 
	# The coefficient will take care of the last dummy variable. 
		
#-- Generating input
		# sequence of numbers
		seq(0, 1, 0.1)
		
#-- ggplot2 charts
		library(ggplot2)
		
		#scatter with line
		ggplot() +
		  geom_point(aes(x = dataset$Level, y = dataset$Salary),
		             colour = 'red') +
		  geom_line(aes(x = dataset$Level, y = predict(poly_reg, newdata = dataset)),
		            colour = 'blue') +
		  ggtitle('Truth or Bluff (Polynomial Regression)') +
		  xlab('Level') +
		  ylab('Salary')