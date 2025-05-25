from repositories.sqlalchemy.base import engine
from repositories.sqlalchemy.models.user_model import Base

def init_db():
    print("Creating database and tables...")
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()
