"""
This module contains the routes for the Location entity.
It is responsible for handling the HTTP requests.
"""

from fastapi import APIRouter
from repository.location import LocationRepository

router = APIRouter()


@router.get("/locations")
async def get_locations():
    """
    This function handles the GET request for the locations endpoint.
    """
    repo = LocationRepository()
    return repo.find_all()


@router.get("/locations/{location_id}")
async def get_location(location_id: int):
    """
    This function handles the GET request for the locations/{location_id} endpoint.
    """
    repo = LocationRepository()
    return repo.find_by_id(location_id)


@router.post("/locations")
async def create_location(data: dict):
    """
    This function handles the POST request for the locations endpoint.
    """
    repo = LocationRepository()
    return repo.create(data)


@router.put("/locations/{location_id}")
async def update_location(location_id: int, data: dict):
    """
    This function handles the PUT request for the locations/{location_id} endpoint.
    """
    repo = LocationRepository()
    return repo.update(location_id, data)


@router.delete("/locations/{location_id}")
async def delete_location(location_id: int):
    """
    This function handles the DELETE request for the locations/{id} endpoint.
    """
    repo = LocationRepository()
    return repo.delete(location_id)

# Path: microservices/location/repository/location_routes.py
