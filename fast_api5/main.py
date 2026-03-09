from fastapi import FastAPI
from fast_api5.database import engine, Base, SessionLocal
from fast_api5.schema import ItemResponse, ItemCreate
from fast_api5.models import Task

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate):
    db = SessionLocal()
    try: 
        new_item = Task(
            name=item.name,
            price = item.price,
            description = item.description,
            secret_admin_note = "TOP_SECRET_123"
        )
        db.add(new_item)
        db.commit()
        db.refresh(new_item)

        return new_item
    finally:
        db.close()


@app.get("/items/", response_model=list[ItemResponse])
def get_items():
    db= SessionLocal()
    try:
        items = db.query(Task).all()

        return items
    finally:
        db.close()




# 🚀 Days 7 & 8: The Persistence & Security MilestoneThe Problem We 
# SolvedBefore today, our data lived in "RAM"—it disappeared every time the 
# server restarted. We also had no way to hide sensitive internal notes from the public API.What We BuiltSQLAlchemy Integration (Day 7): 
# We connected FastAPI to a SQLite database.
# We learned that the Model is the "Source of Truth" for the database.CRUD Implementation: We built a POST route to save data and a GET route to fetch it. 
# We learned that if we change the Model, we have to reset the .db file so the columns stay in sync.Pydantic Serializers (Day 8): We moved from one schema to 
# two:ItemCreate: Validates the data coming in.ItemResponse: Filters the data going out.The "Security Guard" (Response Model): We used response_model to automatically 
# strip out secret_admin_note from our JSON, ensuring our API is secure and professional.Key Concepts MasteredConceptRoleReal-World AnalogyModelDatabase TableThe Warehouse 
# (Stores everything)SchemaAPI ShapeThe Shop Window (Only shows what's for sale)SessionLocalDB ConnectionThe Delivery Truck (Moves data to/from the warehouse)MigrationSchema UpdateRenovating 
#                                                    the Warehouse (Why we deleted the .db file