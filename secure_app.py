import sqlite3
import os

# FIX-02: Load secrets safely via environment variables with a safe fallback
SECRET_KEY = os.getenv("SECRET_KEY", "dev-fallback-key-change-in-prod")

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
    
    # FIX-01: Use parameterized queries (?) to completely eliminate SQL injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    
    result = cursor.fetchall()
    conn.close()
    return result

def evaluate_user_input(user_code):
    # FIX-03: Removed insecure eval() entirely.
    raise NotImplementedError("Dynamic code evaluation has been disabled for security.")

if __name__ == "__main__":
    # Testing with malicious input safely returns an empty result instead of exploiting the DB
    print(get_user_profile("admin' OR '1'='1"))