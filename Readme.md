# FastAPI CRUD with MongoDB

This project demonstrates a simple FastAPI application that connects to a MongoDB database and implements CRUD (Create, Read, Update, Delete) operations for a "Todo" model.

## Tech Stack
- FastAPI (Web Framework)
- Pydantic (Data Validation)
- MongoDB (Database)
- pymongo (MongoDB Driver)


## Running Project
1. Install dependecies
    ```bash
    pip install -r requirements.txt
    ```
2. Set up MongoDB connection:
- Configure the MongoDB connection details in `src/config/connection_db.py`.

3. Start Application
    ```bash
    fastapi dev app/main.py
    ```
## Running Test
1. Run All Test
    ```bash
    pytest -v -s
    ```
2. Run Specific Scenario
    ```bash
    pytest -v -s tests/test_todo.py::<test_scenario_name>
    ```