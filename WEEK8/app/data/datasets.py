def insert_dataset(conn, dataset_name, description=""):
    """Insert a new dataset metadata record and return its ID."""
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO datasets_metadata (dataset_name, description) VALUES (?, ?)",
        (dataset_name, description)
    )
    conn.commit()
    return cursor.lastrowid

def get_all_datasets(conn):
    """Retrieve all datasets metadata."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datasets_metadata ORDER BY id DESC")
    return cursor.fetchall()
#update 
def update_dataset_description(conn, dataset_id, new_description):
    """Update the description of a dataset."""
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE datasets_metadata SET description = ? WHERE id = ?",
        (new_description, dataset_id)
    )
    conn.commit()
    return cursor.rowcount
#delete
def delete_dataset(conn, dataset_id):
    """Delete a dataset record."""
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM datasets_metadata WHERE id = ?",
        (dataset_id,)
    )
    conn.commit()
    return cursor.rowcount