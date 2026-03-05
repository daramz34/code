from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

tasks = [
    {"id": 1, "title": "Task A", "status": "In Progress"},
    {"id": 2, "title": "Task B", "status": "Done"},

]
   
class Item(BaseModel):
    
    title: str
    description: Optional[str] = None
    status: Optional[str] = "Pending"


@app.post("/tasks/{id}")
def create_task(id: int, item: Item):
    for t in tasks:
        if t["id"] == id:
            raise HTTPException(status_code=400, detail="ID already exists")
    

    new_task = item.dict()
    new_task["id"] = id

    tasks.append(new_task)

    return new_task

    
    

@app.get("/tasks")
def get_task():
    return tasks
