from shared.database import engine
from shared.models import Base

Base.metadata.create_all(bind=engine)
print("Database tables created.")
