"""
This module contains routes for the State entity.
It is responsible for handling the HTTP requests.
"""

from fastapi import APIRouter
from repository.state import StateRepository

router = APIRouter()


@router.get("/states")
async def get_states():
    """
    This function handles the GET request for the states endpoint.
    """
    repo = StateRepository()
    return repo.find_all()


@router.get("/states/{state_id}")
async def get_state(state_id: int):
    """
    This function handles the GET request for the states/{state_id} endpoint.
    """
    repo = StateRepository()
    return repo.find_by_id(state_id)


@router.post("/states")
async def create_state(data: dict):
    """
    This function handles the POST request for the states endpoint.
    """
    repo = StateRepository()
    return repo.create(data)


@router.put("/states/{state_id}")
async def update_state(state_id: int, data: dict):
    """
    This function handles the PUT request for the states/{state_id} endpoint.
    """
    repo = StateRepository()
    return repo.update(state_id, data)


@router.delete("/states/{state_id}")
async def delete_state(state_id: int):
    """
    This function handles the DELETE request for the states/{id} endpoint.
    """
    repo = StateRepository()
    return repo.delete(state_id)

# Path: microservices/location/repository/state_routes.py
