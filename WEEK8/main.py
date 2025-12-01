from app.data.db import connect_database
from app.data.schema import create_all_tables
from app.services.user_service import register_user, login_user, migrate_users_from_file
from app.data.users import get_user_by_username
from app.data.incidents import insert_incident, get_all_incidents
from app.data.it_tickets import insert_ticket, get_all_tickets
from app.data.datasets import insert_dataset, get_all_datasets
import pandas as pd
from pathlib import Path

# Function to load CSV files
def load_csv_to_table(conn, csv_path, table_name):
    """
    Load a CSV file into a database table using pandas.
    """
    file_path = Path(csv_path)
    if not file_path.exists():
        print(f"CSV file '{csv_path}' not found!")
        return 0

    df = pd.read_csv(file_path)
    df.to_sql(name=table_name, con=conn, if_exists='append', index=False)

    row_count = len(df)
    print(f"Loaded {row_count} rows from '{csv_path}' into '{table_name}'")
    return row_count

def main():
    print("=" * 60)
    print("Week 8: Database Demo")
    print("=" * 60)

    # Setup database
    conn = connect_database()
    create_all_tables(conn)
    print("Database tables are ready.\n")

    # Migrating users 
    success, msg = migrate_users_from_file()
    print(msg)

    # Load CSV data for the 3 domains
    load_csv_to_table(conn, "DATA/cyber_incidents.csv", "cyber_incidents")
    load_csv_to_table(conn, "DATA/it_tickets.csv", "it_tickets")
    load_csv_to_table(conn, "DATA/datasets_metadata.csv", "datasets_metadata")
    print()

    # Register a new user 
    success, msg = register_user("alice", "SecurePass123!", "analyst")
    print(msg)

    # Authenticate user 
    success, msg = login_user("alice", "SecurePass123!")
    print(msg)
    if success:
        print(f"User details: {get_user_by_username('alice')}\n")

    #  Insert a cyber incident 
    incident_id = insert_incident(
        conn,
        "2025-11-30",
        "Phishing",
        "High",
        "Open",
        "Suspicious email detected",
        "alice"
    )
    print(f"Created cyber incident #{incident_id}")

    # Query and display all incidents 
    df_incidents = get_all_incidents(conn)
    print(f"Total incidents: {len(df_incidents)}\n")

    #  Insert IT ticket 
    ticket_id = insert_ticket(conn, "VPN not connecting")
    print(f"Created IT ticket #{ticket_id}")
    tickets = get_all_tickets(conn)
    print(f"Total IT tickets: {len(tickets)}\n")

    #  Insert dataset metadata 
    dataset_id = insert_dataset(conn, "Employee Records", "Contains employee info")
    print(f"Inserted dataset #{dataset_id}")
    datasets = get_all_datasets(conn)
    print(f"Total datasets: {len(datasets)}\n")

    #  Close connection
    conn.close()

    print("=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
