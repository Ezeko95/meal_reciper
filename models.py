from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    recipes = relationship("Recipes", back_populates="owner")


class Recipes(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    recipe_name = Column(String)
    description = Column(String)
    ingredients = Column(String)
    instructions = Column(String)
    image = Column(String)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="recipes")
