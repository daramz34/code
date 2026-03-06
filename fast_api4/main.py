from fastapi import FastAPI
from fast_api4.database import Base, engine, SessionLocal
import fast_api4.model as model
from fast_api4.schemas import Task_Create



Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/tasks/")
def create_task(task_data: Task_Create):
    db = SessionLocal()
    try:
        new_item = model.Task(
            name = task_data.name,
            description = task_data.description,
            price = task_data.price,
            

        )
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    finally:
        db.close()

@app.get("/tasks/")
def get_all_task():
    db = SessionLocal()
    try:
        task = db.query(model.Task).all()
        return {
            "data" : task 
        }
    finally:
        db.close()




# What is abt 
# Day 7 Summary: Persistent Data Retrieval
# The Goal
# The core objective of Day 7 was to transition from volatile memory (data that disappears when the server stops) to persistent storage using an ORM (Object Relational Mapper).

# What I Implemented
# Database Modeling: Created an Item model using SQLAlchemy to define a structured table in SQLite. This table includes fields for name, description, price, and created_at.

# CRUD Logic (Read All): Developed a GET /items/ endpoint that queries the database to fetch every record stored in the items table.

# Data Consistency: Ensured the API response follows a standard JSON structure by wrapping the results in a {"data": [...]} object.

# Database Synchronization: Learned how to handle schema changes by managing the SQLite database file and ensuring the Python models match the physical database columns.

# The Impact
# Instead of a temporary list, my API now interacts with a real database file (tasks.db). This allows the application to maintain state across restarts, forming the backbone of any production-ready backend system.