from backend.app.database.db import Base, engine


def create_tables():
    Base.metadata.create_all(bind=engine)
