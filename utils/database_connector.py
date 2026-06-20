import sqlite3

def log_transaction(ride_data):
    """Stores ride history into a local SQLite ledger."""
    conn = sqlite3.connect('fleet_ledger.db')
    cursor = conn.cursor()
    # Insert ride data into ledger
    conn.commit()
    conn.close()
  
