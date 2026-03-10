💰 SpendSmart – AI Powered Expense Tracker

SpendSmart is a personal finance management web application that helps users track their expenses, manage income, visualize spending habits, and predict future expenses using Machine Learning.

The application is built using Python, Streamlit, SQLite, and Random Forest Regression to provide an interactive and intelligent financial dashboard.

🚀 Features
1️⃣ Transaction Management

1.Add Debit (Expenses) and Credit (Income) transactions

2.Categorize expenses such as:

3.Utilities

4.Groceries

5.Food

6.Transportation

7.Entertainment

8.Medical Expenses

9.Subscriptions

10.Edit or delete transactions easily.

2️⃣ Personal Finance Dashboard

1.Set your monthly salary

2.Automatically calculate:

3.Total income

4.Total expenses

5.Remaining balance

6.Budget alerts when spending exceeds limits.

3️⃣ Expense Prediction (Machine Learning)

SpendSmart predicts future expenses using a Random Forest Regression model.

The model:

Uses historical expense data

Uses previous months' spending patterns

Predicts category-wise expenses for the selected month.

The model is implemented in predictor.py using Scikit-learn RandomForestRegressor. 

predictor

4️⃣ Financial Data Visualization

Users can visualize their financial behavior using:

Bar Charts (Expenses by Category)

Pie Charts (Expense Distribution)

Monthly Income Trends

Visualizations are generated using Streamlit and Plotly.

5️⃣ Transaction History

View a complete table of all transactions including:

Transaction ID

Date

Amount

Category

Description


| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core Programming Language |
| Streamlit    | Web Application UI        |
| SQLite       | Database                  |
| Pandas       | Data Processing           |
| Scikit-Learn | Machine Learning          |
| Plotly       | Data Visualization        |
| NumPy        | Numerical Computation     |


Deployed ; - https://spendsmart-sbub6qzbnmrlndypzhidbp.streamlit.app/
