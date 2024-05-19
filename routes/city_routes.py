"""
This module contains the routes for the City entity.
It is responsible for handling the HTTP requests.
"""

from fastapi import APIRouter
from repository.city import CityRepository

router = APIRouter()


@router.get("/cities")
async def get_cities():
    """
    This function handles the GET request for the cities endpoint.
    """
    repo = CityRepository()
    return repo.find_all()


@router.get("/cities/{city_id}")
async def get_city(city_id: int):
    """
    This function handles the GET request for the cities/{city_id} endpoint.
    """
    repo = CityRepository()
    return repo.find_by_id(city_id)


@router.post("/cities")
async def create_city(data: dict):
    """
    This function handles the POST request for the cities endpoint.
    """
    repo = CityRepository()
    return repo.create(data)


@router.put("/cities/{city_id}")
async def update_city(city_id: int, data: dict):
    """
    This function handles the PUT request for the cities/{city_id} endpoint.
    """
    repo = CityRepository()
    return repo.update(city_id, data)


@router.delete("/cities/{city_id}")
async def delete_city(city_id: int):
    """
    This function handles the DELETE request for the cities/{id} endpoint.
    """
    repo = CityRepository()
    return repo.delete(city_id)

# Path: microservices/location/repository/city_routes.py
