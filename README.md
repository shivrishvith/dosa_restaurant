
## Description
# Dosa Restaurant API

This project is a REST API backend for a dosa restaurant using FastAPI and SQLite. It provides CRUD operations for customers, items, and orders.

## Installation

1. Clone the repository.
2. Create a virtual environment:
      python -m venv venv
3. Activate the virtual environment:
      source venv/bin/activate
4. Install the dependencies:
      pip install -r requirements.txt
5. Initialize the database:
      python init_db.py
6. Run the application:
      uvicorn main:app –reload
      
## API Endpoints

- `POST /customers`: Create a customer.
- `GET /customers/{id}`: Retrieve a customer by ID.
- `PUT /customers/{id}`: Update a customer by ID.
- `DELETE /customers/{id}`: Delete a customer by ID.

- `POST /items`: Create an item.
- `GET /items/{id}`: Retrieve an item by ID.
- `PUT /items/{id}`: Update an item by ID.
- `DELETE /items/{id}`: Delete an item by ID.

- `POST /orders`: Create an order.
- `GET /orders/{id}`: Retrieve an order by ID.
- `PUT /orders/{id}`: Update an order by ID.
- `DELETE /orders/{id}`: Delete an order by ID.