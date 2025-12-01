def insert_ticket(conn, issue, status='open'):
    """Insert a new IT ticket and return its ID using the passed connection."""
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO it_tickets (issue, status) VALUES (?, ?)",
        (issue, status)
    )
    conn.commit()
    return cursor.lastrowid
#get all tickets
def get_all_tickets(conn):
    """Retrieve all IT tickets using the passed connection."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM it_tickets ORDER BY id DESC")
    tickets = cursor.fetchall()
    return tickets
#update
def update_ticket_status(conn, ticket_id, new_status):
    """Update the status of an IT ticket."""
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE it_tickets SET status = ? WHERE id = ?",
        (new_status, ticket_id)
    )
    conn.commit()
    return cursor.rowcount
#delete
def delete_ticket(conn, ticket_id):
    """Delete an IT ticket."""
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM it_tickets WHERE id = ?",
        (ticket_id,)
    )
    conn.commit()
    return cursor.rowcount