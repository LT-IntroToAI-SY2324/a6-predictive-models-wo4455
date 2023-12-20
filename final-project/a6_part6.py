import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo 
import matplotlib.pyplot as plt

# fetch dataset 
wine_quality = fetch_ucirepo(id=186) 
  
# data (as pandas dataframes) 
x = wine_quality.data.features.values
y = wine_quality.data.targets.values

# Split the data into training and testing sets
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

# Create and fit the linear regression model
model = LinearRegression().fit(xtrain, ytrain)

# Get the coefficients, intercept, and R-squared values
coef = np.around(model.coef_, 2)
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(xtrain, ytrain), 2)

print(f"Model's Linear Equation: y = {coef[0]}x + {intercept}")
print("R Squared value:", r_squared)

# Testing Results
print("***************")
print("Testing Results:")
predict = model.predict(xtest)
predict = np.around(predict, 2)

for index in range(len(xtest)):
    actual = ytest[index]
    predicted_y = predict[index]
    x_coord = xtest[index]

    print(f"Actual: {actual} Predicted: {predicted_y}")

plt.figure(figsize=(6,4))
plt.scatter(x,y, c="blue")
plt.scatter(x_coord, predicted_y, c="orange")
plt.title("Wine Quality")
plt.xlabel("Wine Quality")
plt.ylabel("Score")
plt.plot(x, coef * x + intercept, c="r", label="Line of Best Fit")
plt.legend()
plt.show()
