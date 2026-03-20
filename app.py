
import streamlit as st
import pandas as pd
from datetime import datetime
import sqlite3
import database
import predictor
import plotly.graph_objects as go
import nlp_model


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SpendSmart",
    page_icon="💰",
    layout="wide"
)

st.title("💰 SpendSmart")

# ---------------- DATABASE FOR SALARY ----------------
conn = sqlite3.connect("transactions.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS monthly_salary(
month TEXT PRIMARY KEY,
salary REAL
)
""")
conn.commit()

# ---------------- SIDEBAR ----------------
st.sidebar.subheader("Welcome!")

nv = st.sidebar.selectbox(
    "Navigator",
    [
        "About",
        "Home",
        "Add Transactions",
        "Edit/Delete Transactions",
        "History",
        "Expense Predictor",
        "Visual Representations"
    ],
)

# =========================================================
# ABOUT
# =========================================================
if nv == "About":

    st.header("ℹ️ About SpendSmart")

    st.subheader("Welcome to SpendSmart")
    st.write("SpendSmart is your personal finance management tool.")
    st.write("Here's what you can do:")

    st.markdown("- **Add Transactions:** Record your expenses and incomes.")
    st.markdown("- **View Transaction History:** Review your past transactions.")
    st.markdown("- **Expense Predictor:** Get insights and predictions about your future expenses.")
    st.markdown("- **Visual Representations:** View charts and graphs representing your financial data.")

    st.write("Use the navigation panel on the left to get started.")

    st.subheader("Tips for Effective Financial Management")

    st.markdown("- **Budgeting:** Set financial goals and create a budget.")
    st.markdown("- **Tracking Expenses:** Monitor your spending habits.")
    st.markdown("- **Saving:** Build an emergency fund.")
    st.markdown("- **Investing:** Grow wealth through investments.")
    st.markdown("- **Reviewing:** Regularly review financial status.")

    st.subheader("Why Choose SpendSmart?")

    st.markdown("- **User-Friendly:** Simple and intuitive interface.")
    st.markdown("- **Customizable:** Adaptable to your financial needs.")
    st.markdown("- **Insightful:** Understand your spending patterns.")
    st.markdown("- **Secure:** Your financial data is securely stored.")

# =========================================================
# HOME DASHBOARD
# =========================================================
elif nv == "Home":

    st.header("📊 Personal Finance Dashboard")

    st.image(
        "https://images.unsplash.com/photo-1554224155-6726b3ff858f",
        caption="Take control of your finances",
        use_container_width=True
    )

    st.markdown(
        """
        ### 💡 Smart Money Management Starts Here
        Track expenses, manage your budget, and predict future spending with **SpendSmart**.
        """
    )

    current_month = datetime.now().strftime("%Y-%m")

    # Retrieve stored salary
    cursor.execute(
        "SELECT salary FROM monthly_salary WHERE month=?",
        (current_month,)
    )

    result = cursor.fetchone()

    default_salary = result[0] if result else 0

    salary = st.number_input(
        "Set Monthly Salary",
        value=float(default_salary),
        step=1000.0
    )

    if st.button("Save Salary"):

        cursor.execute(
            "INSERT OR REPLACE INTO monthly_salary(month,salary) VALUES(?,?)",
            (current_month, salary)
        )

        conn.commit()
        st.success("Salary saved successfully")

    debit_data = database.get_debit_record()
    credit_data = database.get_credit_record()

    total_expense = 0
    total_income = 0

    if debit_data:
        df = pd.DataFrame(
            debit_data,
            columns=["ID","Date","Amount","Category","Description"]
        )

        df["Date"] = pd.to_datetime(df["Date"])

        month_df = df[df["Date"].dt.strftime("%Y-%m") == current_month]

        total_expense = month_df["Amount"].sum()

    if credit_data:
        df = pd.DataFrame(
            credit_data,
            columns=["ID","Date","Amount","Category","Description"]
        )

        df["Date"] = pd.to_datetime(df["Date"])

        month_df = df[df["Date"].dt.strftime("%Y-%m") == current_month]

        total_income = month_df["Amount"].sum()

    remaining = salary + total_income - total_expense

    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Total Income", f"₹{salary + total_income:.2f}")
    col2.metric("💳 Total Expenses", f"₹{total_expense:.2f}")
    col3.metric("💵 Remaining Balance", f"₹{remaining:.2f}")

    if remaining < 0:
        st.error("⚠️ You exceeded your budget!")
    elif remaining < salary * 0.2:
        st.warning("⚠️ Budget almost finished")
    else:
        st.success("✅ Budget under control")

# =========================================================
# ADD TRANSACTIONS
# =========================================================
elif nv == "Add Transactions":

    st.header("➕ Add Transaction")

    tran_type = st.radio("Transaction Type", ["Debit","Credit"])

    if tran_type == "Debit":

        with st.form("debit_form"):

            date = st.date_input("Date")

            description = st.text_area("Description")

            # 🔥 NLP AUTO CATEGORY
            categories = [
                "Utilities","Groceries","Food","Transportation",
                "Stationary","Subscriptions","Entertainment",
                "Medical_Expenses","Phone/Internet_Bill"
            ]

            if description:
                try:
                    predicted_cat = nlp_model.predict_category(description)
                    st.success(f"Auto Category: {predicted_cat}")

                    # allow user to change (better UX)
                    category = st.selectbox(
                        "Category",
                        categories,
                        index=categories.index(predicted_cat)
                    )
                except:
                    category = st.selectbox("Category", categories)
            else:
                category = st.selectbox("Category", categories)

            amount = st.number_input("Amount", min_value=0.01)

            submit = st.form_submit_button("Add Expense")

        if submit:
            database.add_debit(date, amount, category, description)
            predictor.retrain_models()
            st.success("Expense added & model updated!")

    else:

        with st.form("credit_form"):

            date = st.date_input("Date")

            category = st.selectbox(
                "Category",
                ["Salary","Sale","Lottery","Bank_Interest","Rent_Received"]
            )

            amount = st.number_input("Amount",min_value=0.01)
            description = st.text_area("Description")

            submit = st.form_submit_button("Add Income")

        if submit:
            database.add_credit(date,amount,category,description)
            predictor.retrain_models()

            st.success("Income added & model updated!")

# =========================================================
# EDIT / DELETE
# =========================================================
elif nv == "Edit/Delete Transactions":

    st.header("✏️ Edit or Delete Transaction")

    option = st.radio("Function Type",["Edit","Delete"])
    tran_type = st.radio("Transaction Type",["Debit","Credit"])

    transaction_id = st.number_input("Enter Transaction ID",step=1)

    transaction = None

    if tran_type == "Debit":
        transaction = database.get_debit_tran_id(transaction_id)
    else:
        transaction = database.get_credit_tran_id(transaction_id)

    if transaction:

        st.subheader("Transaction Details")

        st.write(f"Date: {transaction[1]}")
        st.write(f"Amount: ₹{transaction[2]}")
        st.write(f"Category: {transaction[3]}")
        st.write(f"Description: {transaction[4]}")
        st.write(f"Type: {tran_type}")

        if option == "Edit":

            with st.form("edit_form"):

                date = st.date_input("Date",pd.to_datetime(transaction[1]))
                amount = st.number_input("Amount",value=float(transaction[2]))
                description = st.text_area("Description",value=transaction[4])

                submit = st.form_submit_button("Update")

            if submit:

                if tran_type == "Debit":
                    database.update_debit(transaction_id,date,transaction[3],amount,description)
                else:
                    database.update_credit(transaction_id,date,transaction[3],amount,description)

                st.success("Transaction updated")

        else:

            confirm = st.checkbox("Confirm delete")

            if confirm:

                if st.button("Delete Transaction"):

                    if tran_type == "Debit":
                        database.del_debit_tran(transaction_id)
                    else:
                        database.del_credit_tran(transaction_id)

                    st.success("Transaction deleted")

    else:
        st.warning("Transaction not found")

# =========================================================
# HISTORY
# =========================================================
elif nv == "History":

    st.header("📜 Transaction History")

    tran_type = st.radio("Type",["Debit","Credit"])

    if tran_type == "Debit":
        data = database.get_debit_record()
    else:
        data = database.get_credit_record()

    if data:

        df = pd.DataFrame(
            data,
            columns=["ID","Date","Amount","Category","Description"]
        )

        st.dataframe(df)

    else:
        st.write("No records found")

# =========================================================
# EXPENSE PREDICTOR
# =========================================================
elif nv == "Expense Predictor":

    st.header("🤖 Expense Prediction")

    months = {
        "January":1,"February":2,"March":3,"April":4,
        "May":5,"June":6,"July":7,"August":8,
        "September":9,"October":10,"November":11,"December":12
    }

    selected_month = st.selectbox("Select Month",list(months.keys()))

    if st.button("Predict Expenses"):

        month_number = months[selected_month]

        predicted = predictor.predict_expenses_with_random_forest(month_number)

        df = pd.DataFrame(predicted.items(), columns=["Category", "Predicted Expense"])

        st.subheader("📊 Predicted Expenses")
        st.dataframe(df)

        st.success(f"Total Predicted Expense ₹{df['Predicted Expense'].sum():.2f}")

        # 🔥 SMART BUDGET
        budget = predictor.recommend_budget(predicted)

        df_budget = pd.DataFrame(
            budget.items(),
            columns=["Category", "Recommended Budget"]
        )

        st.subheader("💡 Smart Budget Recommendation")
        st.dataframe(df_budget)

        st.success(f"Recommended Total Budget ₹{df_budget['Recommended Budget'].sum():.2f}")

# =========================================================
# VISUALIZATION
# =========================================================
elif nv == "Visual Representations":

    st.header("📊 Financial Visualizations")

    debit_data = database.get_debit_record()

    if debit_data:

        df = pd.DataFrame(
            debit_data,
            columns=["ID","Date","Amount","Category","Description"]
        )

        df["Date"] = pd.to_datetime(df["Date"])

        category_sum = df.groupby("Category")["Amount"].sum()

        st.subheader("Bar Chart")
        st.bar_chart(category_sum)

        st.subheader("Pie Chart")

        fig = go.Figure(
            data=[go.Pie(
                labels=category_sum.index,
                values=category_sum.values
            )]
        )

        st.plotly_chart(fig)

    else:
        st.write("No data to visualize")
