from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from ..crud import (
    create_contact,
    get_contacts,
    get_contact_by_id,
    update_contact,
    delete_contact,
)
from ..database import database
from ..models import Contact
from ..schemas import ContactCreate, ContactUpdate, Contact

router = APIRouter()

@router.post("/contacts/", response_model=Contact)
async def create_contact(contact: ContactCreate, db: Session = Depends(database.get_db)):
    db_contact = create_contact(db, contact)
    return db_contact

@router.get("/contacts/", response_model=List[Contact])
async def list_contacts(skip: int = Query(0, description="Skip rows"), limit: int = Query(100, description="Limit rows"), db: Session = Depends(database.get_db)):
    contacts = get_contacts(db, skip, limit)
    return contacts

@router.get("/contacts/{contact_id}", response_model=Contact)
async def read_contact(contact_id: int, db: Session = Depends(database.get_db)):
    contact = get_contact_by_id(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.put("/contacts/{contact_id}", response_model=Contact)
async def update_contact_info(contact_id: int, contact_data: ContactUpdate, db: Session = Depends(database.get_db)):
    contact = update_contact(db, contact_id, contact_data)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.delete("/contacts/{contact_id}", response_model=Contact)
async def delete_contact_by_id(contact_id: int, db: Session = Depends(database.get_db)):
    contact = delete_contact(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact
