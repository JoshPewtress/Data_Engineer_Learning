import sqlite3
from config import DB_PATH

def create_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def execute_command(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)

def execute_insert(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.lastrowid

def execute_query(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()