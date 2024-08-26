from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Customer model
class Customer(BaseModel):
    name: str

# Database helper
def get_db_connection():
    try:
        conn = sqlite3.connect('db.sqlite')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail="Failed to connect to database")

@app.post("/customers")
def create_customer(customer: Customer):
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO customers (name) VALUES (?)", (customer.name,))
            conn.commit()
            return {"message": "Customer created"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Failed to create customer: {e}")

@app.get("/customers/{id}")
def get_customer(id: int):
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM customers WHERE id = ?", (id,))
            customer = c.fetchone()
            if customer is None:
                raise HTTPException(status_code=404, detail="Customer not found")
            return dict(customer)
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve customer: {e}")

@app.put("/customers/{id}")
def update_customer(id: int, customer: Customer):
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("UPDATE customers SET name = ? WHERE id = ?", (customer.name, id))
            conn.commit()
            if c.rowcount == 0:
                raise HTTPException(status_code=404, detail="Customer not found")
            return {"message": "Customer updated"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Failed to update customer: {e}")

@app.delete("/customers/{id}")
def delete_customer(id: int):
    try:
        with get_db_connection() as conn:
            c = conn.cursor()
            c.execute("DELETE FROM customers WHERE id = ?", (id,))
            conn.commit()
            if c.rowcount == 0:
                raise HTTPException(status_code=404, detail="Customer not found")
            return {"message": "Customer deleted"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete customer: {e}")