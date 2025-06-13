from fastapi import APIRouter, HTTPException
from app.schemas.propertySchema import PropertyBase, PropertyCreate
from app.services.propertyService import get_all_properties, create_property


