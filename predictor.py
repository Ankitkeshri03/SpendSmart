
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






# # import pandas as pd
# # import numpy as np
# # from sklearn.ensemble import RandomForestRegressor
# # from sklearn.metrics import mean_squared_error
# # import numpy as np

# # # Load CSV file
# # data = pd.read_csv('historic_dataset1.csv')

# # # Define the categories
# # expense_categories = ["Utilities", "Groceries", "Food", "Transportation", "Stationary",
# #                       "Subscriptions", "Entertainment", "Medical_Expenses", "Phone/Internet_Bill"]

# # # Function to train a Random Forest regression model for a given expense category
# # def train_random_forest_model(category):
# #     # Extract features (months) and target variable (expense category)
# #     X = data['Month'].values.reshape(-1, 1)
# #     y = data[category].values
    
# #     # Initialize and fit the model
# #     model = RandomForestRegressor(n_estimators=100, random_state=42)
# #     model.fit(X, y)
    
# #     # Calculate training error (RMSE)
# #     y_pred = model.predict(X)
# #     mse = mean_squared_error(y, y_pred)
# #     rmse = np.sqrt(mse)
    
# #     return model, rmse

# # # Train Random Forest models for each expense category
# # random_forest_models = {}
# # for category in expense_categories:
# #     model, rmse = train_random_forest_model(category)
# #     random_forest_models[category] = {'model': model, 'rmse': rmse}

# # # Print the root mean squared error (RMSE) for each category
# # print("Random Forest Regression RMSE values:")
# # for category, info in random_forest_models.items():
# #     print(f"{category}: RMSE = {info['rmse']:.2f}")

# # # Initialize predicted_expenses dictionary
# # predicted_expenses = {}

# # # Function to predict expenses for each category for a given month and sum them up using Random Forest models
# # def predict_expenses_with_random_forest(month):
# #     total_expense = 0
# #     for category, info in random_forest_models.items():
# #         model = info['model']
# #         predicted_expense = model.predict(np.array([[month]]))[0]
# #         predicted_expense = round(predicted_expense, 2) 
# #         predicted_expenses[category] = predicted_expense
# #         total_expense += predicted_expense
# #         print(f"{category}: ${predicted_expense:.2f}")
# #     print(f"Total Expense for Month {month}: ${total_expense:.2f}")
    
# #     return predicted_expenses


# # CORRECT
# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor
# import database

# # Categories used in the project
# categories = [
#     "Utilities",
#     "Groceries",
#     "Food",
#     "Transportation",
#     "Stationary",
#     "Subscriptions",
#     "Entertainment",
#     "Medical_Expenses",
#     "Phone/Internet_Bill"
# ]


# # ============================================
# # LOAD CSV DATASET
# # ============================================
# # `ython``p
# def load_csv_dataset():

#     try:
#         # Load real dataset
#         real_data = pd.read_csv("historic_dataset1.csv")

#         # Load synthetic dataset
#         synthetic_data = pd.read_csv("synthetic_expense_dataset.csv")

#         # Merge datasets
#         data = pd.concat([real_data, synthetic_data], ignore_index=True)

#         # Shuffle rows (better training)
#         data = data.sample(frac=1, random_state=42).reset_index(drop=True)

#         return data

#     except:
#         return None


# # ============================================
# # LOAD DATABASE TRANSACTIONS
# # ============================================
# def load_transaction_data():

#     debit_data = database.get_debit_record()

#     if not debit_data:
#         return None

#     df = pd.DataFrame(
#         debit_data,
#         columns=["ID", "Date", "Amount", "Category", "Description"]
#     )

#     df["Date"] = pd.to_datetime(df["Date"])
#     df["Month"] = df["Date"].dt.month

#     pivot = df.pivot_table(
#         index="Month",
#         columns="Category",
#         values="Amount",
#         aggfunc="sum",
#         fill_value=0
#     )

#     pivot.reset_index(inplace=True)

#     for cat in categories:
#         if cat not in pivot.columns:
#             pivot[cat] = 0

#     pivot = pivot[["Month"] + categories]

#     return pivot


# # ============================================
# # MERGE CSV + DATABASE DATA
# # ============================================
# def prepare_training_data():

#     csv_data = load_csv_dataset()
#     db_data = load_transaction_data()

#     if csv_data is None and db_data is None:
#         return None

#     if csv_data is None:
#         return db_data

#     if db_data is None:
#         return csv_data

#     combined = pd.concat([csv_data, db_data], ignore_index=True)

#     return combined


# # ============================================
# # TRAIN RANDOM FOREST MODELS
# # ============================================
# def train_models(data):

#     models = {}

#     X = data[["Month"]]

#     for category in categories:

#         y = data[category]

#         model = RandomForestRegressor(
#             n_estimators=200,
#             random_state=42
#         )

#         model.fit(X, y)

#         models[category] = model

#     return models


# # ============================================
# # PREDICT EXPENSES
# # ============================================
# def predict_expenses_with_random_forest(month):

#     dataset = prepare_training_data()

#     if dataset is None:
#         return {cat: 0 for cat in categories}

#     models = train_models(dataset)

#     predictions = {}

#     for category, model in models.items():

#         pred = model.predict([[month]])[0]

#         predictions[category] = round(pred, 2)

#     return predictions


# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor

# # Categories
# categories = [
#     "Utilities",
#     "Groceries",
#     "Food",
#     "Transportation",
#     "Stationary",
#     "Subscriptions",
#     "Entertainment",
#     "Medical_Expenses",
#     "Phone/Internet_Bill"
# ]

# # Load dataset
# data = pd.read_csv("historic_dataset1.csv")

# models = {}

# # Train model for each category
# for category in categories:

#     df = data[["Month", category]].copy()

#     # Create lag features
#     df["Prev1"] = df[category].shift(1)
#     df["Prev2"] = df[category].shift(2)
#     df["Prev3"] = df[category].shift(3)

#     df = df.dropna()

#     X = df[["Prev1", "Prev2", "Prev3"]]
#     y = df[category]

#     model = RandomForestRegressor(
#         n_estimators=200,
#         random_state=42
#     )

#     model.fit(X, y)

#     models[category] = model


# def predict_next_month():

#     predictions = {}

#     for category in categories:

#         prev1 = data[category].iloc[-1]
#         prev2 = data[category].iloc[-2]
#         prev3 = data[category].iloc[-3]

#         pred = models[category].predict([[prev1, prev2, prev3]])[0]

#         predictions[category] = round(pred, 2)

#     total = sum(predictions.values())

#     return predictions, round(total, 2)


# ```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

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

data = pd.read_csv("historic_dataset1.csv")

models = {}

for category in categories:

    df = data[["Month", category]].copy()

    df["Prev1"] = df[category].shift(1)
    df["Prev2"] = df[category].shift(2)
    df["Prev3"] = df[category].shift(3)

    df = df.dropna()

    X = df[["Month", "Prev1", "Prev2", "Prev3"]]
    y = df[category]

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X, y)

    models[category] = model


def predict_expenses_with_random_forest(month):
    total_expense = 0
    for category, info in random_forest_models.items():
        model = info['model']
        predicted_expense = model.predict(np.array([[month]]))[0]
        predicted_expense = round(predicted_expense, 2) 
        predicted_expenses[category] = predicted_expense
        total_expense += predicted_expense
        print(f"{category}: ${predicted_expense:.2f}")
    print(f"Total Expense for Month {month}: ${total_expense:.2f}")
    
    return predicted_expenses
