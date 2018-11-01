# Simple Linear Regression from scratch
Simple linear regression takes continous data and tries to fit the best fit line.
Linear regression works best on data that has a linear correlation to it. If the data does not contain any correlation , linear regression might not be the best algorithm to use.

Let's start with the definition of a straight line:
### y = m * x + b
This gives us the best fit line for the data.
###  m = ((mean(X)*mean(y))-(mean(X*y)))/((mean(X)**2)-(mean(X**2)))
###  b = b = mean(y)-(m * mean(X))

These are pretty much all the formulas required for a simple linear regression

#### But how do we know how good the best fit line is? Or on a more broader scale, how do we know if linear regression is the best algorithm for this dataset?
Introducing Coefficient of Determination which is calculated using squared error
### r^2 = 1 - S.E(y_hat) / S.E(y_mean)

Hints:
* If r^2 is close to 1, then it's a pretty good best fit line
* If r^2 is close to 0, then there is probably no correlation in your dataset

There you have it folks, your very first ML Algorithm and it couldn't be simpler.
Check out the scikit-learn equivalent of this algorithm in the Machine-Learning-using-scikitlearn repository.
