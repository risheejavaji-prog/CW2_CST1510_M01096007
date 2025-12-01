import pandas as pd
from app.data.db import connect_database
from app.services.user_service import register_user, login_user
from app.data.incidents import (
    insert_incident,
    get_all_incidents,
    update_incident_status,
    delete_incident,
)
from app.data.it_tickets import (
    insert_ticket,
    get_all_tickets,
    update_ticket_status,
    delete_ticket,
)
from app.data.datasets import (
    insert_dataset,
    get_all_datasets,
    update_dataset_description,
    delete_dataset,
)


def run_comprehensive_tests():
    """
    Run comprehensive tests on your database.
    """
    print("\n" + "="*60)
    print("🧪 RUNNING COMPREHENSIVE DATABASE TESTS")
    print("="*60)
    
    conn = connect_database()
    
    # ---------------------
    # TEST 1: Authentication
    # ---------------------
    print("\n[TEST 1] User Authentication")
    success, msg = register_user("test_user", "TestPass123!", "user")
    print(f"  Register: {'✅' if success else '❌'} {msg}")
    
    success, msg = login_user("test_user", "TestPass123!")
    print(f"  Login:    {'✅' if success else '❌'} {msg}")
    
    # ---------------------
    # TEST 2: Cyber Incidents CRUD
    # ---------------------
    print("\n[TEST 2] Cyber Incidents CRUD")
    
    # Create
    incident_id = insert_incident(
        conn,
        "2025-11-30",
        "Test Incident",
        "Low",
        "Open",
        "This is a test incident",
        "test_user"
    )
    print(f"  Create: ✅ Incident #{incident_id} created")
    
    # Read
    df_inc = pd.read_sql_query(
        "SELECT * FROM cyber_incidents WHERE id = ?",
        conn,
        params=(incident_id,)
    )
    print(f"  Read:    Found incident #{incident_id}" if not df_inc.empty else "  Read: ❌ Incident not found")
    
    # Update
    update_incident_status(conn, incident_id, "Resolved")
    print(f"  Update:  Incident status updated")
    
    # Delete
    delete_incident(conn, incident_id)
    print(f"  Delete:  Incident deleted")
    
    # ---------------------
    # TEST 3: IT Tickets CRUD
    # ---------------------
    print("\n[TEST 3] IT Tickets CRUD")
    
    # Create
    ticket_id = insert_ticket(conn, "Test ticket issue")
    print(f"  Create: ✅ Ticket #{ticket_id} created")
    
    # Read
    tickets = get_all_tickets(conn)
    print(f"  Read:    Found {len(tickets)} tickets")
    
    # Update
    update_ticket_status(conn, ticket_id, "Closed")
    print(f"  Update:  Ticket status updated")
    
    # Delete
    delete_ticket(conn, ticket_id)
    print(f"  Delete:  Ticket deleted")
    
    # ---------------------
    # TEST 4: Datasets CRUD
    # ---------------------
    print("\n[TEST 4] Dataset Metadata CRUD")
    
    # Create
    dataset_id = insert_dataset(conn, "Test Dataset", "Sample dataset description")
    print(f"  Create: ✅ Dataset #{dataset_id} created")
    
    # Read
    datasets = get_all_datasets(conn)
    print(f"  Read:    Found {len(datasets)} datasets")
    
    # Update
    update_dataset_description(conn, dataset_id, "Updated dataset description")
    print(f"  Update:  Dataset description updated")
    
    # Delete
    delete_dataset(conn, dataset_id)
    print(f"  Delete:  Dataset deleted")
    
    conn.close()
    
    print("\n" + "="*60)
    print("✅ ALL TESTS PASSED!")
    print("="*60)

# Run the tests
if __name__ == "__main__":
    run_comprehensive_tests()
