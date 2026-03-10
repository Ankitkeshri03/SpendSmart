# import streamlit as st
# import pandas as pd
# from datetime import datetime, timedelta
# import sqlite3 as sql
# import database 
# import predictor
 
 
 
# st.title("SpendSmart")

# st.sidebar.subheader("Welcome!!")

# # App Navigator
# nv = st.sidebar.selectbox("Navigator", ["Home","Add Transactions", "Edit/Delete Transactions", "History", "Expense Predictor", "Visual Representations"])

# if nv == "Home":
#     st.info("Home")
    
#     st.subheader("Welcome to SpendSmart")
#     st.write("SpendSmart is your personal finance management tool.")
#     st.write("Here's what you can do:")
    
#     st.markdown("- **Add Transactions:** Record your expenses and incomes.")
#     st.markdown("- **View Transaction History:** Review your past transactions.")
#     st.markdown("- **Expense Predictor:** Get insights and predictions about your future expenses.")
#     st.markdown("- **Visual Representations:** View charts and graphs representing your financial data.")
    
#     st.write("Use the navigation panel on the left to get started.")
    
#     st.subheader("Tips for Effective Financial Management")
#     st.markdown("- **Budgeting:** Set financial goals and create a budget to track your expenses.")
#     st.markdown("- **Tracking Expenses:** Monitor your spending habits and identify areas for improvement.")
#     st.markdown("- **Saving:** Start saving regularly to build an emergency fund and meet your long-term financial goals.")
#     st.markdown("- **Investing:** Learn about investment options and consider investing to grow your wealth.")
#     st.markdown("- **Reviewing:** Regularly review your financial status and adjust your strategies as needed.")
    
#     st.subheader("Why Choose SpendSmart?")
#     st.markdown("- **User-Friendly:** SpendSmart offers a simple and intuitive interface for easy navigation.")
#     st.markdown("- **Customizable:** Tailor SpendSmart to suit your unique financial needs and preferences.")
#     st.markdown("- **Insightful:** Gain valuable insights into your spending patterns and financial habits.")
#     st.markdown("- **Secure:** Your financial data is securely stored and protected.")


# elif nv == "Add Transactions":
#     st.info("Add Transactions")
    
#     st.subheader("Record Your Transactions")
#     st.write("Use this section to record your expenses and incomes.")
    
#     # Month-Mapping
#     month_mapping = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06", "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"}
    
#     # Get current month and year
#     current_month_year = datetime.now().strftime("%Y-%m")
#     current_month_name = datetime.now().strftime("%B")
    
#     # Get selected month from session state
#     selected_month = st.session_state.get("selected_month", current_month_name)
    
#     # Show Balance button
#     bal = st.button("Show Balance")
#     if bal:
#         # Month selection box
#         selected_month = st.selectbox("Select a month:", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], index=int(current_month_year.split("-")[1]) - 1, format_func=lambda x: f"{x} ({current_month_year.split('-')[0]})")
        
#         # Store selected month in session state
#         st.session_state.selected_month = selected_month
        
#         # Map the selected month name to its numeric representation
#         selected_month_number = month_mapping[selected_month]
        
#         selected_month_year = f"{current_month_year.split('-')[0]}-{selected_month_number}"
        
#         # Get total amounts for the selected month
#         debit_total = database.get_debit_total_for_month(selected_month_year)
#         credit_total = database.get_credit_total_for_month(selected_month_year)
        
#         if debit_total is None or credit_total is None:
#             st.write(f"No data available for {selected_month_year}.")
#         else:
#             # Calculate balance
#             balance = database.calculate_balance(credit_total, debit_total)
            
#             # Display total credit, total debit, and balance
#             st.write(f"Total credit for {selected_month_year}: {credit_total}")
#             st.write(f"Total debit for {selected_month_year}: {debit_total}")
#             st.write(f"Balance for {selected_month_year}: {balance}")

#     # Transaction type selection
#     tran_type = st.radio("Transaction Type", ["Debit", "Credit"])

#     # Debit transaction form
#     if tran_type == "Debit":
#         with st.form(key="debit_form"):
#             st.subheader("Debit Transaction")
#             st.write("Record your expenses here.")

#             date = st.date_input("Date:", pd.to_datetime("today"))
#             category = st.selectbox("Category:", ["Utilities", "Groceries", "Food", "Transportation", "Stationary",
#                       "Subscriptions", "Entertainment", "Medical_Expenses", "Phone/Internet_Bill"])
#             amount = st.number_input("Amount:", min_value=0.01, format="%f")
#             description = st.text_area("Description:")

#             # Form submission
#             debit_sbtn = st.form_submit_button("Add Transaction")

#         if debit_sbtn:
#             st.success("Transaction Added Successfully")
#             database.add_debit(date, amount, category, description)

#     # Credit transaction form
#     elif tran_type == "Credit":
#         with st.form(key="credit_form"):
#             st.subheader("Credit Transaction")
#             st.write("Record your incomes here.")

#             date = st.date_input("Date:", pd.to_datetime("today"))
#             category = st.selectbox("Category:", ["Salary", "Sale", "Lottery", "Bank_Interest", "Rent_Received"])
#             amount = st.number_input("Amount:", min_value=0.01, format="%f")
#             description = st.text_area("Description:")

#             # Form submission
#             credit_sbtn = st.form_submit_button("Add Transaction")

#         if credit_sbtn:
#             st.success("Transaction Added Successfully") 
#             database.add_credit(date, amount, category, description)


# elif nv == "Edit/Delete Transactions":
#     st.info("Edit/Delete Transactions")
    
#     option = st.radio("Funtion Type:", ["Edit", "Delete"])
    
#     if option == "Edit":
#         st.subheader("Edit Transaction")
#         st.write("Select a transaction to edit and make modifications.")
        
    
#         # Transaction type selection
#         tran_type = st.radio("Transaction Type:", ["Debit", "Credit"])
    
#         # User input for unique transaction id
#         transaction_id = st.number_input("Enter Transaction ID:", value=1, step=1)
        
#         if tran_type == "Debit":
#             transaction_data = database.get_debit_tran_id(transaction_id)
#         else:
#             transaction_data = database.get_credit_tran_id(transaction_id)
            
#         # Display transaction before editing
#         if transaction_data:
#             st.write("Transaction Details:")
#             st.write(transaction_data)
            
#             # Edit transaction form
#             with st.form(key="edit_form"):
#                 st.subheader("Edit Transaction")
#                 date = st.date_input("Date:", pd.to_datetime(transaction_data[1]))
#                 category = st.selectbox("Category:", [transaction_data[3]])
#                 amount = st.number_input("Amount:", value=float(transaction_data[2]), format="%.2f")
#                 description = st.text_area("Description:", value=transaction_data[4])
                
#                 # Form submission
#                 edit_sbtn = st.form_submit_button("Update Transaction")
            
#             if edit_sbtn:
#                 if tran_type == "Debit":
#                     database.update_debit(transaction_id, date, category, amount, description)
#                 else:
#                     database.update_credit(transaction_id, date, category, amount, description)
                
#                 st.success("Transaction Updated Successfully.")
#         else:
#             st.write("No transaction found with the given ID.")

#     else:
#         st.subheader("Delete Transaction")
#         st.write("Select a transaction to Delete.")
        
#         # Transaction type selection
#         tran_type = st.radio("Transaction Type:", ["Debit", "Credit"])
    
#         # User input for unique transaction id
#         transaction_id = st.number_input("Enter Transaction ID:", value=1, step=1)
        
#         if tran_type == "Debit":
#             transaction_data = database.get_debit_tran_id(transaction_id)
#         else:
#             transaction_data = database.get_credit_tran_id(transaction_id)
            
#         # Display transaction before deleting
#         if transaction_data:
#             st.write("Transaction Details:")
#             st.write(transaction_data)
            
#             # Delete button
            
#             del_btn = st.button("Delete Transaction")
            
#             if del_btn:
#                 if tran_type == "Debit":
#                     database.del_debit_tran(transaction_id)
#                 else:
#                     database.del_credit_tran(transaction_id)
#             st.success("Selected Transaction Deleted!!")
            
#         else:
#             st.write("No transaction found with the provided ID.")
            

# elif nv == "History":
#     st.info("History")
    
#     st.subheader("Transaction History")
#     st.write("Here you can view your past transactions.")

#     # Transaction type selection
#     tran_type = st.radio("Transaction Type", ["Debit", "Credit"])

#     # Display debit transaction history
#     if tran_type == "Debit":
#         debit_data = database.get_debit_record()
#         if debit_data:
#             st.write("Debit Transactions:")
#             column_names = ["Transaction ID", "Date", "Amount", "Category", "Description"]
#             debit_df = pd.DataFrame(debit_data, columns=column_names)
#             debit_df_no_index = debit_df.reset_index(drop=True)  # Reset index without adding as a column
#             st.table(debit_df_no_index)
#         else:
#             st.write("No debit records found.")

#     # Display credit transaction history
#     elif tran_type == "Credit":
#         credit_data = database.get_credit_record()
#         if credit_data:
#             st.write("Credit Transactions:")
#             column_names = ["Transaction ID", "Date", "Amount", "Category", "Description"]
#             credit_df = pd.DataFrame(credit_data, columns=column_names, index = None)
#             st.table(credit_df)
#         else:
#             st.write("No credit records found.")

        
# elif nv == "Expense Predictor":
#     st.info("Expense Predictor")
  
#     # Button to predict expenses for the current month
#     predict_btn = st.button("Predict Expenses for Current Month")

#     if predict_btn:
#         st.subheader("Predicted Expenses for Current Month")
        
#         current_month_number = datetime.now().month

#         # Predict expenses for the current month using the Random Forest models
#         predicted_expenses = predictor.predict_expenses_with_random_forest(current_month_number)

#         # Display predicted expenses for each category
#         st.write("Predicted Expenses:")
#         for category, expense in predicted_expenses.items():
#             st.write(f"{category}: ${expense:.2f}")

        
# elif nv == "Visual Representations":
#     st.subheader("Visual Representations")
#     st.write("Here you can find visualizations of your financial data.")

#     # Load data from the database
#     conn = sql.connect("transactions.db")
#     debit_data = database.get_debit_record()
#     credit_data = database.get_credit_record()
    
#     # Button to select which kind of transaction data to be shown
#     tran_type = st.radio("Select Transaction Type: ", ("Debit","Credit"))
    
#     if debit_data or credit_data:
        
#         if tran_type == "Debit":
#             # Convert data to DataFrames
#             debit_df = pd.DataFrame(debit_data, columns=["Transaction ID" ,"Date", "Amount", "Category", "Description"])
            
#             # Convert "Date" column to datetime format
#             debit_df["Date"] = pd.to_datetime(debit_df["Date"])
            
#             # Plot a bar chart of expenses by category
#             st.subheader("Expenses by Category")
#             expense_chart_data = debit_df.groupby("Category")["Amount"].sum()
#             st.bar_chart(expense_chart_data)

#             # Plot a pie chart of expenses by category
#             st.subheader("Expenses by Category (Pie Chart)")
#             st.write("Select a month to view expenses by category:")
#             selected_month = st.selectbox("Month", sorted(set(debit_df["Date"].dt.strftime("%B"))))
#             selected_month_data = debit_df[debit_df["Date"].dt.strftime("%B") == selected_month]
#             category_expenses = selected_month_data.groupby("Category")["Amount"].sum()
    
#             # Create Plotly figure for the pie chart
#             import plotly.graph_objs as go
#             fig = go.Figure(data=[go.Pie(labels=category_expenses.index, values=category_expenses)])
#             st.plotly_chart(fig)
        
#         else:
#             # Covert data to DataFrames
#             credit_df = pd.DataFrame(credit_data, columns=["Transaction ID" ,"Date", "Amount", "Category", "Description"])
    
#             # Convert "Date" column to datetimr format
#             credit_df["Date"] = pd.to_datetime(credit_df["Date"])
    
#             # Plot a line chart of income over time
#             st.subheader("Income Over Time")
#             income_chart_data = credit_df.set_index("Date").resample("M")["Amount"].sum()
#             st.line_chart(income_chart_data)        

#     else:
#         st.write("No data available to visualize. Please add transactions .")



import streamlit as st
import pandas as pd
from datetime import datetime
import sqlite3
import database
import predictor
import plotly.graph_objects as go

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

            category = st.selectbox(
                "Category",
                [
                    "Utilities","Groceries","Food","Transportation",
                    "Stationary","Subscriptions","Entertainment",
                    "Medical_Expenses","Phone/Internet_Bill"
                ]
            )

            amount = st.number_input("Amount",min_value=0.01)
            description = st.text_area("Description")

            submit = st.form_submit_button("Add Expense")

        if submit:
            database.add_debit(date,amount,category,description)
            st.success("Expense added")

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
            st.success("Income added")

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

        df = pd.DataFrame(predicted.items(),columns=["Category","Predicted Expense"])

        st.dataframe(df)

        st.success(f"Total Predicted Expense ₹{df['Predicted Expense'].sum():.2f}")

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

