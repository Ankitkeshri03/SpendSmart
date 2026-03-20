import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

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

# ============================================
# 🔥 LOAD REAL-TIME DATABASE DATA
# ============================================
def load_transaction_data():
    import database

    debit_data = database.get_debit_record()

    if not debit_data:
        return None

    df = pd.DataFrame(
        debit_data,
        columns=["ID", "Date", "Amount", "Category", "Description"]
    )

    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.month

    pivot = df.pivot_table(
        index="Month",
        columns="Category",
        values="Amount",
        aggfunc="sum",
        fill_value=0
    )

    pivot.reset_index(inplace=True)

    return pivot


# ============================================
# 🔥 MERGE CSV + DB DATA
# ============================================
csv_data = pd.read_csv("historic_dataset1.csv")
db_data = load_transaction_data()

if db_data is not None:
    data = pd.concat([csv_data, db_data], ignore_index=True)
else:
    data = csv_data

data = data.fillna(0)


# ============================================
# 🔥 TRAIN MODELS + ACCURACY
# ============================================
models = {}
accuracy_scores = {}

for category in categories:

    df = data[["Month", category]].copy()

    for i in range(1, 7):
        df[f"Prev{i}"] = df[category].shift(i)

    df = df.dropna()

    X = df[["Month", "Prev1", "Prev2", "Prev3", "Prev4", "Prev5", "Prev6"]]
    y = df[category]

    split_index = int(len(X) * 0.8)

    X_train = X[:split_index]
    X_test = X[split_index:]

    y_train = y[:split_index]
    y_test = y[split_index:]

    model = RandomForestRegressor(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    models[category] = model
    accuracy_scores[category] = rmse


# ============================================
# 🔥 PRINT ACCURACY
# ============================================
print("\n📊 Model Accuracy (RMSE):")
for cat, score in accuracy_scores.items():
    print(f"{cat}: RMSE = {round(score, 2)}")


# ============================================
# 🔥 REAL-TIME RETRAIN FUNCTION (NEW 🔥)
# ============================================
def retrain_models():

    global data, models, accuracy_scores

    csv_data = pd.read_csv("historic_dataset1.csv")
    db_data = load_transaction_data()

    if db_data is not None:
        data = pd.concat([csv_data, db_data], ignore_index=True)
    else:
        data = csv_data

    data = data.fillna(0)

    models = {}
    accuracy_scores = {}

    for category in categories:

        df = data[["Month", category]].copy()

        for i in range(1, 7):
            df[f"Prev{i}"] = df[category].shift(i)

        df = df.dropna()

        X = df[["Month", "Prev1", "Prev2", "Prev3", "Prev4", "Prev5", "Prev6"]]
        y = df[category]

        split_index = int(len(X) * 0.8)

        X_train = X[:split_index]
        X_test = X[split_index:]

        y_train = y[:split_index]
        y_test = y[split_index:]

        model = RandomForestRegressor(
            n_estimators=200,
            random_state=42
        )

        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        models[category] = model
        accuracy_scores[category] = rmse


# ============================================
# 🔥 PREDICTION FUNCTION (UNCHANGED)
# ============================================
def predict_expenses_with_random_forest(month):

    predictions = {}
    total_expense = 0

    for category, model in models.items():

        # get last 6 months values
        prev_vals = [data[category].iloc[-i] for i in range(1, 7)]

        # prediction
        pred = model.predict([[month] + prev_vals])[0]

        pred = round(pred, 2)

        predictions[category] = pred
        total_expense += pred

    return predictions


# ============================================
# 💡 SMART BUDGET FUNCTION
# ============================================
def recommend_budget(predictions):

    budget = {}

    for category, value in predictions.items():

        if value > 5000:
            budget[category] = round(value * 0.85, 2)  # strict saving
        else:
            budget[category] = round(value * 0.95, 2)  # normal saving

    return budget
