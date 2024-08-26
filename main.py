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
    try:
        conn = sqlite3.connect('db.sqlite')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail="Failed to connect to database")

# Customer Endpoints
@app.post("/customers")
def create_customer(customer: Customer):
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("INSERT INTO customers (name) VALUES (?)", (customer.name,))
        conn.commit()
        conn.close()
        return {"message": "Customer created"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail="Failed to create customer")

# ... (similar changes for other endpoints)