#!/usr/bin/python3
"""
Import Module for the Place class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Representation of a place its Attributes:
         city_id: This is the City id.
         user_id: The user's ID. Thirteen name: The location's name.
         description: The location's description.
         number_rooms: The location's total number of rooms.
         number_bathroom: The location's total number of bathrooms.
         max_guest: The location's maximum number of visitors.
         price_by_nigh: The location's price per night.
         latitude: This is the location's latitude.
         longitude: The location's longitude.
         amenity_ids: A list of the IDs of the amenities.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
