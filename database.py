import sqlite3 as sql

# Function to create the expense table if not exists
def create_table():
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS debit
                 (transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 date DATE, 
                 amount REAL, 
                 category TEXT, 
                 description TEXT)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS credit
                 (transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 date DATE,
                 amount REAL,
                 category TEXT,  -- Fixed typo here
                 description TEXT)''')
    
    conn.commit()
    conn.close()

    
create_table()

# Function to add a new debit record
def add_debit(date, amount, category, description):
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute("INSERT INTO debit (date, amount, category, description) VALUES (?, ?, ?, ?)", (date, amount, category, description))
    conn.commit()
    conn.close()
    
# Function to add a new credit record
def add_credit(date, amount, category, description):
    conn = sql.connect( "transactions.db" )
    c = conn.cursor()
    c.execute("INSERT INTO credit (date, amount, category, description) VALUES (?, ?, ?, ?)", (date, amount, category, description))
    conn.commit()
    conn.close()
    
# Function to retrieve all debit record
def get_debit_record():
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute("SELECT * FROM debit Order by date ")
    debit_record = c.fetchall()
    conn.close()
    return debit_record

# Function to retrieve all credit record
def get_credit_record():
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute("SELECT * FROM credit Order by date")
    debit_record = c.fetchall()
    conn.close()
    return debit_record

# Function to get total amount for a specific month from debit table
def get_debit_total_for_month(month):
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute("SELECT SUM(amount) FROM debit WHERE strftime('%Y-%m', date) = ?", (month,))
    total = c.fetchone()[0]
    return total if total else 0

# Function to get total amount for a specific month from credit table
def get_credit_total_for_month(month):
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute("SELECT SUM(amount) FROM credit WHERE strftime('%Y-%m', date) = ?", (month,))
    total = c.fetchone()[0]
    return total if total else 0

# Function to calculate balance
def calculate_balance(credit_total, debit_total):
    return credit_total - debit_total

# Funtions to retireve data according to month-year
month_mapping = {
    "January": "01", "February": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08",
    "September": "09", "October": "10", "November": "11", "December": "12"
}

def get_debit_record_by_month_year(month, year):
    conn = sql.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM debit WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?", (month_mapping[month], str(year)))
    debit_records = cursor.fetchall()
    conn.close()
    return debit_records

def get_credit_record_by_month_year(month, year):
    conn = sql.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM credit WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?", (month_mapping[month], str(year)))
    credit_records = cursor.fetchall()
    conn.close()
    return credit_records

# Funtion to retrive debit transtion details by ID
def get_debit_tran_id(transaction_id):
    conn = sql.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM debit WHERE transaction_id = ?", (transaction_id,))
    debit_record = cursor.fetchone()
    return debit_record

# Funtion to retrive credit transtion details by ID
def get_credit_tran_id(transaction_id):
    conn = sql.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM credit WHERE transaction_id = ?", (transaction_id,))
    credit_record = cursor.fetchone()
    return credit_record

# Function to update a debit transaction
def update_debit(transaction_id, date, category, amount, description):
    conn = sql.connect('transactions.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE debit SET date=?, category=?, amount=?, description=? WHERE transaction_id=?", (date, category, amount, description, transaction_id))
    conn.commit()

# Function to update a credit transaction
def update_credit(transaction_id, date, category, amount, description):
    conn = sql.connect('transactions.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE credit SET date=?, category=?, amount=?, description=? WHERE transaction_id=?", (date, category, amount, description, transaction_id))
    conn.commit()
    
# Funtion to delete the transaction from debit or credit table
def del_debit_tran(transaction_id):
    conn = sql.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM debit WHERE transaction_id = ?", (transaction_id,))
    conn.commit()
    conn.close()

def del_credit_tran(transaction_id):
    conn = sql.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM credit WHERE transaction_id = ?", (transaction_id,))
    conn.commit()
    conn.close()
