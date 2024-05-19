"""
This Module contains the routes for the Postal Code entity.
It is responsible for handling the HTTP requests.
"""

from fastapi import APIRouter
from repository.postal_code import PostalCodeRepository

router = APIRouter()


@router.get("/postal_codes")
async def get_postal_codes():
    """
    This function handles the GET request for the postal_codes endpoint.
    """
    repo = PostalCodeRepository()
    return repo.find_all()


@router.get("/postal_codes/{postal_id}")
async def get_postal_code(postal_id: int):
    """
    This function handles the GET request for the postal_codes/{postal_id} endpoint.
    """
    repo = PostalCodeRepository()
    return repo.find_by_id(postal_id)


@router.post("/postal_codes")
async def create_postal_code(data: dict):
    """
    This function handles the POST request for the postal_codes endpoint.
    """
    repo = PostalCodeRepository()
    return repo.create(data)


@router.put("/postal_codes/{postal_id}")
async def update_postal_code(postal_id: int, data: dict):
    """
    This function handles the PUT request for the postal_codes/{postal_id} endpoint.
    """
    repo = PostalCodeRepository()
    return repo.update(postal_id, data)


@router.delete("/postal_codes/{postal_id}")
async def delete_postal_code(postal_id: int):
    """
    This function handles the DELETE request for the postal_codes/{id} endpoint.
    """
    repo = PostalCodeRepository()
    return repo.delete(postal_id)

# Path: microservices/location/repository/postal_code_routes.py
