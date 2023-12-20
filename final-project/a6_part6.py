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
coef = np.around(model.coef_, 2)[0]
intercept = round(float(model.intercept_), 2)
r_squared = round(model.score(xtrain, ytrain), 2)

# Testing Results
print("***************")
print("Testing Results:")
predict = model.predict(xtest)
predict = np.around(predict, 2)

for index in range(len(xtest)):
    actual = ytest[index]
    predicted_y = predict[index]
    x_coord = xtest[index]
    print(f"""
    ----- Result {index} -----
    - Fixed Acidity: {x_coord[0]}
    - Volatile Acidity: {x_coord[1]}
    - Citric Acid: {x_coord[2]}
    - Residual Sugar:{x_coord[3]}
    - Chlorides: {x_coord[4]}
    - Free Sulfure Dioxide: {x_coord[5]}
    - Total Sulfur Dioxide: {x_coord[6]}
    - Density: {x_coord[7]}
    - pH: {x_coord[8]}
    - Sulphates: {x_coord[9]}
    - Alcohol: {x_coord[10]}
    - Actual: {actual[0]}
    - Predicted: {predicted_y[0]}
    ----- ------- -----
    """)

print(f"Model's Linear Equation: y = {coef[0]}x1 + {coef[1]}x2 + {coef[2]}x3 + {coef[3]}x4 + {coef[4]}x5 + {coef[5]}x6 + {coef[6]}x7 + {coef[7]}x8 + {coef[8]}x8 + {coef[9]}x8 + {coef[10]}x8 + {intercept}")
print("R Squared value:", r_squared)
