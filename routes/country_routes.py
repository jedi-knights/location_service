"""
This module contains the routes for the Country entity.
It is responsible for handling the HTTP requests.
"""

from fastapi import APIRouter
from repository.country import CountryRepository

router = APIRouter()


@router.get("/countries")
async def get_countries():
    """
    This function handles the GET request for the countries endpoint.
    """
    repo = CountryRepository()
    return repo.find_all()


@router.get("/countries/{country_id}")
async def get_country(country_id: int):
    """
    This function handles the GET request for the countries/{country_id} endpoint.
    """
    repo = CountryRepository()
    return repo.find_by_id(country_id)


@router.post("/countries")
async def create_country(data: dict):
    """
    This function handles the POST request for the countries endpoint.
    """
    repo = CountryRepository()
    return repo.create(data)


@router.put("/countries/{country_id}")
async def update_country(country_id: int, data: dict):
    """
    This function handles the PUT request for the countries/{country_id} endpoint.
    """
    repo = CountryRepository()
    return repo.update(country_id, data)


@router.delete("/countries/{country_id}")
async def delete_country(country_id: int):
    """
    This function handles the DELETE request for the countries/{id} endpoint.
    """
    repo = CountryRepository()
    return repo.delete(country_id)

# Path: microservices/location/repository/country_routes.py
