## Dosa Restaurant API

This Python application serves as the backend for managing customer orders at a Dosa restaurant. It utilizes FastAPI and SQLite to create a REST API that allows CRUD operations for customers, menu items, and orders. The application is designed to manage customer information, track menu items, and process orders efficiently.

## Setup

To get started, ensure you have Python 3 installed on your machine. Clone this repository to your local environment to begin working with the API.

### Requirements

- Python 3.x
- FastAPI and SQLite (dependencies are installed via `requirements.txt`)
- Any code editor (I used VSCode for this project)

### Running the Application

To start the API, navigate to the project directory in your terminal and follow these steps:

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the SQLite database**:
   ```bash
   python init_db.py
   ```

   This command sets up an SQLite database (`db.sqlite`) with the necessary tables for customers, items, and orders.

5. **Run the FastAPI application**:
   ```bash
   uvicorn main:app --reload
   ```

   This command starts the FastAPI server, allowing you to interact with the API through your browser or API clients like Postman.

### API Endpoints

The API provides several endpoints to manage customers, items, and orders:

- **Customers**:
  - `POST /customers`: Create a new customer.
  - `GET /customers/{id}`: Retrieve a customer by ID.
  - `PUT /customers/{id}`: Update a customer's details.
  - `DELETE /customers/{id}`: Remove a customer from the database.

- **Items**:
  - `POST /items`: Add a new item to the menu.
  - `GET /items/{id}`: Retrieve an item by ID.
  - `PUT /items/{id}`: Update an item's details.
  - `DELETE /items/{id}`: Remove an item from the menu.

- **Orders**:
  - `POST /orders`: Create a new order.
  - `GET /orders/{id}`: Retrieve an order by ID.
  - `PUT /orders/{id}`: Update an order's details.
  - `DELETE /orders/{id}`: Cancel an order.

Each endpoint interacts with the SQLite database (`db.sqlite`) to perform the necessary operations. The API documentation is automatically generated and can be accessed at `http://127.0.0.1:8000/docs` when the server is running.

## Project Structure

- **main.py**: The FastAPI application script, containing all the API endpoint definitions.
- **init_db.py**: Script to initialize the SQLite database with the required tables.
- **requirements.txt**: List of dependencies required to run the application.
- **db.sqlite**: SQLite database file (generated after running `init_db.py`).

## Contributions

Contributions to this project are welcome. Please fork the repository and submit pull requests for review. If you're planning significant changes, it's recommended to open an issue first to discuss your proposal.

### More Info

Replace `python3` with `python` if your system's Python command differs. This README provides a clear, concise guide to understanding, setting up, and running your project, suitable for inclusion in your GitHub repository.
