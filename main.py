from fastapi import FastAPI
from routes import user_routes, ingredients_routes

app = FastAPI()
app.include_router(user_routes.user_router)
app.include_router(ingredients_routes.ingredients_router)