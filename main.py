"""
This is the main entrypoint to the API. It is responsible for starting the FastAPI server and
loading the routes.
"""
import sys

from dotenv import load_dotenv
from fastapi import FastAPI

from routes import country_routes, city_routes, state_routes, location_routes, postal_code_routes

load_dotenv()

app = FastAPI()

app.include_router(country_routes.router)
app.include_router(state_routes.router)
app.include_router(city_routes.router)
app.include_router(postal_code_routes.router)
app.include_router(location_routes.router)


@app.get("/")
async def root():
    """
    Root route for the API
    """
    return {"message": "Hello World"}

if __name__ == "__main__":
    for item in sys.path:
        print(item)
