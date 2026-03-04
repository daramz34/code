from fast_api.database import engine, Base
from fast_api.models import Item

Base.metadata.create_all(bind=engine)
print("Tables created")