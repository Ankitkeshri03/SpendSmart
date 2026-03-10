
# import pandas as pd
# import numpy as np
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error
# import numpy as np

# # Load CSV file
# data = pd.read_csv('historic_dataset1.csv')

# # Define the categories
# expense_categories = ["Utilities", "Groceries", "Food", "Transportation", "Stationary",
#                       "Subscriptions", "Entertainment", "Medical_Expenses", "Phone/Internet_Bill"]

# # Function to train a Random Forest regression model for a given expense category
# def train_random_forest_model(category):
#     # Extract features (months) and target variable (expense category)
#     X = data['Month'].values.reshape(-1, 1)
#     y = data[category].values
    
#     # Initialize and fit the model
#     model = RandomForestRegressor(n_estimators=100, random_state=42)
#     model.fit(X, y)
    
#     # Calculate training error (RMSE)
#     y_pred = model.predict(X)
#     mse = mean_squared_error(y, y_pred)
#     rmse = np.sqrt(mse)
    
#     return model, rmse

# # Train Random Forest models for each expense category
# random_forest_models = {}
# for category in expense_categories:
#     model, rmse = train_random_forest_model(category)
#     random_forest_models[category] = {'model': model, 'rmse': rmse}

# # Print the root mean squared error (RMSE) for each category
# print("Random Forest Regression RMSE values:")
# for category, info in random_forest_models.items():
#     print(f"{category}: RMSE = {info['rmse']:.2f}")

# # Initialize predicted_expenses dictionary
# predicted_expenses = {}

# # Function to predict expenses for each category for a given month and sum them up using Random Forest models
# def predict_expenses_with_random_forest(month):
#     total_expense = 0
#     for category, info in random_forest_models.items():
#         model = info['model']
#         predicted_expense = model.predict(np.array([[month]]))[0]
#         predicted_expense = round(predicted_expense, 2) 
#         predicted_expenses[category] = predicted_expense
#         total_expense += predicted_expense
#         print(f"{category}: ${predicted_expense:.2f}")
#     print(f"Total Expense for Month {month}: ${total_expense:.2f}")
    
#     return predicted_expenses






import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Categories
categories = [
    "Utilities",
    "Groceries",
    "Food",
    "Transportation",
    "Stationary",
    "Subscriptions",
    "Entertainment",
    "Medical_Expenses",
    "Phone/Internet_Bill"
]

# Load dataset
data = pd.read_csv("historic_dataset1.csv")

models = {}

# Train model for each category using lag features
for category in categories:

    df = data[["Month", category]].copy()

    df["Prev1"] = df[category].shift(1)
    df["Prev2"] = df[category].shift(2)
    df["Prev3"] = df[category].shift(3)

    df = df.dropna()

    X = df[["Prev1", "Prev2", "Prev3"]]
    y = df[category]

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X, y)

    models[category] = model


def predict_expenses_with_random_forest(month):

    predictions = {}

    for category in categories:

        prev1 = data[category].iloc[-1]
        prev2 = data[category].iloc[-2]
        prev3 = data[category].iloc[-3]

        pred = models[category].predict([[prev1, prev2, prev3]])[0]

        predictions[category] = round(pred, 2)

    return predictions

