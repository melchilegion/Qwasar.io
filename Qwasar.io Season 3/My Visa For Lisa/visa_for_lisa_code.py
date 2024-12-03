import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Visa_For_Lisa_Loan_Modelling.csv'
dataset = pd.read_csv(file_path)

# Data Cleaning (if necessary)
# Check for missing values
if dataset.isnull().sum().any():
    dataset.fillna(method='ffill', inplace=True)  # Forward fill for simplicity

# Feature Engineering: Create a new feature as an interaction between Income and CCAvg
dataset['Income_CCAvg'] = dataset['Income'] * dataset['CCAvg']

# Define features and target variable
features = ['Age', 'Experience', 'Income', 'Family', 'CCAvg', 'Education', 
            'Mortgage', 'Securities Account', 'CD Account', 'Online', 
            'CreditCard', 'Income_CCAvg']
target = 'Personal Loan'

# Split the dataset into training and testing sets
X = dataset[features]
y = dataset[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Feature Importance
coefficients = model.coef_
feature_importance = pd.DataFrame({'Feature': features, 'Coefficient': coefficients})
feature_importance.sort_values(by='Coefficient', ascending=False, inplace=True)

# Visualizations (optional, can be commented out in production)
plt.figure(figsize=(10, 6))
sns.barplot(x='Coefficient', y='Feature', data=feature_importance)
plt.title('Feature Importance in Loan Acceptance Prediction')
plt.xlabel('Coefficient Value')
plt.ylabel('Features')
plt.grid()
plt.show()

# Save the model (optional, if needed)
import joblib
joblib.dump(model, 'loan_acceptance_model.pkl')