from pathlib import Path
from app.data.db import connect_database
from app.data.schema import create_all_tables
from app.services.user_service import migrate_users_from_file
from main import load_csv_to_table  

# Define database path
DB_PATH = Path("DATA/database.db")


def load_all_csv_data(conn):
    """Load all CSV files into the database."""
    total_rows = 0
    total_rows += load_csv_to_table(conn, "DATA/cyber_incidents.csv", "cyber_incidents")
    total_rows += load_csv_to_table(conn, "DATA/it_tickets.csv", "it_tickets")
    total_rows += load_csv_to_table(conn, "DATA/datasets_metadata.csv", "datasets_metadata")
    return total_rows


def setup_database_complete():
    """
    Complete database setup:
    1. Connect to database
    2. Create all tables
    3. Migrate users from users.txt
    4. Load CSV data for all domains
    5. Verify setup
    """
    print("\n" + "=" * 60)
    print("STARTING COMPLETE DATABASE SETUP")
    print("=" * 60)

    # Step 1: Connect
    print("\n[1/5] Connecting to database...")
    conn = connect_database()
    print("       Connected")

    # Step 2: Create tables
    print("\n[2/5] Creating database tables...")
    create_all_tables(conn)

    # Step 3: Migrate users
    print("\n[3/5] Migrating users from users.txt...")
    success, msg = migrate_users_from_file()
    if success:
        print(f"       {msg}")
    else:
        print(f"       Failed: {msg}")

    # Step 4: Load CSV data
    print("\n[4/5] Loading CSV data...")
    total_rows = load_all_csv_data(conn)
    print(f"       Loaded total {total_rows} rows from all CSV files")

    # Step 5: Verify
    print("\n[5/5] Verifying database setup...")
    cursor = conn.cursor()

    # Count rows in each table
    tables = ['users', 'cyber_incidents', 'datasets_metadata', 'it_tickets']
    print("\n Database Summary:")
    print(f"{'Table':<25} {'Row Count':<15}")
    print("-" * 40)

    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"{table:<25} {count:<15}")

    conn.close()

    print("\n" + "=" * 60)
    print(" DATABASE SETUP COMPLETE!")
    print("=" * 60)
    print(f"\n Database location: {DB_PATH.resolve()}")
    print("\nYou're ready for Week 9 (Streamlit web interface)!")


# Run the complete setup
if __name__ == "__main__":
    setup_database_complete()