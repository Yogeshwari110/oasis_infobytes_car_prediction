# -*- coding: utf-8 -*-
"""car prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vHDLT9ljxQ69oQYzTG8rs_yWGLfOf-po
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('/content/archive (2).zip')

X = data[['Selling_Price','Year']]  # Features
y = data['Present_Price']  # Target variabl

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

plt.figure(figsize=(10, 6))

plt.scatter(y_test, y_pred, color='blue', label='selling_price vs present_price')

plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linewidth=2, label='Perfect Prediction Line')

plt.xlabel('selling_price')
plt.ylabel('Present_Price')
plt.title('Car Price Prediction')
plt.legend()

# Show the plot
plt.show()