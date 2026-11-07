import sqlite3
import os

# VULN-02: Hardcoded Secret (Bandit rule B105 / B106)
SECRET_KEY = "my_super_secret_admin_password_123"

def init_db():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, role TEXT)')
    cursor.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'administrator')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (2, 'alice', 'user')")
    conn.commit()
    conn.close()

def get_user_profile(username):
    init_db()
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    
    # VULN-01: SQL Injection via raw string formatting (Bandit rule B608)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print(f"Executing Query: {query}")
    
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def evaluate_user_input(user_code):
    # VULN-03: Dangerous use of eval() (Bandit rule B307)
    return eval(user_code)

if __name__ == "__main__":
    # Test vulnerable function
    print(get_user_profile("admin' OR '1'='1"))