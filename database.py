# import sqlite3 as sql

# # Function to create the expense table if not exists
# def create_table():
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()

#     c.execute('''CREATE TABLE IF NOT EXISTS debit
#                  (
#                  transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  user_id INTEGER,
#                  date DATE, 
#                  amount REAL, 
#                  category TEXT, 
#                  description TEXT)''')

#     c.execute('''CREATE TABLE IF NOT EXISTS credit
#                  (
#                  transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  user_id INTEGER,
#                  date DATE,
#                  amount REAL,
#                  category TEXT,
#                  description TEXT)''')

#     conn.commit()
#     conn.close()

# create_table()

# # ---------------- ADD ----------------
# def add_debit(user_id, date, amount, category, description):
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute(
#         "INSERT INTO debit (user_id, date, amount, category, description) VALUES (?, ?, ?, ?, ?)",
#         (user_id, date, amount, category, description)
#     )
#     conn.commit()
#     conn.close()


# def add_credit(user_id, date, amount, category, description):
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute(
#         "INSERT INTO credit (user_id, date, amount, category, description) VALUES (?, ?, ?, ?, ?)",
#         (user_id, date, amount, category, description)
#     )
#     conn.commit()
#     conn.close()

# # ---------------- FETCH ----------------
# def get_debit_record(user_id):
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute("SELECT * FROM debit WHERE user_id=? ORDER BY date", (user_id,))
#     debit_record = c.fetchall()
#     conn.close()
#     return debit_record


# def get_credit_record(user_id):
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute("SELECT * FROM credit WHERE user_id=? ORDER BY date", (user_id,))
#     credit_record = c.fetchall()
#     conn.close()
#     return credit_record

# # ---------------- MONTH TOTAL ----------------
# def get_debit_total_for_month(month):
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute("SELECT SUM(amount) FROM debit WHERE strftime('%Y-%m', date) = ?", (month,))
#     total = c.fetchone()[0]
#     conn.close()
#     return total if total else 0


# def get_credit_total_for_month(month):
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute("SELECT SUM(amount) FROM credit WHERE strftime('%Y-%m', date) = ?", (month,))
#     total = c.fetchone()[0]
#     conn.close()
#     return total if total else 0

# # ---------------- BALANCE ----------------
# def calculate_balance(credit_total, debit_total):
#     return credit_total - debit_total

# # ---------------- MONTH FILTER ----------------
# month_mapping = {
#     "January": "01", "February": "02", "March": "03", "April": "04",
#     "May": "05", "June": "06", "July": "07", "August": "08",
#     "September": "09", "October": "10", "November": "11", "December": "12"
# }

# def get_debit_record_by_month_year(user_id, month, year):
#     conn = sql.connect("transactions.db")
#     cursor = conn.cursor()
#     cursor.execute(
#         "SELECT * FROM debit WHERE user_id=? AND strftime('%m', date)=? AND strftime('%Y', date)=?",
#         (user_id, month_mapping[month], str(year))
#     )
#     debit_records = cursor.fetchall()
#     conn.close()
#     return debit_records


# def get_credit_record_by_month_year(user_id, month, year):
#     conn = sql.connect("transactions.db")
#     cursor = conn.cursor()
#     cursor.execute(
#         "SELECT * FROM credit WHERE user_id=? AND strftime('%m', date)=? AND strftime('%Y', date)=?",
#         (user_id, month_mapping[month], str(year))
#     )
#     credit_records = cursor.fetchall()
#     conn.close()
#     return credit_records

# # ---------------- GET BY ID ----------------
# def get_debit_tran_id(transaction_id, user_id):
#     conn = sql.connect("transactions.db")
#     cursor = conn.cursor()
#     cursor.execute(
#         "SELECT * FROM debit WHERE transaction_id=? AND user_id=?",
#         (transaction_id, user_id)
#     )
#     debit_record = cursor.fetchone()
#     conn.close()
#     return debit_record


# def get_credit_tran_id(transaction_id, user_id):
#     conn = sql.connect("transactions.db")
#     cursor = conn.cursor()
#     cursor.execute(
#         "SELECT * FROM credit WHERE transaction_id=? AND user_id=?",
#         (transaction_id, user_id)
#     )
#     credit_record = cursor.fetchone()
#     conn.close()
#     return credit_record

# # ---------------- UPDATE ----------------
# def update_debit(transaction_id, user_id, date, category, amount, description):
#     conn = sql.connect('transactions.db')
#     cursor = conn.cursor()
#     cursor.execute(
#         "UPDATE debit SET date=?, category=?, amount=?, description=? WHERE transaction_id=? AND user_id=?",
#         (date, category, amount, description, transaction_id, user_id)
#     )
#     conn.commit()
#     conn.close()


# def update_credit(transaction_id, user_id, date, category, amount, description):
#     conn = sql.connect('transactions.db')
#     cursor = conn.cursor()
#     cursor.execute(
#         "UPDATE credit SET date=?, category=?, amount=?, description=? WHERE transaction_id=? AND user_id=?",
#         (date, category, amount, description, transaction_id, user_id)
#     )
#     conn.commit()
#     conn.close()

# # ---------------- DELETE ----------------
# def del_debit_tran(transaction_id, user_id):
#     conn = sql.connect("transactions.db")
#     cursor = conn.cursor()
#     cursor.execute(
#         "DELETE FROM debit WHERE transaction_id=? AND user_id=?",
#         (transaction_id, user_id)
#     )
#     conn.commit()
#     conn.close()


# def del_credit_tran(transaction_id, user_id):
#     conn = sql.connect("transactions.db")
#     cursor = conn.cursor()
#     cursor.execute(
#         "DELETE FROM credit WHERE transaction_id=? AND user_id=?",
#         (transaction_id, user_id)
#     )
#     conn.commit()
#     conn.close()

# # ---------------- USER TABLE ----------------
# def create_user_table():
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()

#     c.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT UNIQUE,
#         password TEXT
#     )
#     ''')

#     conn.commit()
#     conn.close()

# create_user_table()

# # ---------------- AUTH ----------------
# def create_user(username, password):
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
#     conn.commit()
#     conn.close()


# def check_user(username, password):
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
#     user = c.fetchone()
#     conn.close()
#     return user


# import sqlite3 as sql

# # Function to create the expense table if not exists
# def create_table():
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS debit
#                  (
#                  transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  user_id INTEGER,
#                  date DATE, 
#                  amount REAL, 
#                  category TEXT, 
#                  description TEXT)''')
    
#     c.execute('''CREATE TABLE IF NOT EXISTS credit
#                  (transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  user_id INTEGER,
#                  date DATE,
#                  amount REAL,
#                  category TEXT,  -- Fixed typo here
#                  description TEXT)''')
    
#     conn.commit()
#     conn.close()

    
# create_table()

# # Function to add a new debit record
# def add_debit(user_id,date, amount, category, description):
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute( "INSERT INTO debit (user_id,date, amount, category, description) VALUES (?, ?, ?, ?)", (user_id, date, amount, category, description))
#     conn.commit()
#     conn.close()
    

# # Function to add a new credit record
# def add_credit(user_id,date, amount, category, description):
#     conn = sql.connect( "transactions.db" )
#     c = conn.cursor()
#     c.execute("INSERT INTO credit (user_id,date, amount, category, description) VALUES (?, ?, ?, ?)", (user_id, date, amount, category, description))
#     conn.commit()
#     conn.close()
    
# # Function to retrieve all debit record
# def get_debit_record():
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute("SELECT * FROM debit WHERE user_id=? ORDER BY date", (user_id,))
#     debit_record = c.fetchall()
#     conn.close()
#     return debit_record

# # Function to retrieve all credit record
# def get_credit_record():
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute("SELECT * FROM credit WHERE user_id=? ORDER BY date", (user_id,))
#     debit_record = c.fetchall()
#     conn.close()
#     return debit_record

# # Function to get total amount for a specific month from debit table
# def get_debit_total_for_month(month):
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute("SELECT SUM(amount) FROM debit WHERE strftime('%Y-%m', date) = ?", (month,))
#     total = c.fetchone()[0]
#     return total if total else 0

# # Function to get total amount for a specific month from credit table
# def get_credit_total_for_month(month):
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()
#     c.execute("SELECT SUM(amount) FROM credit WHERE strftime('%Y-%m', date) = ?", (month,))
#     total = c.fetchone()[0]
#     return total if total else 0

# # Function to calculate balance
# def calculate_balance(credit_total, debit_total):
#     return credit_total - debit_total

# # Funtions to retireve data according to month-year
# month_mapping = {
#     "January": "01", "February": "02", "March": "03", "April": "04",
#     "May": "05", "June": "06", "July": "07", "August": "08",
#     "September": "09", "October": "10", "November": "11", "December": "12"
# }

# def get_debit_record_by_month_year(month, year):
#     conn = sql.connect("transactions.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM debit WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?", (month_mapping[month], str(year)))
#     debit_records = cursor.fetchall()
#     conn.close()
#     return debit_records

# def get_credit_record_by_month_year(month, year):
#     conn = sql.connect("transactions.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM credit WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?", (month_mapping[month], str(year)))
#     credit_records = cursor.fetchall()
#     conn.close()
#     return credit_records

# # Funtion to retrive debit transtion details by ID
# def get_debit_tran_id(transaction_id):
#     conn = sql.connect("transactions.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM debit WHERE transaction_id = ?", (transaction_id,))
#     debit_record = cursor.fetchone()
#     return debit_record

# # Funtion to retrive credit transtion details by ID
# def get_credit_tran_id(transaction_id):
#     conn = sql.connect("transactions.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM credit WHERE transaction_id = ?", (transaction_id,))
#     credit_record = cursor.fetchone()
#     return credit_record

# # Function to update a debit transaction
# def update_debit(transaction_id, date, category, amount, description):
#     conn = sql.connect('transactions.db')
#     cursor = conn.cursor()
#     cursor.execute("UPDATE debit SET date=?, category=?, amount=?, description=? WHERE transaction_id=?", (date, category, amount, description, transaction_id))
#     conn.commit()

# # Function to update a credit transaction
# def update_credit(transaction_id, date, category, amount, description):
#     conn = sql.connect('transactions.db')
#     cursor = conn.cursor()
#     cursor.execute("UPDATE credit SET date=?, category=?, amount=?, description=? WHERE transaction_id=?", (date, category, amount, description, transaction_id))
#     conn.commit()
    
# # Funtion to delete the transaction from debit or credit table
# def del_debit_tran(transaction_id):
#     conn = sql.connect("transactions.db")
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM debit WHERE transaction_id = ?", (transaction_id,))
#     conn.commit()
#     conn.close()

# def del_credit_tran(transaction_id):
#     conn = sql.connect("transactions.db")
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM credit WHERE transaction_id = ?", (transaction_id,))
#     conn.commit()
#     conn.close()

# def create_user_table():
#     conn = sql.connect("transactions.db")
#     c = conn.cursor()

#     c.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT UNIQUE,
#         password TEXT
#     )
#     ''')

#     conn.commit()
#     conn.close()

# create_user_table()
import sqlite3 as sql
def init_db():
    conn = sql.connect("transactions.db")
    c = conn.cursor()

    # Users
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    ''')

    # Debit
    c.execute('''
    CREATE TABLE IF NOT EXISTS debit (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date DATE,
        amount REAL,
        category TEXT,
        description TEXT
    )
    ''')

    # Credit
    c.execute('''
    CREATE TABLE IF NOT EXISTS credit (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date DATE,
        amount REAL,
        category TEXT,
        description TEXT
    )
    ''')

    # 🔥 ADD THIS (missing table)
    c.execute('''
    CREATE TABLE IF NOT EXISTS monthly_salary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        month TEXT,
        salary REAL
    )
    ''')

    conn.commit()
    conn.close()
# Function to create the expense table if not exists
def create_table():
    conn = sql.connect("transactions.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS debit
                 (
                 transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_id INTEGER,
                 date DATE, 
                 amount REAL, 
                 category TEXT, 
                 description TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS credit
                 (
                 transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_id INTEGER,
                 date DATE,
                 amount REAL,
                 category TEXT,
                 description TEXT)''')

    conn.commit()
    conn.close()

create_table()

# ---------------- ADD ----------------
def add_debit(user_id, date, amount, category, description):
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO debit (user_id, date, amount, category, description) VALUES (?, ?, ?, ?, ?)",
        (user_id, date, amount, category, description)
    )
    conn.commit()
    conn.close()


def add_credit(user_id, date, amount, category, description):
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO credit (user_id, date, amount, category, description) VALUES (?, ?, ?, ?, ?)",
        (user_id, date, amount, category, description)
    )
    conn.commit()
    conn.close()

# ---------------- FETCH ----------------
def get_debit_record(user_id):
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute("SELECT * FROM debit WHERE user_id=? ORDER BY date", (user_id,))
    debit_record = c.fetchall()
    conn.close()
    return debit_record


def get_credit_record(user_id):
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute("SELECT * FROM credit WHERE user_id=? ORDER BY date", (user_id,))
    credit_record = c.fetchall()
    conn.close()
    return credit_record

# ---------------- MONTH TOTAL ----------------
def get_debit_total_for_month(month):
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute("SELECT SUM(amount) FROM debit WHERE strftime('%Y-%m', date) = ?", (month,))
    total = c.fetchone()[0]
    conn.close()
    return total if total else 0


def get_credit_total_for_month(month):
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute("SELECT SUM(amount) FROM credit WHERE strftime('%Y-%m', date) = ?", (month,))
    total = c.fetchone()[0]
    conn.close()
    return total if total else 0

# ---------------- BALANCE ----------------
def calculate_balance(credit_total, debit_total):
    return credit_total - debit_total

# ---------------- MONTH FILTER ----------------
month_mapping = {
    "January": "01", "February": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08",
    "September": "09", "October": "10", "November": "11", "December": "12"
}

def get_debit_record_by_month_year(user_id, month, year):
    conn = sql.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM debit WHERE user_id=? AND strftime('%m', date)=? AND strftime('%Y', date)=?",
        (user_id, month_mapping[month], str(year))
    )
    debit_records = cursor.fetchall()
    conn.close()
    return debit_records


def get_credit_record_by_month_year(user_id, month, year):
    conn = sql.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM credit WHERE user_id=? AND strftime('%m', date)=? AND strftime('%Y', date)=?",
        (user_id, month_mapping[month], str(year))
    )
    credit_records = cursor.fetchall()
    conn.close()
    return credit_records

# ---------------- GET BY ID ----------------
def get_debit_tran_id(transaction_id, user_id):
    conn = sql.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM debit WHERE transaction_id=? AND user_id=?",
        (transaction_id, user_id)
    )
    debit_record = cursor.fetchone()
    conn.close()
    return debit_record


def get_credit_tran_id(transaction_id, user_id):
    conn = sql.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM credit WHERE transaction_id=? AND user_id=?",
        (transaction_id, user_id)
    )
    credit_record = cursor.fetchone()
    conn.close()
    return credit_record

# ---------------- UPDATE ----------------
def update_debit(transaction_id, user_id, date, category, amount, description):
    conn = sql.connect('transactions.db')
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE debit SET date=?, category=?, amount=?, description=? WHERE transaction_id=? AND user_id=?",
        (date, category, amount, description, transaction_id, user_id)
    )
    conn.commit()
    conn.close()


def update_credit(transaction_id, user_id, date, category, amount, description):
    conn = sql.connect('transactions.db')
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE credit SET date=?, category=?, amount=?, description=? WHERE transaction_id=? AND user_id=?",
        (date, category, amount, description, transaction_id, user_id)
    )
    conn.commit()
    conn.close()

# ---------------- DELETE ----------------
def del_debit_tran(transaction_id, user_id):
    conn = sql.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM debit WHERE transaction_id=? AND user_id=?",
        (transaction_id, user_id)
    )
    conn.commit()
    conn.close()


def del_credit_tran(transaction_id, user_id):
    conn = sql.connect("transactions.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM credit WHERE transaction_id=? AND user_id=?",
        (transaction_id, user_id)
    )
    conn.commit()
    conn.close()

# ---------------- USER TABLE ----------------
def create_user_table():
    conn = sql.connect("transactions.db")
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    ''')

    conn.commit()
    conn.close()

create_user_table()

# ---------------- AUTH ----------------
def create_user(username, password):
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()


def check_user(username, password):
    init_db()  # 🔥 ensures table exists
    conn = sql.connect("transactions.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    return user
