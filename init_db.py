import os
import sqlite3
import json

def init_db():
    if not os.path.exists('db.sqlite'):
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()

        # Create tables
        c.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL
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
                timestamp INTEGER,
                notes TEXT,
                FOREIGN KEY (customer_id) REFERENCES customers(id),
                FOREIGN KEY (item_id) REFERENCES items(id)
            )
        ''')

        # Load data from JSON file
        with open('example_orders.json', 'r') as f:
            orders_data = json.load(f)

        # Insert customers and orders into the database
        for order in orders_data:
            # Insert customer
            c.execute("INSERT INTO customers (name, phone) VALUES (?, ?)",
                      (order['name'], order['phone']))
            customer_id = c.lastrowid
            print(f"Inserted customer: {order['name']} with phone {order['phone']}")

            # Insert items and orders
            for item in order['items']:
                # Check if the item already exists
                c.execute("SELECT id FROM items WHERE name = ? AND price = ?",
                          (item['name'], item['price']))
                item_row = c.fetchone()

                if item_row:
                    item_id = item_row[0]
                else:
                    c.execute("INSERT INTO items (name, price) VALUES (?, ?)",
                              (item['name'], item['price']))
                    item_id = c.lastrowid
                    print(f"Inserted item: {item['name']} at price {item['price']}")

                # Insert order
                c.execute("INSERT INTO orders (customer_id, item_id, quantity, timestamp, notes) VALUES (?, ?, ?, ?, ?)",
                          (customer_id, item_id, 1, order['timestamp'], order['notes']))
                print(f"Inserted order for customer ID {customer_id} with item ID {item_id} at timestamp {order['timestamp']}")

        conn.commit()
        conn.close()

if __name__ == '__main__':
    init_db()