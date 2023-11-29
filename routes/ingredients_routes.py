from fastapi import APIRouter, Depends, Request, HTTPException
from pydantic import BaseModel
from typing import List, Union
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine

ingredients_router = APIRouter()
models.Base.metadata.create_all(bind=engine)


@ingredients_router.post("/ingredients")
async def get_ingredients(request: Request):
    # Extract the ingredients from the request
    ingredients = await request.json()

    api_url = "https://api.spoonacular.com/recipes/findByIngredients"
    api_key = "&apiKey=34dbb4e97665494dbcee6c4c7a9d618c"
    url = f"{api_url}?ingredients={ingredients}&number=3{api_key}"

    # Make a request to the Spoonacular API
    response = await request.get(url)
    print(response)

    # If the response is not 200, raise an HTTPException
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail="Failed to fetch ingredient"
        )

    # Extract the value from the response
    return response.json()
