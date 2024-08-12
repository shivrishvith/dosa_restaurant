from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List

app = FastAPI()

# Models
class Customer(BaseModel):
    name: str

class Item(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    customer_id: int
    item_id: int
    quantity: int

# Database Helper
def get_db_connection():
    conn = sqlite3.connect('db.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

# Customer Endpoints
@app.post("/customers")
def create_customer(customer: Customer):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO customers (name) VALUES (?)", (customer.name,))
    conn.commit()
    conn.close()
    return {"message": "Customer created"}

@app.get("/customers/{id}")
def read_customer(id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE id=?", (id,))
    customer = c.fetchone()
    conn.close()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return dict(customer)

@app.put("/customers/{id}")
def update_customer(id: int, customer: Customer):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE customers SET name=? WHERE id=?", (customer.name, id))
    conn.commit()
    conn.close()
    return {"message": "Customer updated"}

@app.delete("/customers/{id}")
def delete_customer(id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {"message": "Customer deleted"}

# Item Endpoints
@app.post("/items")
def create_item(item: Item):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO items (name, price) VALUES (?, ?)", (item.name, item.price))
    conn.commit()
    conn.close()
    return {"message": "Item created"}

@app.get("/items/{id}")
def read_item(id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM items WHERE id=?", (id,))
    item = c.fetchone()
    conn.close()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return dict(item)

@app.put("/items/{id}")
def update_item(id: int, item: Item):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE items SET name=?, price=? WHERE id=?", (item.name, item.price, id))
    conn.commit()
    conn.close()
    return {"message": "Item updated"}

@app.delete("/items/{id}")
def delete_item(id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM items WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {"message": "Item deleted"}

# Order Endpoints
@app.post("/orders")
def create_order(order: Order):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO orders (customer_id, item_id, quantity) VALUES (?, ?, ?)",
              (order.customer_id, order.item_id, order.quantity))
    conn.commit()
    conn.close()
    return {"message": "Order created"}

@app.get("/orders/{id}")
def read_order(id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM orders WHERE id=?", (id,))
    order = c.fetchone()
    conn.close()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return dict(order)

@app.put("/orders/{id}")
def update_order(id: int, order: Order):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE orders SET customer_id=?, item_id=?, quantity=? WHERE id=?",
              (order.customer_id, order.item_id, order.quantity, id))
    conn.commit()
    conn.close()
    return {"message": "Order updated"}

@app.delete("/orders/{id}")
def delete_order(id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM orders WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return {"message": "Order deleted"}
