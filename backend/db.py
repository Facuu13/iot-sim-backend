import sqlite3

DB_PATH = 'telemetry.db'

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT NOT NULL,
            device_type TEXT NOT NULL,
            status TEXT NOT NULL,
            battery_level REAL,
            value REAL,
            ts INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_telemetry(data):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO telemetry (device_id, device_type, status, battery_level, value, ts)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (data['device_id'], data['device_type'], data['status'], data['battery_level'], data['value'], data['ts']))
    conn.commit()
    conn.close()

