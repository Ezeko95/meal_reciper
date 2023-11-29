from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define your database URL based on your database type, username, password, host, port, and database name
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/meal_recipe"

# Create an async engine
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for your models
Base = declarative_base()
