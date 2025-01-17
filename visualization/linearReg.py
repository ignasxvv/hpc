import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# x from 0 to 30
x = 30 * np.random.random((20, 1)) # 20 floating point numbers between 0.0 to 1.0 - 1D 

# y = a*x + b with noise
y = 0.5 * x + 1.0 + np.random.normal(size=x.shape) # Normal Gaussian Distribution



# create a linear regression model
model = LinearRegression()
model.fit(x, y) 

# predict y from the data
x_new = np.linspace(0, 30, 100) # starting value of the sequece, the end value of the sequence,number of samples to generate
y_new = model.predict(x_new[:, np.newaxis])

# plot the results
plt.figure(figsize=(4, 3))
ax = plt.axes()
ax.scatter(x, y)
ax.plot(x_new, y_new) # Plot the Regression line

ax.set_xlabel('x')
ax.set_ylabel('y')

ax.axis('tight')


plt.show()
