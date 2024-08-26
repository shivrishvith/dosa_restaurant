import os
import sqlite3

def init_db():
    if not os.path.exists('db.sqlite'):
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()

        # Create tables
        c.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                item_id INTEGER,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers (id),
                FOREIGN KEY (item_id) REFERENCES items (id)
            )
        ''')

        conn.commit()
        conn.close()

if __name__ == '__main__':
    init_db()