#Simple Linear Regression
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

style.use('fivethirtyeight')

#create a simple dataset
#You could change the values to create different datasets
number_of_datapoints = 100
variance = 100
step = 2
correlation = 'pos'

value = 1
y = []

for i in range(number_of_datapoints):
    ys = value + random.randrange(-variance,variance)
    y.append(ys)
    if correlation == 'pos':
        value = value + step
    if correlation == 'neg':
        value = value - step
X  = [i for i in range(number_of_datapoints)]

#convert the lists into arrays
y = np.array(y,dtype = np.float64)
X = np.array(X, dtype = np.float64)

#calculate m
def calc_slope(X,y):
    m = ((mean(X)*mean(y))-(mean(X*y)))/((mean(X)**2)-(mean(X**2)))
    return m

#calculate b
def calc_y_intercept(m,X,y):
    b = mean(y)-(m * mean(X))
    return b

#Squared error is required to find coefficient of determination
def squared_error(y,y_line):
    return (sum((y_line - y)**2))

#coefficient of determination determines whether the best fit line is a good line for the dataset
def coefficient_of_determination(y,y_line):
    y_mean_line = [mean(y) for ys in y]
    SE_regr = squared_error(y,y_line)
    SE_y_mean = squared_error(y,y_mean_line)
    return 1 - (SE_regr/SE_y_mean)

# calculate y = m * x + b
m = calc_slope(X,y)
b = calc_y_intercept(m,X,y)

regression_line = []
for x in X:
    regression_line.append((m * x) + b)

#Coefficient of determination
r_squared = coefficient_of_determination(y,regression_line)
print(r_squared)

#Make predictions
predict_y = []
predict_x = [7,8,10,6]
for x in predict_x:
    predict_y.append((m * x) + b)

#Visualising the simple linear regression
plt.scatter(X, y, label = 'data',color = 'pink')
plt.scatter(predict_x, predict_y, color = 'blue', label = 'prediction')
plt.plot(X,regression_line, color = 'purple', label = 'regression line')
plt.legend(loc = 4)
plt.show()
