from app.models.properties import Property
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.property.propertySchema import PropertyCreate
from typing import List
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


from langchain_openai import ChatOpenAI
import os
import re
import json

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def get_all_properties(db: AsyncSession ):
    return db.query(Property).all()


def create_property (db:Session, data: PropertyCreate ):
    new_property = Property(**data.model_dump())
    db.add(new_property)
    db.commit()
    db.refresh(new_property)
    return new_property

def create_properties(db: Session, data: List[PropertyCreate] ):
    new_properties = [Property(**prop.model_dump())for prop in data]
    db.add_all(new_properties)
    db.commit()
    for prop in new_properties:
        db.refresh(prop)
    return new_properties


def update_property(db: Session,property_id: int , data: PropertyCreate):
    updated_property = db.query(Property).filter(Property.id == property_id).first()
    if not updated_property:
        return None

    for field, value in data.model_dump().items():
        setattr(updated_property, field, value)

    db.commit()
    db.refresh(updated_property)
    return updated_property

# Updating status of property
# def update_property_status(db: Session, property_id: int, status: str):
#     updated_property = db.query(Property).filter(Property.id == property_id).first()
#     if not updated_property:
#         return None
#     updated_property.status = status
#     db.commit()
#     db.refresh(updated_property)



def search_property(db: Session, q: str | None , page: int, items: int):
    query_property = db.query(Property)

    if q:
        query_property = query_property.filter(
            or_( 
                Property.name.ilike(f"%{q}%"),
                Property.address.ilike(f"%{q}%"),
                Property.state.ilike(f"%{q}%"),
                Property.city.ilike(f"%{q}%"),
                Property.status.ilike(f"%{q}%"),
                # Property.minPrice.ilike(f"%{q}%"),
                # Property.maxPrice.ilike(f"%{q}%")
            )
        )
    total = query_property.count()
    results = query_property.offset((page - 1 ) * items).limit(items).all()

    return results, total


# def get_property_by_filter(db: Session, property_id: int):
#     return db.query(Property).filter(Property.id == property_id).first()


#Property Search with AI

def search_properties_with_ai(prompt: str, db: Session):
    properties = db.query(Property).all()

    property_list = [{
        "id": prop.id, "name":prop.name, "city": prop.city, "price": prop.price, "state": prop.state, "address": prop.address,
    }
    for prop in properties
    ] 

    context_str = "\n".join([
    f"ID: {p['id']}, Name: {p['name']}, City: {p['city']}, Price: {p['price']}, State: {p['state']}, Address{p['address']}"
    for p in property_list
    ])

    template = PromptTemplate.from_template(
        "User query: {user_query}\n\nHere is a list of properties:\n{property_data}\n\n"
        "Return a JSON array of matching property IDs based on the user query."
    )

    final_prompt = template.format(
        user_query=prompt,
        property_data=context_str
    )

  
    llm = ChatOpenAI(
            temperature=0,
            model="gpt-4o-mini",
            openai_api_key=api_key 
    )
    response = llm.invoke(final_prompt)

    print("LLM response:", response.content)  
    try:
     
        raw_json = re.sub(r"^```(?:json)?\s*|```$", "", response.content.strip(), flags=re.IGNORECASE | re.MULTILINE)
        matching_ids = json.loads(raw_json)
    except Exception as e:
        print("Error parsing LLM response:", e)
        matching_ids = []


    return matching_ids