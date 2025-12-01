from app.data.db import connect_database
import sqlite3

def insert_user(username, password_hash, role='user'):
    """Insert a new user safely."""
    conn = connect_database()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
            (username, password_hash, role)
        )
        conn.commit()
        print(f"User '{username}' inserted successfully!")
    except sqlite3.IntegrityError:
        print(f"Username '{username}' already exists!")
    finally:
        conn.close()

def get_user_by_username(username):
    """Retrieve user by username."""
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user