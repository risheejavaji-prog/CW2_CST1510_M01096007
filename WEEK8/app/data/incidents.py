import pandas as pd
#insert
def insert_incident(conn, date, incident_type, severity, status, description, reported_by=None):
    """Insert a new cyber incident and return its ID."""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cyber_incidents
        (date, incident_type, severity, status, description, reported_by)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (date, incident_type, severity, status, description, reported_by))
    conn.commit()
    return cursor.lastrowid
#collecting incidents
def get_all_incidents(conn):
    """Retrieve all incidents as a DataFrame."""
    df = pd.read_sql_query("SELECT * FROM cyber_incidents ORDER BY id DESC", conn)
    return df
#update
def update_incident_status(conn, incident_id, new_status):
    """Update the status of an incident."""
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE cyber_incidents SET status = ? WHERE id = ?",
        (new_status, incident_id)
    )
    conn.commit()
    return cursor.rowcount
#delete
def delete_incident(conn, incident_id):
    """Delete an incident."""
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM cyber_incidents WHERE id = ?",
        (incident_id,)
    )
    conn.commit()
    return cursor.rowcount

def get_incidents_by_type_count(conn):
    """
    Return a DataFrame with count of incidents grouped by incident_type.
    """
    query = "SELECT incident_type, COUNT(*) as count FROM cyber_incidents GROUP BY incident_type"
    df = pd.read_sql_query(query, conn)
    return df

def get_high_severity_by_status(conn):
    """
    Return a DataFrame with high severity incidents grouped by status.
    """
    query = "SELECT status, COUNT(*) as count FROM cyber_incidents WHERE severity='High' GROUP BY status"
    df = pd.read_sql_query(query, conn)
    return df