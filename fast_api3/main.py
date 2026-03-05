from fastapi import FastAPI
from fast_api3.database import Base, engine, SessionLocal
from fast_api3.models import Task
from fast_api3.schemas import Task_Create



Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/tasks/")
def create_task(task_data: Task_Create):
    db = SessionLocal()
    new_task = Task(title=task_data.title, description=task_data.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task



class User:
    def __init__(self, username):
        self.username = username

    def to_dict(self):
        return {
            "username" : self.username
        }
    

my_user = User("Daramz")
print(my_user.to_dict())