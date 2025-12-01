from app.data.db import connect_database

def create_users_table(conn):
    """Create users table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user'
        )
    """)
    conn.commit()
#creating cyber incidents table
def create_cyber_incidents_table(conn):
    """Create cyber_incidents table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cyber_incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            incident_type TEXT NOT NULL,
            severity TEXT,
            status TEXT,
            description TEXT,
            reported_by TEXT
        )
    """)
    conn.commit()
#creating dataset table
def create_datasets_metadata_table(conn):
    """Create datasets_metadata table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS datasets_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dataset_name TEXT NOT NULL,
            description TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
#creating tickets table
def create_it_tickets_table(conn):
    """Create it_tickets table."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS it_tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            issue TEXT NOT NULL,
            status TEXT DEFAULT 'open',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
#creating all tables 
def create_all_tables(conn):
    """Create all tables."""
    create_users_table(conn)
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    create_it_tickets_table(conn)
#main
if __name__ == "__main__":
    conn = connect_database()  
    create_all_tables(conn)
    conn.close()
    print("All tables created successfully!")